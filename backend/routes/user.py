from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database.db import get_db
from database.models import User, Enrollment
from schemas.user import UserResponse, UserUpdate, EnrollmentResponse
from routes.auth import get_current_user

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/profile", response_model=UserResponse)
def get_profile(token: str = None, db: Session = Depends(get_db)):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    user = get_current_user(token, db)
    return user

@router.put("/profile", response_model=UserResponse)
def update_profile(
    data: UserUpdate,
    token: str = None,
    db: Session = Depends(get_db)
):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = get_current_user(token, db)

    if data.first_name:
        user.first_name = data.first_name
    if data.last_name:
        user.last_name = data.last_name
    if data.phone:
        user.phone = data.phone
    if data.preferred_language:
        user.preferred_language = data.preferred_language

    db.commit()
    db.refresh(user)
    return user

@router.get("/enrollments", response_model=List[EnrollmentResponse])
def get_enrollments(token: str = None, db: Session = Depends(get_db)):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = get_current_user(token, db)
    enrollments = db.query(Enrollment).filter(Enrollment.user_id == user.id).all()
    return enrollments
