# EduLearn - Complete Setup Instructions

## Current Status
✅ All requirements implemented
⏳ Steps 4 & 5: Database setup pending (requires Docker)

---

## Step 4: Start PostgreSQL (Using Docker)

### Prerequisites
- **Docker Desktop** must be installed
- Download from: https://www.docker.com/products/docker-desktop

### Installation Steps

#### Option A: Quick Setup (Automated)
1. Install Docker Desktop and restart your system
2. Open PowerShell and run:
```bash
cd c:\Users\ASUS\Desktop\william_edition
.\setup_database.ps1
```

#### Option B: Manual Setup
1. Ensure Docker Desktop is running (check system tray)
2. Open PowerShell and navigate to project root:
```bash
cd c:\Users\ASUS\Desktop\william_edition
```

3. Start PostgreSQL container:
```bash
docker compose up -d
```

Expected output:
```
[+] Building 0.0s (0/0)
[+] Running 2/2
 ✓ Network william_edition_default  Created
 ✓ Container william_edition-db-1   Started
```

4. Verify PostgreSQL is running:
```bash
docker ps
```

You should see a container with status `Up`:
```
CONTAINER ID   IMAGE              STATUS          PORTS
abc123def456   postgres:15        Up 2 minutes    0.0.0.0:5432->5432/tcp
```

---

## Step 5: Create Database & Seed Data

### Run Seeding Script

Open PowerShell and run:
```bash
cd c:\Users\ASUS\Desktop\william_edition\backend
.\venv\Scripts\activate.ps1
python seed_data.py
```

### Expected Output

```
✅ Admin user created: admin@edulearn.com
✅ Teacher user created: teacher@edulearn.com
✅ Sample student created: student@edulearn.com
✅ Created course: Math Basics for Grade 3-5
✅ Created course: English Language Fundamentals
✅ Created course: Science Fundamentals
✅ Created course: Social Studies - Our World
✅ Created course: Algebra for Grade 6-8
✅ Created course: Physics Essentials
✅ Created course: Chemistry Made Simple
✅ Created course: Biology for Grade 9-10
✅ Created course: Advanced Mathematics - Board Exam Prep
✅ Created course: Math Olympiad Preparation

✅ Database seeded successfully!
Total courses created: 10

Sample Credentials:
Admin - email: admin@edulearn.com, password: Admin@123
Teacher - email: teacher@edulearn.com, password: Teacher@123
Student - email: student@edulearn.com, password: Student@123
```

---

## Step 6: Run Backend Server

Open PowerShell:
```bash
cd c:\Users\ASUS\Desktop\william_edition\backend
.\venv\Scripts\activate.ps1
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Expected output:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

Access API documentation: http://localhost:8000/docs

---

## Step 7: Run Frontend Server

Open a new PowerShell terminal:
```bash
cd c:\Users\ASUS\Desktop\william_edition
python -m http.server 3000 --directory frontend
```

Expected output:
```
Serving HTTP on 0.0.0.0 port 3000 (http://0.0.0.0:3000/) ...
```

---

## Step 8: End-to-End Testing

With both backend and frontend running, open a new PowerShell and run:
```bash
cd c:\Users\ASUS\Desktop\william_edition
python e2e_test.py
```

This will test:
- ✅ API connectivity
- ✅ Database connectivity
- ✅ User authentication (Admin, Teacher, Student)
- ✅ Course retrieval
- ✅ User profile retrieval
- ✅ Frontend connectivity

---

## Testing the Platform

### Access Points
- **Frontend**: http://localhost:3000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### Sample Credentials

#### Admin
- Email: `admin@edulearn.com`
- Password: `Admin@123`

#### Teacher
- Email: `teacher@edulearn.com`
- Password: `Teacher@123`

#### Student
- Email: `student@edulearn.com`
- Password: `Student@123`

---

## Available Features to Test

### 1. Authentication
- Login with different user roles
- Token validation
- Logout functionality

### 2. Courses
- View all courses (10 courses pre-loaded)
- Filter by subject, board, grade level
- View course details
- View course content

### 3. Student Dashboard
- View enrolled courses
- Track progress
- Access course materials

### 4. Admin Panel
- Manage users
- Manage courses
- View analytics

### 5. Quiz System
- Take quizzes
- Instant feedback
- Score tracking

---

## Troubleshooting

### Docker Issues

**Problem**: `docker: command not found`
- **Solution**: Restart PowerShell after Docker installation
- Ensure Docker is in PATH

**Problem**: `Cannot connect to Docker daemon`
- **Solution**: Start Docker Desktop
- Wait for it to fully load

**Problem**: Port 5432 already in use
- **Solution**: Edit `docker-compose.yml`:
```yaml
ports:
  - "5433:5432"  # Changed port
```
- Update `DATABASE_URL` in `.env`:
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5433/education_db
```

### Database Issues

**Problem**: `connection refused` when seeding
- **Solution**: 
  - Ensure PostgreSQL container is running: `docker ps`
  - Wait 30 seconds for PostgreSQL to fully start
  - Check logs: `docker logs william_edition-db-1`

**Problem**: `ModuleNotFoundError: No module named 'psycopg2'`
- **Solution**:
```bash
cd backend
.\venv\Scripts\activate.ps1
pip install psycopg[binary]
```

### API Issues

**Problem**: Cannot connect to API
- **Solution**: 
  - Ensure backend is running
  - Check port 8000 is not blocked
  - Run: `python -m uvicorn app:app --reload`

**Problem**: 401 Unauthorized on protected endpoints
- **Solution**:
  - Ensure you have valid JWT token
  - Login first to get token
  - Include in header: `Authorization: Bearer <token>`

---

## Project Structure

```
william_edition/
├── backend/
│   ├── app.py                 # Main FastAPI app
│   ├── requirements.txt        # Python dependencies
│   ├── .env                   # Environment variables
│   ├── seed_data.py           # Database seeding script
│   ├── database/
│   │   ├── db.py             # Database configuration
│   │   └── models.py         # SQLAlchemy models
│   ├── routes/
│   │   ├── auth.py           # Authentication endpoints
│   │   ├── courses.py        # Course endpoints
│   │   ├── payments.py       # Payment endpoints
│   │   └── users.py          # User endpoints
│   ├── schemas/
│   │   └── *.py              # Pydantic models
│   └── utils/
│       ├── security.py       # JWT & password hashing
│       └── mail.py           # Email utilities
├── frontend/
│   ├── index.html            # Home page
│   ├── auth.html             # Login/Register
│   ├── courses.html          # Course listing
│   ├── dashboard.html        # Student dashboard
│   ├── checkout.html         # Payment checkout
│   ├── admin/                # Admin pages
│   ├── css/                  # Stylesheets
│   ├── js/                   # JavaScript
│   └── assets/               # Images & resources
├── docker-compose.yml         # PostgreSQL container config
├── setup_database.ps1         # Automated setup script
├── e2e_test.py               # End-to-end tests
└── README.md                 # Project documentation
```

---

## Next Steps After Setup

1. ✅ Customize the platform:
   - Add more courses
   - Customize frontend design
   - Integrate your payment gateway keys

2. 🚀 Deploy to production:
   - Follow DEPLOYMENT_GUIDE.md
   - Deploy to Render
   - Set up CI/CD pipeline

3. 📊 Monitor & maintain:
   - Check API logs
   - Monitor database performance
   - Update dependencies regularly

---

## Support & Documentation

- **API Documentation**: http://localhost:8000/docs (Swagger UI)
- **README**: See README.md for full documentation
- **Deployment Guide**: See DEPLOYMENT_GUIDE.md
- **Docker Setup**: See DOCKER_SETUP_GUIDE.md

---

**Last Updated**: May 21, 2026
**Status**: ✅ Ready for testing once Docker is installed
