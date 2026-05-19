from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# User Schemas
class UserRegister(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    phone: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    role: str
    preferred_language: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    preferred_language: Optional[str] = None

# Course Schemas
class CourseCreate(BaseModel):
    title: str
    description: str
    subject: str
    board: str  # CBSE, ICSE, State, Olympiad
    grade_level: str
    language: str = "en"
    price: float = 0
    duration_hours: int = 0

class CourseResponse(BaseModel):
    id: int
    teacher_id: int
    title: str
    description: str
    subject: str
    board: str
    grade_level: str
    language: str
    price: float
    duration_hours: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    subject: Optional[str] = None
    board: Optional[str] = None
    grade_level: Optional[str] = None
    price: Optional[float] = None
    duration_hours: Optional[int] = None

# Course Content Schemas
class CourseContentCreate(BaseModel):
    content_type: str  # lesson, video, pdf, quiz
    title: str
    description: Optional[str] = None
    order: int
    language: str = "en"
    content_url: Optional[str] = None

class CourseContentResponse(BaseModel):
    id: int
    course_id: int
    content_type: str
    title: str
    description: Optional[str]
    order: int
    language: str
    content_url: Optional[str]

    class Config:
        from_attributes = True

# Enrollment Schemas
class EnrollmentCreate(BaseModel):
    course_id: int

class EnrollmentResponse(BaseModel):
    id: int
    user_id: int
    course_id: int
    enrollment_date: datetime
    status: str
    progress_percentage: float

    class Config:
        from_attributes = True

# Payment Schemas
class PaymentCreateRequest(BaseModel):
    course_id: int
    amount: float

class PaymentResponse(BaseModel):
    id: int
    user_id: int
    course_id: int
    amount: float
    currency: str
    razorpay_order_id: Optional[str]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class PaymentVerify(BaseModel):
    razorpay_order_id: str
    razorpay_payment_id: str
    razorpay_signature: str

# Quiz Schemas
class QuizQuestionCreate(BaseModel):
    course_id: int
    content_id: Optional[int] = None
    question_text: str
    options: dict  # {"A": "option1", "B": "option2", ...}
    correct_answer: str
    difficulty_level: str = "medium"
    language: str = "en"

class QuizQuestionResponse(BaseModel):
    id: int
    course_id: int
    question_text: str
    options: dict
    difficulty_level: str
    language: str

    class Config:
        from_attributes = True

class QuizSubmit(BaseModel):
    question_id: int
    selected_answer: str

class QuizResponseCreate(BaseModel):
    question_id: int
    selected_answer: str

# Token Schema
class Token(BaseModel):
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "bearer"
