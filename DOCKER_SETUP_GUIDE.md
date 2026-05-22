# Docker Setup Guide for EduLearn

## Prerequisites
Your system doesn't currently have Docker installed. Follow these steps:

### Step 1: Install Docker Desktop
1. Download Docker Desktop from: https://www.docker.com/products/docker-desktop
2. Run the installer and follow the on-screen instructions
3. Restart your computer after installation
4. Verify installation by opening PowerShell and running:
   ```bash
   docker --version
   docker compose version
   ```

### Step 2: Enable Docker Daemon
1. After installation, start Docker Desktop (it should auto-start)
2. Wait for it to fully load (you'll see the Docker icon in system tray)

### Step 3: Start PostgreSQL Container
Once Docker is running and verified, execute:
```bash
cd c:\Users\ASUS\Desktop\william_edition
docker compose up -d
```

You should see output like:
```
[+] Building ...
[+] Running 2/2
 ✓ Network william_edition_default  Created
 ✓ Container william_edition-db-1   Started
```

### Step 4: Verify PostgreSQL is Running
Check container status:
```bash
docker ps
```

You should see a container named `william_edition-db-1` or similar with status `Up`.

### Step 5: Seed the Database
Once PostgreSQL is running:
```bash
cd c:\Users\ASUS\Desktop\william_edition\backend
.\venv\Scripts\activate.ps1
python seed_data.py
```

Expected output:
```
✅ Admin user created: admin@edulearn.com
✅ Teacher user created: teacher@edulearn.com
✅ Sample student created: student@edulearn.com
✅ Created course: Math Basics for Grade 3-5
...
✅ Database seeded successfully!
Total courses created: 10

Sample Credentials:
Admin - email: admin@edulearn.com, password: Admin@123
Teacher - email: teacher@edulearn.com, password: Teacher@123
Student - email: student@edulearn.com, password: Student@123
```

## Troubleshooting

### Docker command not found
- Restart PowerShell after Docker installation
- Add Docker to PATH if needed

### PostgreSQL connection refused
- Ensure Docker Desktop is running
- Wait 30 seconds for PostgreSQL to fully start
- Check logs: `docker logs william_edition-db-1`

### Port 5432 already in use
Edit `docker-compose.yml` and change port mapping:
```yaml
ports:
  - "5433:5432"  # Changed from 5432:5432
```
Then update DATABASE_URL in `.env`:
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5433/education_db
```

## Next Steps
After successful setup, run the backend server:
```bash
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

And frontend (in another terminal):
```bash
python -m http.server 3000 --directory ../frontend
```

Then test at: http://localhost:3000
