# Quick Reference - EduLearn Setup

## Prerequisites Check
```bash
# Check if Docker is installed
docker --version

# Check if Python venv is ready
cd c:\Users\ASUS\Desktop\william_edition\backend
.\venv\Scripts\activate.ps1
```

## Quick Start (After Docker Install)

### Terminal 1: Start Database
```bash
cd c:\Users\ASUS\Desktop\william_edition
docker compose up -d
# Wait 30 seconds for PostgreSQL to start
```

### Terminal 2: Seed Database
```bash
cd c:\Users\ASUS\Desktop\william_edition\backend
.\venv\Scripts\activate.ps1
python seed_data.py
```

### Terminal 3: Start Backend
```bash
cd c:\Users\ASUS\Desktop\william_edition\backend
.\venv\Scripts\activate.ps1
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### Terminal 4: Start Frontend
```bash
cd c:\Users\ASUS\Desktop\william_edition
python -m http.server 3000 --directory frontend
```

### Terminal 5: Run Tests
```bash
cd c:\Users\ASUS\Desktop\william_edition
python e2e_test.py
```

---

## Access Points

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| API Docs | http://localhost:8000/docs |
| Backend API | http://localhost:8000 |

---

## Sample Credentials

| Role | Email | Password |
|------|-------|----------|
| Admin | admin@edulearn.com | Admin@123 |
| Teacher | teacher@edulearn.com | Teacher@123 |
| Student | student@edulearn.com | Student@123 |

---

## Useful Docker Commands

```bash
# Check if containers are running
docker ps

# View container logs
docker logs william_edition-db-1

# Stop containers
docker compose down

# Stop and remove data
docker compose down -v

# Restart PostgreSQL
docker compose restart

# Check container stats
docker stats
```

---

## Database Connection Info

```
Host: localhost
Port: 5432
User: postgres
Password: postgres
Database: education_db
```

---

## If Something Goes Wrong

### Database won't connect
```bash
# 1. Check if Docker is running
docker ps

# 2. Check container logs
docker logs william_edition-db-1

# 3. Wait 30 seconds and try again (PostgreSQL startup time)

# 4. Restart if needed
docker compose restart
```

### Can't connect to API
```bash
# 1. Check if backend is running on correct port
netstat -ano | findstr :8000

# 2. Check if port is free (if not, kill the process)
# 3. Restart backend server
```

### Database seeding failed
```bash
# 1. Ensure PostgreSQL is running
docker ps

# 2. Manually connect to verify
psql postgresql://postgres:postgres@localhost/education_db

# 3. Check .env file for correct DATABASE_URL

# 4. Try seeding again
python seed_data.py
```

---

## Files Created/Modified

- ✅ `DOCKER_SETUP_GUIDE.md` - Detailed Docker setup
- ✅ `SETUP_INSTRUCTIONS.md` - Complete setup guide
- ✅ `setup_database.ps1` - Automated setup script
- ✅ `e2e_test.py` - End-to-end test suite
- ✅ `QUICK_REFERENCE.md` - This file

---

## Next: Manual Steps Required

1. **Install Docker Desktop**
   - Download: https://www.docker.com/products/docker-desktop
   - Restart your system after installation

2. **Run the Quick Start commands above** (or use `setup_database.ps1`)

3. **Test the platform** using `e2e_test.py`

---

**Status**: ⏳ Awaiting Docker installation to proceed with steps 4-5
