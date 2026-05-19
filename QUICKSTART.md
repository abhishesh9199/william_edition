# Quick Start Guide

## Local Development (5 minutes)

### Prerequisites
- Python 3.9+
- Docker & Docker Compose
- Git

### Start Backend

```bash
# 1. Navigate to backend
cd william_edition/backend

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start PostgreSQL (from william_edition root)
docker-compose up -d

# 5. Start backend
python -m uvicorn app:app --reload

# Server running at http://localhost:8000
```

### Seed Database (Optional)

```bash
# From william_edition/backend directory
python seed_data.py
```

### Start Frontend

```bash
# From william_edition directory
python -m http.server 3000 --directory frontend

# Open browser: http://localhost:3000
```

## Test the Application

### 1. Register New User
- Visit `http://localhost:3000/auth.html`
- Fill in registration form
- Submit

### 2. Login
- Use registered email and password
- Get redirected to dashboard

### 3. Browse Courses
- Visit `http://localhost:3000/courses.html`
- View all available courses
- Filter by subject, board, grade

### 4. Enroll in Course
- Click "Enroll Now"
- Select payment method
- Complete checkout

### 5. Admin Panel
- Login with: `admin@edulearn.com` / `Admin@123`
- Visit `http://localhost:3000/admin/dashboard.html`
- Create, edit, delete courses
- View analytics

## Sample Credentials

| Role | Email | Password |
|------|-------|----------|
| Admin | admin@edulearn.com | Admin@123 |
| Teacher | teacher@edulearn.com | Teacher@123 |
| Student | student@edulearn.com | Student@123 |

## API Examples

### Register
```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "Password123",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

### Login
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "Password123"
  }'
```

### Get Courses
```bash
curl http://localhost:8000/courses
```

## File Structure

```
william_edition/
├── README.md                 # Project overview
├── DEPLOYMENT_GUIDE.md      # Deployment steps
├── QUICKSTART.md            # This file
├── docker-compose.yml       # Local DB setup
├── Procfile                 # Render deployment
├── backend/
│   ├── app.py              # Main FastAPI app
│   ├── requirements.txt     # Dependencies
│   ├── seed_data.py        # Database seeding
│   ├── database/           # Database models
│   ├── routes/             # API endpoints
│   ├── schemas/            # Data models
│   └── utils/              # Utilities
└── frontend/
    ├── index.html          # Home page
    ├── auth.html           # Login/Register
    ├── courses.html        # Course listing
    ├── dashboard.html      # Student dashboard
    ├── checkout.html       # Payment
    ├── admin/              # Admin panel
    ├── css/                # Stylesheets
    ├── js/                 # JavaScript
    └── assets/             # Images, icons
```

## Common Issues

### Database Connection Error
```
Solution: Ensure docker-compose is running
docker ps  # Check if postgres is running
```

### Port Already in Use
```
Solution: Use different port
python -m http.server 3001 --directory frontend
```

### CORS Error
```
Solution: Already configured in FastAPI
Check backend/app.py CORS settings
```

### Module Not Found
```
Solution: Reinstall dependencies
pip install -r requirements.txt
```

## Next Steps

1. ✅ **Local Testing** - Complete
2. ✅ **Sample Data** - Seeded
3. ⏳ **Deployment** - See DEPLOYMENT_GUIDE.md
4. ⏳ **Production** - Follow Render steps
5. ⏳ **Content** - Add your courses

## Support

- Check README.md for features
- Review API endpoints in backend/routes/
- Test with Postman or curl
- Check browser console for frontend errors

---

**Start building and learning! 🚀**
