# Deployment Guide for EduLearn on Render

## Step-by-Step Deployment to Render

### 1. Prepare Your Repository

```bash
cd william_edition
git init
git add .
git commit -m "Initial EduLearn educational platform"
git remote add origin https://github.com/YOUR_USERNAME/edulearn.git
git push -u origin main
```

### 2. Create PostgreSQL Database on Render

1. Go to https://render.com
2. Click "New +" → "PostgreSQL"
3. Fill in:
   - Name: `edulearn-db`
   - Database: `education_db`
   - User: `education_user`
4. Create database
5. Copy the **Internal Database URL** (save this)

### 3. Create Web Service for Backend

1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Fill in:
   - Name: `edulearn-api`
   - Environment: `Python 3`
   - Build Command: `pip install -r backend/requirements.txt`
   - Start Command: `cd backend && uvicorn app:app --host 0.0.0.0 --port $PORT`
4. Add Environment Variables:

```
DATABASE_URL=<paste your Internal Database URL>
SECRET_KEY=<generate a secure random string>
RAZORPAY_KEY_ID=<your Razorpay Key ID>
RAZORPAY_KEY_SECRET=<your Razorpay Secret Key>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
API_URL=https://<your-backend-url>.onrender.com
FRONTEND_URL=https://<your-frontend-url>.onrender.com
```

5. Create service
6. Copy the service URL (e.g., `https://edulearn-api.onrender.com`)

### 4. Create Static Site for Frontend

1. Click "New +" → "Static Site"
2. Connect your GitHub repository
3. Fill in:
   - Name: `edulearn-web`
   - Build Command: `echo "No build needed"`
   - Publish directory: `frontend`
4. Add Environment Variable in frontend files:
   - Update `frontend/js/app.js` to use production API URL
5. Create service
6. Copy the site URL (e.g., `https://edulearn-web.onrender.com`)

### 5. Configure Razorpay

1. Go to https://dashboard.razorpay.com
2. Get your Key ID and Key Secret
3. Add Webhook URL: `https://edulearn-api.onrender.com/payment/webhook`

### 6. Seed Production Database

After deployment:

```bash
# Connect to production database
psql <your-database-url>

# Then run seed data (manually or via API)
```

### 7. Update Frontend Configuration

Edit `frontend/js/app.js`:

```javascript
const API_BASE_URL = 'https://edulearn-api.onrender.com';
```

### 8. Update Razorpay Key in Frontend

Edit `frontend/checkout.html`:

```javascript
key: "YOUR_RAZORPAY_KEY_ID", // Replace with production key
```

### 9. Test Deployment

1. Visit: `https://edulearn-web.onrender.com`
2. Try register and login
3. Check dashboard
4. Test course enrollment

### Troubleshooting

**Database Connection Error:**
- Verify DATABASE_URL format
- Ensure internal Database URL is used
- Check firewall rules

**Static files not loading:**
- Ensure `frontend/` directory is correct
- Check publish directory setting
- Clear browser cache

**Payment not working:**
- Verify Razorpay keys are correct
- Check webhook URL is accessible
- Test in Razorpay test mode first

### Important Notes

⚠️ **Before Production:**
- Change `SECRET_KEY` to a strong random value
- Update `RAZORPAY_KEY_ID` and `RAZORPAY_KEY_SECRET`
- Set up HTTPS (Render does this automatically)
- Enable CORS only for your frontend domain
- Set up database backups
- Monitor logs regularly

### Maintenance

**Regular Tasks:**
1. Update dependencies monthly
2. Monitor database size
3. Check error logs
4. Update courses and content
5. Backup database regularly

**Monitoring:**
- Render Dashboard: Check CPU, Memory
- Application Logs: Look for errors
- Razorpay Dashboard: Monitor transactions
- User Feedback: Collect and address issues

---

**Your platform is now live! 🚀**

Access at: `https://edulearn-web.onrender.com`
API at: `https://edulearn-api.onrender.com`
