# EduLearn - Visual Setup Guide

## Current Status

```
✅ Steps 1-3: COMPLETED
   ├─ Multi-language support ✅
   ├─ User authentication ✅
   ├─ Course management ✅
   ├─ Student dashboard ✅
   ├─ Payment integration ✅
   ├─ Admin panel ✅
   └─ Quiz system ✅

⏳ Step 4: START POSTGRESQL (Pending Docker)
   └─ docker compose up -d

⏳ Step 5: SEED DATABASE (Depends on Step 4)
   └─ python seed_data.py

⏳ Step 6: RUN SERVERS (After Steps 4-5)
   ├─ Backend: python -m uvicorn app:app --reload
   ├─ Frontend: python -m http.server 3000
   └─ Tests: python e2e_test.py
```

---

## Installation Timeline

```
┌─────────────────────────────────────────────────────────────────┐
│                     EduLearn Setup Process                       │
└─────────────────────────────────────────────────────────────────┘

STEP 0: Install Docker Desktop
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🔗 Download: https://www.docker.com/products/docker-desktop
  ⏱  Time: 10-15 minutes
  ✓  Result: docker command available
  
  └─→ [5 min] Download installer
      └─→ [5 min] Run installer  
          └─→ [5 min] Restart computer
              └─→ [Verify] docker --version


STEP 1: Start PostgreSQL Container
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🐘 Command: docker compose up -d
  ⏱  Time: 2-5 minutes (first time with image download)
  ✓  Result: PostgreSQL running on localhost:5432
  
  └─→ [1 min] Pull PostgreSQL image (first time only)
      └─→ [30 sec] Create container
          └─→ [30 sec] Start database
              └─→ [Wait] PostgreSQL initialization
                  └─→ [✓] Ready at localhost:5432


STEP 2: Seed Database
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🌱 Command: python seed_data.py
  ⏱  Time: 1-2 minutes
  ✓  Result: Database populated with sample data
  
  └─→ [10 sec] Create tables
      └─→ [20 sec] Create users
          └─→ [1 min] Create 10 courses
              └─→ [30 sec] Add quizzes
                  └─→ [✓] Database ready


STEP 3: Start Backend Server
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🚀 Command: python -m uvicorn app:app --reload
  ⏱  Time: 1 minute
  ✓  Result: API running on localhost:8000
  
  └─→ [30 sec] Load FastAPI app
      └─→ [30 sec] Initialize database connection
          └─→ [✓] API ready


STEP 4: Start Frontend Server
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🎨 Command: python -m http.server 3000 --directory frontend
  ⏱  Time: 10 seconds
  ✓  Result: Frontend running on localhost:3000
  
  └─→ [10 sec] Start HTTP server
      └─→ [✓] Frontend ready


STEP 5: Run End-to-End Tests
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🧪 Command: python e2e_test.py
  ⏱  Time: 1-2 minutes
  ✓  Result: All systems validated
  
  └─→ [Test] API connectivity
      └─→ [Test] Database connection
          └─→ [Test] Authentication
              └─→ [Test] Courses
                  └─→ [Test] User profile
                      └─→ [✓] All systems working

═══════════════════════════════════════════════════════════════════
✨ READY FOR LIVE TESTING ✨
═══════════════════════════════════════════════════════════════════

📍 Access Points:
   Frontend: http://localhost:3000
   API:      http://localhost:8000
   Docs:     http://localhost:8000/docs
```

---

## Five-Terminal Setup

```
╔════════════════════════════════════════════════════════════════════╗
║                   OPEN 5 POWERSHELL TERMINALS                       ║
╚════════════════════════════════════════════════════════════════════╝

┌─ TERMINAL 1: PostgreSQL Container ────────────────────────────────┐
│                                                                     │
│ $ docker compose up -d                                             │
│                                                                     │
│ Output:                                                            │
│ ✓ Network william_edition_default  Created                         │
│ ✓ Container william_edition-db-1   Started                         │
│                                                                     │
│ ⏳ Wait 30 seconds                                                  │
│ 🟢 Status: Running                                                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘


┌─ TERMINAL 2: Database Seeding ────────────────────────────────────┐
│                                                                     │
│ $ cd backend                                                       │
│ $ .\venv\Scripts\activate.ps1                                      │
│ $ python seed_data.py                                              │
│                                                                     │
│ Output:                                                            │
│ ✅ Admin user created: admin@edulearn.com                          │
│ ✅ Sample student created: student@edulearn.com                    │
│ ✅ Created course: Math Basics for Grade 3-5                       │
│ ... (10 courses total)                                             │
│ ✅ Database seeded successfully!                                   │
│                                                                     │
│ 🟢 Status: Complete                                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘


┌─ TERMINAL 3: Backend API Server ────────────────────────────────┐
│                                                                     │
│ $ cd backend                                                       │
│ $ .\venv\Scripts\activate.ps1                                      │
│ $ python -m uvicorn app:app --reload --host 0.0.0.0               │
│                                                                     │
│ Output:                                                            │
│ INFO:     Started server process [12345]                          │
│ INFO:     Uvicorn running on http://0.0.0.0:8000                  │
│ INFO:     Application startup complete                            │
│                                                                     │
│ 🟢 Status: Running                                                 │
│ 📍 API URL: http://localhost:8000                                  │
│ 📍 Docs: http://localhost:8000/docs                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘


┌─ TERMINAL 4: Frontend Server ─────────────────────────────────────┐
│                                                                     │
│ $ cd william_edition                                               │
│ $ python -m http.server 3000 --directory frontend                  │
│                                                                     │
│ Output:                                                            │
│ Serving HTTP on 0.0.0.0 port 3000 (http://0.0.0.0:3000/) ...     │
│                                                                     │
│ 🟢 Status: Running                                                 │
│ 📍 Frontend URL: http://localhost:3000                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘


┌─ TERMINAL 5: End-to-End Tests ────────────────────────────────────┐
│                                                                     │
│ $ cd william_edition                                               │
│ $ python e2e_test.py                                               │
│                                                                     │
│ Output:                                                            │
│ ════════════════════════════════════════                           │
│ EduLearn End-to-End Test Suite                                    │
│ ════════════════════════════════════════                           │
│                                                                     │
│ [1/6] Testing API Connection                                       │
│ ✅ API is running at http://localhost:8000                         │
│                                                                     │
│ [2/6] Testing Database Connection                                  │
│ ✅ Retrieved 10 courses                                            │
│                                                                     │
│ [3/6] Testing Authentication                                       │
│ ✅ Admin Login - Token received                                    │
│ ✅ Teacher Login - Token received                                  │
│ ✅ Student Login - Token received                                  │
│                                                                     │
│ [4/6] Testing Courses                                              │
│ ✅ Retrieved 10 courses                                            │
│                                                                     │
│ [5/6] Testing User Profile                                         │
│ ✅ User profile retrieved                                          │
│                                                                     │
│ [6/6] Testing Frontend                                             │
│ ✅ Frontend is running at http://localhost:3000                    │
│                                                                     │
│ ════════════════════════════════════════                           │
│ ✅ All tests passed! Platform is ready to use.                     │
│ ════════════════════════════════════════                           │
│                                                                     │
│ 🟢 Status: All Systems GO! ✅                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════
🎉 COMPLETE - READY FOR TESTING 🎉
═══════════════════════════════════════════════════════════════════════
```

---

## Sample Credentials for Testing

```
┌─ ADMIN ACCOUNT ────────────────────────────┐
│ Email:    admin@edulearn.com                │
│ Password: Admin@123                        │
│ Access:   Full system access                │
└────────────────────────────────────────────┘

┌─ TEACHER ACCOUNT ──────────────────────────┐
│ Email:    teacher@edulearn.com              │
│ Password: Teacher@123                      │
│ Access:   Create & manage courses           │
└────────────────────────────────────────────┘

┌─ STUDENT ACCOUNT ──────────────────────────┐
│ Email:    student@edulearn.com              │
│ Password: Student@123                      │
│ Access:   Enroll & take courses             │
└────────────────────────────────────────────┘
```

---

## What to Test

```
✅ FEATURE CHECKLIST

Authentication
  ☐ Admin login
  ☐ Teacher login
  ☐ Student login
  ☐ Token generation
  ☐ Profile access

Courses
  ☐ View all courses (should show 10)
  ☐ View course details
  ☐ Filter by subject
  ☐ Filter by grade level
  ☐ Filter by board

Student Features
  ☐ Dashboard displays courses
  ☐ Can view course content
  ☐ Can take quizzes
  ☐ Quiz scoring works
  ☐ Progress tracking

Teacher Features
  ☐ Can view teacher dashboard
  ☐ Can see created courses
  ☐ Can view student enrollments

Admin Features
  ☐ Admin dashboard loads
  ☐ Can manage users
  ☐ Can manage courses
  ☐ Can view analytics

API
  ☐ API docs available at /docs
  ☐ All endpoints documented
  ☐ CORS enabled
  ☐ Error handling works

Frontend
  ☐ Responsive design
  ☐ Mobile view works
  ☐ Desktop view works
  ☐ Navigation works
```

---

## Access Points After Setup

```
┌───────────────────────────────────────────────────────┐
│              WHAT TO OPEN IN BROWSER                  │
└───────────────────────────────────────────────────────┘

1. Main Application
   🌐 http://localhost:3000
   👉 Start here - frontend entry point

2. API Documentation
   📚 http://localhost:8000/docs
   👉 Explore and test API endpoints

3. API Health
   ❤️  http://localhost:8000/health
   👉 Check if backend is running

4. Courses API
   📖 http://localhost:8000/courses
   👉 View courses as JSON
```

---

## Automated Setup Option

```
If you prefer one-command setup:

┌─ RUN THIS SINGLE COMMAND ──────────────────────────┐
│                                                     │
│ $ .\setup_database.ps1                             │
│                                                     │
│ This will automatically:                           │
│ 1. Check Docker installation                       │
│ 2. Start PostgreSQL container                      │
│ 3. Seed database                                   │
│ 4. Display sample credentials                      │
│ 5. Show next steps                                 │
│                                                     │
│ ⏱  Total time: 5-10 minutes                        │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## Troubleshooting Quick Guide

```
Problem: "docker: command not found"
Solution: 
  1. Install Docker Desktop
  2. Restart PowerShell
  3. Verify: docker --version

Problem: "Cannot connect to PostgreSQL"
Solution:
  1. Check if Docker is running
  2. Check container status: docker ps
  3. Wait 30 seconds (startup time)
  4. Check logs: docker logs william_edition-db-1

Problem: "API returns 500 error"
Solution:
  1. Ensure PostgreSQL is running
  2. Check backend console for errors
  3. Verify DATABASE_URL in .env
  4. Restart backend server

Problem: "Frontend not loading"
Solution:
  1. Check if frontend server is running
  2. Verify port 3000 is available
  3. Check for 404 errors in browser console
  4. Restart frontend server

See DOCKER_SETUP_GUIDE.md or SETUP_INSTRUCTIONS.md for more details
```

---

## Time Estimate

```
Activity                    Time
────────────────────────────────
Install Docker Desktop      10-15 min
Download PostgreSQL image    2-5 min  (only first time)
Start PostgreSQL container   1 min
Seed database               1-2 min
Start backend server         1 min
Start frontend server       30 sec
Run tests                   1-2 min
────────────────────────────────
TOTAL                       16-25 min
```

---

**Status**: ✅ All code ready | ⏳ Awaiting Docker for steps 4-5 | 🎯 Ready to test
