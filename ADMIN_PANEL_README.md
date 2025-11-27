# 🔐 Admin Control Panel - Complete Setup Guide

## 📋 Overview

Gawa ko ng comprehensive admin panel para sa hosting platform mo. May complete features para ma-monitor lahat ng users, files, activities, at disk usage.

---

## ✨ Features Implemented

### 1. **Admin Authentication**
- Secure admin login page
- Default admin account (auto-created on first run)
- Session-based authentication
- Logout functionality

### 2. **Main Dashboard**
- Real-time statistics:
  - Total users
  - Total disk usage (MB)
  - Total bots
  - Active/running bots
- Search functionality by username o email
- User list table with detailed information
- Auto-refresh every 30 seconds

### 3. **User Management**
Per user, makikita mo:
- **Personal Info:**
  - Username
  - Email
  - Account creation date
  - Last login time
  - Account balance

- **Storage:**
  - Disk usage visualization
  - Total file count
  - Bot count
  - Running bots count

### 4. **File Management**
- View all uploaded files per user
- File size tracking
- Upload timestamps
- Bot association
- Sortable table

### 5. **Activity Tracking**
- Login history
- IP address tracking
- Timestamped activities
- Up to 50 recent logins

### 6. **Bot Monitoring**
- Bot name
- Bot ID
- Status (running/stopped)
- Creation date
- Expiration date

---

## 🚀 How to Start

### Step 1: Access Admin Panel
```
URL: http://localhost:5000/admin/login
```

### Step 2: Default Credentials
```
Username: admin
Password: admin123
```

### Step 3: Dashboard
```
URL: http://localhost:5000/admin/dashboard
```

---

## 📊 Database Models

### 1. **UserActivity** (New)
Tracks user login history:
```
- id (Primary Key)
- user_id (Foreign Key → User)
- login_time (DateTime)
- disk_usage (Float - MB)
- ip_address (String)
```

### 2. **UploadedFile** (New)
Tracks file uploads:
```
- id (Primary Key)
- user_id (Foreign Key → User)
- bot_id (Foreign Key → HostedBot)
- filename (String)
- file_size (Float - MB)
- uploaded_at (DateTime)
- file_path (String)
```

### 3. **Admin** (New)
Admin accounts:
```
- id (Primary Key)
- username (String)
- password_hash (String)
- is_admin (Boolean)
- created_at (DateTime)
```

---

## 🔗 API Endpoints

### Admin Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/admin/login` | GET/POST | Admin login page |
| `/admin/dashboard` | GET | Main admin dashboard |
| `/admin/user/<id>` | GET | User details page |
| `/admin/logout` | GET | Admin logout |

### API Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/admin/api/users` | GET | Get all users (JSON) |
| `/admin/api/user/<id>/files` | GET | Get user files |
| `/admin/api/user/<id>/activity` | GET | Get user activity |

---

## 📁 New Files Created

```
templates/
├── admin_login.html         ← Admin login page
├── admin_dashboard.html     ← Main admin dashboard
└── admin_user_detail.html   ← User details page

ADMIN_SETUP.md              ← Setup instructions
ADMIN_PANEL_README.md       ← This file
```

---

## 🎨 UI/UX Features

✅ **Modern Design**
- Gradient purple theme
- Responsive layout
- Mobile-friendly
- Dark-mode ready design

✅ **User Experience**
- Search functionality
- Real-time refresh
- Sort/filter options
- Color-coded status badges
- Smooth animations
- Hover effects

✅ **Data Visualization**
- Disk usage bars
- Statistics cards
- Tables with pagination
- Time formatting
- File size display

---

## 🔒 Security Features

✅ Session-based authentication
✅ Password hashing (werkzeug)
✅ Admin-only routes
✅ CSRF protection ready
✅ Input validation

⚠️ **Important Security Notes:**
1. Change default admin password immediately
2. Use strong passwords
3. Set SECRET_KEY environment variable in production
4. Use HTTPS in production
5. Implement rate limiting
6. Add logging for security events

---

## 📈 Tracking Information

### What Gets Tracked

1. **User Activity**
   - Login time
   - IP address
   - Disk usage

2. **File Uploads**
   - Filename
   - File size
   - Upload timestamp
   - Bot association

3. **Bot Information**
   - Bot name & ID
   - Status
   - Creation date
   - Expiration date

---

## 💾 Database Integration

Lahat ng data ay automatically tracked sa database:

```python
# Login tracking
activity = UserActivity(
    user_id=user.id,
    login_time=datetime.utcnow(),
    ip_address=request.remote_addr
)

# File tracking
uploaded_file = UploadedFile(
    user_id=user_id,
    filename=file.filename,
    file_size=file_size,
    file_path=file_path
)
```

---

## 🛠️ Customization

### Change Admin Credentials

Edit sa app.py, sa `if __name__ == '__main__':` section:

```python
if not Admin.query.filter_by(username='admin').first():
    admin = Admin(
        username='YOUR_USERNAME',
        password_hash=generate_password_hash('YOUR_PASSWORD'),
        is_admin=True
    )
```

### Customize Theme

Edit CSS sa admin templates para baguhin ang colors:

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Auto-Refresh Rate

Change sa admin_dashboard.html:

```javascript
setInterval(loadUsers, 30000); // Change 30000 to desired milliseconds
```

---

## 📋 Checklist

- [x] Admin authentication system
- [x] Admin dashboard with statistics
- [x] User list with search
- [x] User detail page
- [x] File tracking
- [x] Activity tracking
- [x] Bot monitoring
- [x] Responsive design
- [x] Database models
- [x] API endpoints
- [x] Session management

---

## 🎯 Next Steps

1. **Test the Panel**
   - Login with default credentials
   - Navigate through dashboard
   - View user details

2. **Change Admin Password**
   - Delete existing database (optional)
   - Restart application
   - Update default credentials

3. **Monitor Users**
   - Check login activity
   - Monitor disk usage
   - Track file uploads
   - Monitor bot status

4. **Production Setup**
   - Use environment variables for credentials
   - Set up HTTPS
   - Configure firewall
   - Set up backups
   - Enable logging

---

## 📞 Support Information

Panel created with:
- Flask web framework
- SQLAlchemy ORM
- Jinja2 templates
- Modern CSS/JavaScript
- SQLite database

---

## 🎉 Ready to Go!

Your admin panel is now ready to use. Login at:

**http://localhost:5000/admin/login**

**Credentials:**
- Username: `admin`
- Password: `admin123`

⚠️ **Remember to change the default password immediately after first login!**

---

Happy hosting! 🚀
