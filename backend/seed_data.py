import sys
sys.path.insert(0, '/backend')

from database.db import SessionLocal, engine
from database.models import Base, User, Course, CourseContent, QuizQuestion, UserRole, CourseStatus
from utils.security import get_password_hash
from datetime import datetime

Base.metadata.create_all(bind=engine)
db = SessionLocal()

sample_courses = [
    {
        "title": "Math Basics for Grade 3-5",
        "description": "Learn fundamental math concepts including addition, subtraction, multiplication, and division.",
        "subject": "Math",
        "board": "CBSE",
        "grade_level": "3-5",
        "price": 299,
        "duration_hours": 10,
        "language": "en",
        "content": [
            {"title": "Introduction to Numbers", "type": "lesson", "order": 1},
            {"title": "Addition Basics", "type": "lesson", "order": 2},
            {"title": "Math Quiz 1", "type": "quiz", "order": 3},
        ]
    },
    {
        "title": "English Language Fundamentals",
        "description": "Master English grammar, vocabulary, and communication skills.",
        "subject": "English",
        "board": "CBSE",
        "grade_level": "3-5",
        "price": 249,
        "duration_hours": 8,
        "language": "en",
        "content": [
            {"title": "Alphabets and Phonics", "type": "lesson", "order": 1},
            {"title": "Simple Sentences", "type": "lesson", "order": 2},
        ]
    },
    {
        "title": "Science Fundamentals",
        "description": "Explore the basics of biology, physics, and chemistry.",
        "subject": "Science",
        "board": "CBSE",
        "grade_level": "3-5",
        "price": 299,
        "duration_hours": 12,
        "language": "en",
        "content": [
            {"title": "Living and Non-living Things", "type": "lesson", "order": 1},
            {"title": "Human Body Basics", "type": "lesson", "order": 2},
        ]
    },
    {
        "title": "Social Studies - Our World",
        "description": "Learn about geography, history, and culture.",
        "subject": "Social Studies",
        "board": "CBSE",
        "grade_level": "3-5",
        "price": 199,
        "duration_hours": 6,
        "language": "en",
        "content": [
            {"title": "Countries and Continents", "type": "lesson", "order": 1},
            {"title": "Historical Timelines", "type": "lesson", "order": 2},
        ]
    },
    {
        "title": "Algebra for Grade 6-8",
        "description": "Master algebraic expressions, equations, and problem solving.",
        "subject": "Math",
        "board": "CBSE",
        "grade_level": "6-8",
        "price": 399,
        "duration_hours": 15,
        "language": "en",
        "content": [
            {"title": "Variables and Expressions", "type": "lesson", "order": 1},
            {"title": "Linear Equations", "type": "lesson", "order": 2},
        ]
    },
    {
        "title": "Physics Essentials",
        "description": "Understand motion, forces, energy, and light.",
        "subject": "Physics",
        "board": "ICSE",
        "grade_level": "6-8",
        "price": 449,
        "duration_hours": 18,
        "language": "en",
        "content": [
            {"title": "Motion and Speed", "type": "lesson", "order": 1},
            {"title": "Forces and Friction", "type": "lesson", "order": 2},
        ]
    },
    {
        "title": "Chemistry Made Simple",
        "description": "Learn about atoms, molecules, and chemical reactions.",
        "subject": "Chemistry",
        "board": "ICSE",
        "grade_level": "6-8",
        "price": 449,
        "duration_hours": 16,
        "language": "en",
        "content": [
            {"title": "Elements and Compounds", "type": "lesson", "order": 1},
            {"title": "Chemical Reactions", "type": "lesson", "order": 2},
        ]
    },
    {
        "title": "Biology for Grade 9-10",
        "description": "Study cells, organisms, ecology, and evolution.",
        "subject": "Biology",
        "board": "State",
        "grade_level": "9-10",
        "price": 499,
        "duration_hours": 20,
        "language": "en",
        "content": [
            {"title": "Cell Structure", "type": "lesson", "order": 1},
            {"title": "Photosynthesis and Respiration", "type": "lesson", "order": 2},
        ]
    },
    {
        "title": "Advanced Mathematics - Board Exam Prep",
        "description": "Complete preparation for CBSE board exams with all chapters.",
        "subject": "Math",
        "board": "CBSE",
        "grade_level": "9-10",
        "price": 599,
        "duration_hours": 30,
        "language": "en",
        "content": [
            {"title": "Polynomials", "type": "lesson", "order": 1},
            {"title": "Quadratic Equations", "type": "lesson", "order": 2},
        ]
    },
    {
        "title": "Math Olympiad Preparation",
        "description": "Train for national and international math olympiad competitions.",
        "subject": "Math",
        "board": "Olympiad",
        "grade_level": "9-10",
        "price": 799,
        "duration_hours": 40,
        "language": "en",
        "content": [
            {"title": "Number Theory", "type": "lesson", "order": 1},
            {"title": "Combinatorics", "type": "lesson", "order": 2},
        ]
    },
]

try:
    admin_user = User(
        email="admin@edulearn.com",
        password_hash=get_password_hash("Admin@123"),
        first_name="Admin",
        last_name="User",
        role=UserRole.ADMIN,
        preferred_language="en"
    )
    db.add(admin_user)
    db.commit()
    db.refresh(admin_user)
    print(f"✅ Admin user created: {admin_user.email}")

    teacher_user = User(
        email="teacher@edulearn.com",
        password_hash=get_password_hash("Teacher@123"),
        first_name="John",
        last_name="Educator",
        role=UserRole.TEACHER,
        preferred_language="en"
    )
    db.add(teacher_user)
    db.commit()
    db.refresh(teacher_user)
    print(f"✅ Teacher user created: {teacher_user.email}")

    sample_student = User(
        email="student@edulearn.com",
        password_hash=get_password_hash("Student@123"),
        first_name="Jane",
        last_name="Learner",
        role=UserRole.STUDENT,
        preferred_language="en",
        phone="9876543210"
    )
    db.add(sample_student)
    db.commit()
    print(f"✅ Sample student created: {sample_student.email}")

    for course_data in sample_courses:
        course = Course(
            teacher_id=teacher_user.id,
            title=course_data["title"],
            description=course_data["description"],
            subject=course_data["subject"],
            board=course_data["board"],
            grade_level=course_data["grade_level"],
            price=course_data["price"],
            duration_hours=course_data["duration_hours"],
            language=course_data["language"],
            status=CourseStatus.ACTIVE
        )
        db.add(course)
        db.commit()
        db.refresh(course)

        for content_data in course_data["content"]:
            content = CourseContent(
                course_id=course.id,
                title=content_data["title"],
                content_type=content_data["type"],
                order=content_data["order"],
                language="en"
            )
            db.add(content)

        if "Math" in course_data["subject"]:
            questions = [
                {
                    "question": "What is 2 + 2?",
                    "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
                    "answer": "B"
                },
                {
                    "question": "What is 5 × 3?",
                    "options": {"A": "15", "B": "12", "C": "20", "D": "18"},
                    "answer": "A"
                }
            ]
        else:
            questions = [
                {
                    "question": "Sample question 1?",
                    "options": {"A": "Option 1", "B": "Option 2", "C": "Option 3", "D": "Option 4"},
                    "answer": "A"
                }
            ]

        for q in questions:
            quiz_q = QuizQuestion(
                course_id=course.id,
                question_text=q["question"],
                options=q["options"],
                correct_answer=q["answer"],
                language="en"
            )
            db.add(quiz_q)

        db.commit()
        print(f"✅ Created course: {course.title}")

    print("\n✅ Database seeded successfully!")
    print(f"Total courses created: {len(sample_courses)}")
    print("\nSample Credentials:")
    print("Admin - email: admin@edulearn.com, password: Admin@123")
    print("Teacher - email: teacher@edulearn.com, password: Teacher@123")
    print("Student - email: student@edulearn.com, password: Student@123")

except Exception as e:
    print(f"❌ Error seeding database: {str(e)}")
    db.rollback()

finally:
    db.close()
