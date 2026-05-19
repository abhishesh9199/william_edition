from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import razorpay
import os
from dotenv import load_dotenv
from database.db import get_db
from database.models import Payment, Enrollment, Course, PaymentStatus, EnrollmentStatus
from schemas.user import PaymentCreateRequest, PaymentResponse, PaymentVerify
from routes.auth import get_current_user

load_dotenv()

router = APIRouter(prefix="/payment", tags=["payment"])

RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

@router.post("/create-order", response_model=PaymentResponse)
def create_payment_order(
    payment_data: PaymentCreateRequest,
    token: str = None,
    db: Session = Depends(get_db)
):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = get_current_user(token, db)
    course = db.query(Course).filter(Course.id == payment_data.course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    existing_enrollment = db.query(Enrollment).filter(
        Enrollment.user_id == user.id,
        Enrollment.course_id == payment_data.course_id
    ).first()

    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Already enrolled in this course")

    try:
        razorpay_order = client.order.create(dict(
            amount=int(payment_data.amount * 100),
            currency="INR",
            payment_capture=1
        ))

        payment = Payment(
            user_id=user.id,
            course_id=payment_data.course_id,
            amount=payment_data.amount,
            currency="INR",
            payment_method="razorpay",
            razorpay_order_id=razorpay_order["id"],
            status=PaymentStatus.CREATED
        )
        db.add(payment)
        db.commit()
        db.refresh(payment)

        return payment
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/verify", response_model=PaymentResponse)
def verify_payment(
    verify_data: PaymentVerify,
    token: str = None,
    db: Session = Depends(get_db)
):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = get_current_user(token, db)

    payment = db.query(Payment).filter(
        Payment.razorpay_order_id == verify_data.razorpay_order_id,
        Payment.user_id == user.id
    ).first()

    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    try:
        payment_details = client.payment.fetch(verify_data.razorpay_payment_id)

        if payment_details["status"] == "captured":
            payment.razorpay_payment_id = verify_data.razorpay_payment_id
            payment.status = PaymentStatus.CAPTURED

            enrollment = Enrollment(
                user_id=user.id,
                course_id=payment.course_id,
                status=EnrollmentStatus.ACTIVE,
                payment_id=payment.id
            )
            db.add(enrollment)
            db.commit()
            db.refresh(payment)

            return payment
        else:
            payment.status = PaymentStatus.FAILED
            db.commit()
            raise HTTPException(status_code=400, detail="Payment verification failed")

    except HTTPException:
        raise
    except Exception as e:
        payment.status = PaymentStatus.FAILED
        db.commit()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/webhook")
def payment_webhook(payload: dict, db: Session = Depends(get_db)):
    event = payload.get("event")

    if event == "payment.authorized":
        payment_id = payload.get("payload", {}).get("payment", {}).get("entity", {}).get("id")
        order_id = payload.get("payload", {}).get("payment", {}).get("entity", {}).get("order_id")

        payment = db.query(Payment).filter(Payment.razorpay_order_id == order_id).first()
        if payment:
            payment.razorpay_payment_id = payment_id
            payment.status = PaymentStatus.AUTHORIZED
            db.commit()

    return {"status": "received"}
