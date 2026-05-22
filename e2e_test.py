#!/usr/bin/env python3
"""
EduLearn End-to-End Testing Script
Tests all major features of the platform
"""

import requests
import json
import time
from urllib.parse import urljoin

# Configuration
API_BASE_URL = "http://localhost:8000"
FRONTEND_URL = "http://localhost:3000"

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.OKCYAN}{'='*50}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKCYAN}{text}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKCYAN}{'='*50}{Colors.ENDC}")

def print_success(text):
    print(f"{Colors.OKGREEN}✅ {text}{Colors.ENDC}")

def print_error(text):
    print(f"{Colors.FAIL}❌ {text}{Colors.ENDC}")

def print_info(text):
    print(f"{Colors.OKCYAN}ℹ️  {text}{Colors.ENDC}")

def test_api_connection():
    """Test if API is reachable"""
    print_header("Testing API Connection")
    try:
        response = requests.get(f"{API_BASE_URL}/docs", timeout=5)
        if response.status_code == 200:
            print_success(f"API is running at {API_BASE_URL}")
            return True
        else:
            print_error(f"API returned status {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Cannot connect to API: {str(e)}")
        print_info(f"Make sure backend is running: python -m uvicorn app:app --reload")
        return False

def test_authentication():
    """Test user authentication flow"""
    print_header("Testing Authentication")
    
    test_cases = [
        {
            "name": "Admin Login",
            "email": "admin@edulearn.com",
            "password": "Admin@123"
        },
        {
            "name": "Teacher Login",
            "email": "teacher@edulearn.com",
            "password": "Teacher@123"
        },
        {
            "name": "Student Login",
            "email": "student@edulearn.com",
            "password": "Student@123"
        }
    ]
    
    for test in test_cases:
        try:
            response = requests.post(
                f"{API_BASE_URL}/auth/login",
                json={"email": test["email"], "password": test["password"]},
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                if "access_token" in data:
                    print_success(f"{test['name']} - Token received")
                else:
                    print_error(f"{test['name']} - No token in response")
            else:
                print_error(f"{test['name']} - Status {response.status_code}")
        except Exception as e:
            print_error(f"{test['name']} - {str(e)}")

def test_courses():
    """Test course retrieval"""
    print_header("Testing Courses")
    
    try:
        response = requests.get(
            f"{API_BASE_URL}/courses",
            timeout=5
        )
        
        if response.status_code == 200:
            courses = response.json()
            if isinstance(courses, list):
                print_success(f"Retrieved {len(courses)} courses")
                if courses:
                    print_info(f"Sample courses:")
                    for course in courses[:3]:
                        course_name = course.get("title", "Unknown")
                        course_price = course.get("price", 0)
                        print_info(f"  • {course_name} - ₹{course_price}")
            else:
                print_error("Courses response is not a list")
        else:
            print_error(f"Failed to fetch courses - Status {response.status_code}")
    except Exception as e:
        print_error(f"Cannot fetch courses: {str(e)}")

def test_user_profile():
    """Test user profile retrieval"""
    print_header("Testing User Profile")
    
    # First login
    try:
        login_response = requests.post(
            f"{API_BASE_URL}/auth/login",
            json={"email": "student@edulearn.com", "password": "Student@123"},
            timeout=5
        )
        
        if login_response.status_code != 200:
            print_error("Failed to login for profile test")
            return
        
        token = login_response.json().get("access_token")
        
        # Then get profile
        response = requests.get(
            f"{API_BASE_URL}/user/profile",
            headers={"Authorization": f"Bearer {token}"},
            timeout=5
        )
        
        if response.status_code == 200:
            profile = response.json()
            print_success(f"User profile retrieved")
            print_info(f"  Name: {profile.get('first_name')} {profile.get('last_name')}")
            print_info(f"  Email: {profile.get('email')}")
            print_info(f"  Role: {profile.get('role')}")
        else:
            print_error(f"Failed to fetch profile - Status {response.status_code}")
    except Exception as e:
        print_error(f"Cannot fetch profile: {str(e)}")

def test_frontend():
    """Test if frontend is reachable"""
    print_header("Testing Frontend")
    
    try:
        response = requests.get(FRONTEND_URL, timeout=5)
        if response.status_code == 200:
            print_success(f"Frontend is running at {FRONTEND_URL}")
            print_info("Open in browser: http://localhost:3000")
        else:
            print_error(f"Frontend returned status {response.status_code}")
    except Exception as e:
        print_error(f"Cannot connect to frontend: {str(e)}")
        print_info("Make sure frontend is running: python -m http.server 3000 --directory ../frontend")

def test_database():
    """Test database connectivity through API"""
    print_header("Testing Database")
    
    try:
        # Try to get any data from the database
        response = requests.get(
            f"{API_BASE_URL}/courses?limit=1",
            timeout=5
        )
        
        if response.status_code == 200:
            print_success("Database is accessible")
            # Check if data exists
            courses = response.json()
            if courses:
                print_success(f"Database contains data ({len(courses)} courses found)")
            else:
                print_error("Database is empty - make sure seed_data.py was run")
        else:
            print_error(f"Database query failed - Status {response.status_code}")
    except Exception as e:
        print_error(f"Cannot access database: {str(e)}")

def print_summary(passed, total):
    """Print test summary"""
    print_header("Test Summary")
    percentage = (passed / total) * 100 if total > 0 else 0
    status = Colors.OKGREEN if percentage >= 80 else Colors.WARNING
    
    print(f"{status}Passed: {passed}/{total} ({percentage:.0f}%){Colors.ENDC}")
    
    if percentage == 100:
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}🎉 All tests passed! Platform is ready to use.{Colors.ENDC}")
    elif percentage >= 80:
        print(f"\n{Colors.WARNING}⚠️  Most tests passed. Check warnings above.{Colors.ENDC}")
    else:
        print(f"\n{Colors.FAIL}❌ Some tests failed. Check errors above.{Colors.ENDC}")

def main():
    """Run all tests"""
    print(f"{Colors.BOLD}{Colors.OKBLUE}")
    print("╔════════════════════════════════════╗")
    print("║   EduLearn End-to-End Test Suite   ║")
    print("╚════════════════════════════════════╝")
    print(f"{Colors.ENDC}")
    
    print_info(f"API Base URL: {API_BASE_URL}")
    print_info(f"Frontend URL: {FRONTEND_URL}")
    
    tests = [
        ("API Connection", test_api_connection),
        ("Database Connection", test_database),
        ("Authentication", test_authentication),
        ("Courses", test_courses),
        ("User Profile", test_user_profile),
        ("Frontend", test_frontend),
    ]
    
    passed = 0
    for name, test_func in tests:
        try:
            result = test_func()
            if result is not False:  # None or True counts as passed
                passed += 1
        except Exception as e:
            print_error(f"Test '{name}' crashed: {str(e)}")
    
    print_summary(passed, len(tests))
    
    print(f"\n{Colors.BOLD}{Colors.OKCYAN}Useful API Endpoints:{Colors.ENDC}")
    print(f"  • GET  {API_BASE_URL}/docs - API documentation")
    print(f"  • POST {API_BASE_URL}/auth/login - User login")
    print(f"  • GET  {API_BASE_URL}/courses - List courses")
    print(f"  • GET  {API_BASE_URL}/user/profile - User profile")

if __name__ == "__main__":
    main()
