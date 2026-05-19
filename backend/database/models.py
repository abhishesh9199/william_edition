from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean, JSON, ForeignKey, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

Base = declarative_base()

class UserRole(str, enum.Enum):
    STUDENT = "student"
    TEACHER = "teacher"
    ADMIN = "admin"

class CourseStatus(str, enum.Enum):
    ACTIVE = "active"
    DRAFT = "draft"
    ARCHIVED = "archived"

class EnrollmentStatus(str, enum.Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    EXPIRED = "expired"

class PaymentStatus(str, enum.Enum):
    CREATED = "created"
    AUTHORIZED = "authorized"
    CAPTURED = "captured"
    FAILED = "failed"

class DifficultyLevel(str, enum.Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String, nullable=True)
    role = Column(SQLEnum(UserRole), default=UserRole.STUDENT)
    preferred_language = Column(String, default="en")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    courses = relationship("Course", back_populates="teacher")
    enrollments = relationship("Enrollment", back_populates="user")
    payments = relationship("Payment", back_populates="user")
    quiz_responses = relationship("UserQuizResponse", back_populates="user")

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    description = Column(Text)
    subject = Column(String)
    board = Column(String)  # CBSE, ICSE, State, Olympiad
    grade_level = Column(String)  # 3-5, 6-8, 9-10
    language = Column(String, default="en")
    price = Column(Float, default=0)
    duration_hours = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(SQLEnum(CourseStatus), default=CourseStatus.ACTIVE)

    teacher = relationship("User", back_populates="courses")
    content = relationship("CourseContent", back_populates="course")
    enrollments = relationship("Enrollment", back_populates="course")
    payments = relationship("Payment", back_populates="course")
    quiz_questions = relationship("QuizQuestion", back_populates="course")

class CourseContent(Base):
    __tablename__ = "course_content"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    content_type = Column(String)  # lesson, video, pdf, quiz
    title = Column(String)
    description = Column(Text, nullable=True)
    order = Column(Integer)
    language = Column(String, default="en")
    content_url = Column(String, nullable=True)

    course = relationship("Course", back_populates="content")

class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    enrollment_date = Column(DateTime, default=datetime.utcnow)
    status = Column(SQLEnum(EnrollmentStatus), default=EnrollmentStatus.ACTIVE)
    progress_percentage = Column(Float, default=0)
    payment_id = Column(Integer, ForeignKey("payments.id"), nullable=True)

    user = relationship("User", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    amount = Column(Float)
    currency = Column(String, default="INR")
    payment_method = Column(String)  # razorpay, etc
    razorpay_order_id = Column(String, nullable=True)
    razorpay_payment_id = Column(String, nullable=True)
    status = Column(SQLEnum(PaymentStatus), default=PaymentStatus.CREATED)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="payments")
    course = relationship("Course", back_populates="payments")

class QuizQuestion(Base):
    __tablename__ = "quiz_questions"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    content_id = Column(Integer, ForeignKey("course_content.id"), nullable=True)
    question_text = Column(String)
    options = Column(JSON)  # {"A": "option1", "B": "option2", ...}
    correct_answer = Column(String)
    difficulty_level = Column(SQLEnum(DifficultyLevel), default=DifficultyLevel.MEDIUM)
    language = Column(String, default="en")

    course = relationship("Course", back_populates="quiz_questions")

class UserQuizResponse(Base):
    __tablename__ = "user_quiz_responses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("quiz_questions.id"))
    selected_answer = Column(String)
    is_correct = Column(Boolean)
    score = Column(Float, default=0)
    attempted_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="quiz_responses")
