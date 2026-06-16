from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from database.db import engine
from database.models import Base
from routes import auth, user, courses

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Educational Platform API",
    description="API for students and teachers",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(courses.router)

# Serve frontend
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")

@app.get("/")
def serve_index():
    return FileResponse(os.path.join(frontend_path, "index.html"))

@app.get("/auth")
def serve_auth():
    return FileResponse(os.path.join(frontend_path, "auth.html"))

@app.get("/courses")
def serve_courses():
    return FileResponse(os.path.join(frontend_path, "courses.html"))

@app.get("/dashboard")
def serve_dashboard():
    return FileResponse(os.path.join(frontend_path, "dashboard.html"))

@app.get("/checkout")
def serve_checkout():
    return FileResponse(os.path.join(frontend_path, "checkout.html"))

# MUST be last
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)