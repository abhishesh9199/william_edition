# EduLearn Database Setup Script
# Run this script after Docker Desktop is installed and running

Write-Host "================================" -ForegroundColor Cyan
Write-Host "EduLearn Database Setup" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Check Docker
Write-Host "[1/4] Checking Docker installation..." -ForegroundColor Yellow
try {
    $dockerVersion = docker --version
    Write-Host "✅ Docker found: $dockerVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Docker not found. Please install Docker Desktop first." -ForegroundColor Red
    Write-Host "   Download: https://www.docker.com/products/docker-desktop" -ForegroundColor Yellow
    exit 1
}

# Step 2: Start PostgreSQL
Write-Host "`n[2/4] Starting PostgreSQL container..." -ForegroundColor Yellow
try {
    cd "c:\Users\ASUS\Desktop\william_edition"
    docker compose up -d
    Write-Host "✅ PostgreSQL container started" -ForegroundColor Green
    Write-Host "⏳ Waiting for PostgreSQL to be ready (30 seconds)..." -ForegroundColor Yellow
    Start-Sleep -Seconds 30
} catch {
    Write-Host "❌ Failed to start PostgreSQL: $_" -ForegroundColor Red
    exit 1
}

# Step 3: Verify connection
Write-Host "`n[3/4] Verifying PostgreSQL connection..." -ForegroundColor Yellow
try {
    $containerStatus = docker ps --filter "name=william_edition-db" --format "{{.Status}}"
    if ($containerStatus -like "*Up*") {
        Write-Host "✅ PostgreSQL is running" -ForegroundColor Green
    } else {
        Write-Host "❌ PostgreSQL container is not running" -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "❌ Failed to verify PostgreSQL: $_" -ForegroundColor Red
    exit 1
}

# Step 4: Seed database
Write-Host "`n[4/4] Seeding database..." -ForegroundColor Yellow
try {
    cd "c:\Users\ASUS\Desktop\william_edition\backend"
    .\venv\Scripts\activate.ps1
    python seed_data.py
    Write-Host "" -ForegroundColor Green
    Write-Host "================================" -ForegroundColor Green
    Write-Host "✅ Setup Complete!" -ForegroundColor Green
    Write-Host "================================" -ForegroundColor Green
    Write-Host "" -ForegroundColor Green
    Write-Host "Sample Credentials:" -ForegroundColor Cyan
    Write-Host "  Admin  : admin@edulearn.com / Admin@123" -ForegroundColor White
    Write-Host "  Teacher: teacher@edulearn.com / Teacher@123" -ForegroundColor White
    Write-Host "  Student: student@edulearn.com / Student@123" -ForegroundColor White
    Write-Host "" -ForegroundColor Green
    Write-Host "Next Steps:" -ForegroundColor Cyan
    Write-Host "  1. Start backend: python -m uvicorn app:app --reload" -ForegroundColor White
    Write-Host "  2. Start frontend: python -m http.server 3000 --directory ../frontend" -ForegroundColor White
    Write-Host "  3. Open browser: http://localhost:3000" -ForegroundColor White
} catch {
    Write-Host "❌ Failed to seed database: $_" -ForegroundColor Red
    exit 1
}
