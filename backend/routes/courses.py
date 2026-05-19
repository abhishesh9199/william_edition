from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from database.db import get_db
from database.models import Course, CourseContent, User, UserRole
from schemas.user import CourseResponse, CourseCreate, CourseUpdate, CourseContentResponse, CourseContentCreate
from routes.auth import get_current_user

router = APIRouter(prefix="/courses", tags=["courses"])

@router.get("/", response_model=List[CourseResponse])
def list_courses(
    subject: Optional[str] = None,
    board: Optional[str] = None,
    grade_level: Optional[str] = None,
    language: Optional[str] = "en",
    db: Session = Depends(get_db)
):
    query = db.query(Course).filter(Course.status == "active")

    if subject:
        query = query.filter(Course.subject == subject)
    if board:
        query = query.filter(Course.board == board)
    if grade_level:
        query = query.filter(Course.grade_level == grade_level)
    if language:
        query = query.filter(Course.language == language)

    return query.all()

@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.post("/", response_model=CourseResponse)
def create_course(
    course_data: CourseCreate,
    token: str = None,
    db: Session = Depends(get_db)
):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = get_current_user(token, db)
    if user.role not in [UserRole.TEACHER, UserRole.ADMIN]:
        raise HTTPException(status_code=403, detail="Only teachers can create courses")

    new_course = Course(
        teacher_id=user.id,
        title=course_data.title,
        description=course_data.description,
        subject=course_data.subject,
        board=course_data.board,
        grade_level=course_data.grade_level,
        language=course_data.language,
        price=course_data.price,
        duration_hours=course_data.duration_hours
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@router.put("/{course_id}", response_model=CourseResponse)
def update_course(
    course_id: int,
    course_data: CourseUpdate,
    token: str = None,
    db: Session = Depends(get_db)
):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = get_current_user(token, db)
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    if course.teacher_id != user.id and user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Cannot update this course")

    if course_data.title:
        course.title = course_data.title
    if course_data.description:
        course.description = course_data.description
    if course_data.subject:
        course.subject = course_data.subject
    if course_data.board:
        course.board = course_data.board
    if course_data.grade_level:
        course.grade_level = course_data.grade_level
    if course_data.price is not None:
        course.price = course_data.price
    if course_data.duration_hours:
        course.duration_hours = course_data.duration_hours

    db.commit()
    db.refresh(course)
    return course

@router.delete("/{course_id}")
def delete_course(
    course_id: int,
    token: str = None,
    db: Session = Depends(get_db)
):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = get_current_user(token, db)
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    if course.teacher_id != user.id and user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Cannot delete this course")

    db.delete(course)
    db.commit()
    return {"message": "Course deleted successfully"}

@router.post("/{course_id}/content", response_model=CourseContentResponse)
def add_course_content(
    course_id: int,
    content_data: CourseContentCreate,
    token: str = None,
    db: Session = Depends(get_db)
):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = get_current_user(token, db)
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    if course.teacher_id != user.id and user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Cannot add content to this course")

    new_content = CourseContent(
        course_id=course_id,
        content_type=content_data.content_type,
        title=content_data.title,
        description=content_data.description,
        order=content_data.order,
        language=content_data.language,
        content_url=content_data.content_url
    )
    db.add(new_content)
    db.commit()
    db.refresh(new_content)
    return new_content

@router.get("/{course_id}/content", response_model=List[CourseContentResponse])
def get_course_content(course_id: int, db: Session = Depends(get_db)):
    content = db.query(CourseContent).filter(CourseContent.course_id == course_id).order_by(CourseContent.order).all()
    return content
