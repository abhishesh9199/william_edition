# EduLearn - Educational Platform

A comprehensive online learning platform for students (LKG-12th grade) with support for CBSE, ICSE, State Boards, and Olympiad preparation.

## Features

✅ **Multi-language Support** - English & Hindi
✅ **User Authentication** - Secure JWT-based authentication
✅ **Course Management** - Teachers can create and manage courses
✅ **Student Dashboard** - Track progress and enrolled courses
✅ **Payment Integration** - Razorpay payment gateway
✅ **Admin Panel** - Manage courses, students, and analytics
✅ **Quiz System** - Interactive quizzes with instant feedback
✅ **Responsive Design** - Works on all devices

## Tech Stack

**Backend:**
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- JWT Authentication
- Razorpay Payment Gateway

**Frontend:**
- HTML5
- CSS3
- Vanilla JavaScript
- Responsive Design

**Hosting:**
- Render (Backend & Frontend)
- PostgreSQL Database

## Project Structure

```
william_edition/
├── backend/              # FastAPI application
│   ├── app.py
│   ├── requirements.txt
│   ├── database/        # Database models & connection
│   ├── routes/          # API endpoints
│   ├── schemas/         # Pydantic models
│   └── utils/           # Utilities (security, mail)
├── frontend/            # Frontend HTML/CSS/JS
│   ├── index.html       # Home page
│   ├── auth.html        # Login/Register
│   ├── courses.html     # Course listing
│   ├── dashboard.html   # Student dashboard
│   ├── checkout.html    # Payment checkout
│   ├── admin/           # Admin panel
│   ├── css/
│   ├── js/
│   └── assets/
├── docker-compose.yml   # Local PostgreSQL
├── Procfile             # Render deployment
└── README.md
```

## Setup Instructions

### Local Development

1. **Clone/Setup Project**
```bash
cd william_edition
```

2. **Setup Backend**
```bash
cd backend
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
```

3. **Create .env file**
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. **Start PostgreSQL (using Docker)**
```bash
docker-compose up -d
```

5. **Create Database & Seed Data**
```bash
python seed_data.py
```

6. **Run Backend Server**
```bash
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

7. **Serve Frontend**
```bash
# Use any local server or open frontend/index.html directly
python -m http.server 3000 --directory ../frontend
```

## API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `POST /auth/refresh` - Refresh access token
- `POST /auth/logout` - Logout user

### Courses
- `GET /courses` - List all courses
- `GET /courses/{id}` - Get course details
- `POST /courses` - Create course (teacher/admin)
- `PUT /courses/{id}` - Update course
- `DELETE /courses/{id}` - Delete course
- `GET /courses/{id}/content` - Get course content
- `POST /courses/{id}/content` - Add course content

### User
- `GET /user/profile` - Get user profile
- `PUT /user/profile` - Update profile
- `GET /user/enrollments` - Get enrolled courses

### Payments
- `POST /payment/create-order` - Create Razorpay order
- `POST /payment/verify` - Verify payment
- `POST /payment/webhook` - Payment webhook

## Database Schema

### Users
- User roles: student, teacher, admin
- JWT token support
- Multi-language preference

### Courses
- Subject, Board, Grade Level filters
- Multiple language support
- Teacher ownership

### Enrollments
- Track student progress
- Payment integration
- Status tracking

### Payments
- Razorpay integration
- Transaction history
- Status tracking

### Quiz System
- Multiple choice questions
- Difficulty levels
- Student responses tracking

## Environment Variables

```
DATABASE_URL=postgresql://user:password@localhost/education_db
SECRET_KEY=your-secret-key-for-jwt
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
RAZORPAY_KEY_ID=rzp_test_xxxx
RAZORPAY_KEY_SECRET=your_secret_key
FRONTEND_URL=http://localhost:3000
API_URL=http://localhost:8000
```

## Sample Credentials

After seeding:
- **Admin**: admin@edulearn.com / Admin@123
- **Teacher**: teacher@edulearn.com / Teacher@123
- **Student**: student@edulearn.com / Student@123

## Deployment to Render

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Create Render Services**
   - Create PostgreSQL database
   - Create Web Service (Python)
   - Set environment variables

3. **Configure .env**
   - Update DATABASE_URL with Render PostgreSQL URL
   - Add Razorpay keys
   - Update FRONTEND_URL to Render URL

4. **Deploy**
```bash
git push  # Automatically triggers deploy
```

## Features Roadmap

- [ ] AI-powered learning recommendations
- [ ] Video streaming integration
- [ ] Certificate generation
- [ ] Discussion forums
- [ ] Live classes support
- [ ] Progress analytics dashboard
- [ ] Mobile app (React Native)
- [ ] More language support

## Security

- Password hashing with bcrypt
- JWT authentication
- CORS protection
- SQL injection prevention
- XSS protection
- HTTPS enforcement (on Render)

## Performance

- Pagination support
- Database indexing
- Caching strategy
- Optimized queries
- CDN-ready static files

## Support

For issues or questions:
1. Check documentation
2. Review API endpoints
3. Check sample credentials
4. Review error logs

## License

MIT License - Feel free to use for educational purposes

## Contributing

This is an educational platform. Contributions welcome!

---

**Built with ❤️ for learners everywhere**
