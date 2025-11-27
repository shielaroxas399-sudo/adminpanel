# Admin Panel Setup Instructions

## Features ng Panel

✅ **User Management Dashboard**
- View lahat ng users sa isang table
- Search users by username o email
- Real-time disk usage monitoring
- File count tracking
- Bot status monitoring

✅ **Detailed User Information**
- Complete user profile
- Gmail/Email address
- Password (hashed for security)
- Account creation date
- Last login time
- Account balance

✅ **File Management**
- View lahat ng uploaded files per user
- File size tracking
- Upload timestamp
- Bot association

✅ **Activity Tracking**
- Login history
- IP address tracking
- Timestamped activities
- Login frequency

✅ **Bot Monitoring**
- Bot status (running/stopped)
- Bot expiration dates
- Bot creation dates
- Running bots count

## How to Access Admin Panel

1. **Admin Login Page**
   - URL: `http://localhost:5000/admin/login`
   - Default Username: `admin`
   - Default Password: `admin123`

2. **Admin Dashboard**
   - URL: `http://localhost:5000/admin/dashboard`
   - Overview ng lahat ng users
   - Statistics at metrics
   - Search functionality

3. **User Details**
   - Click "View Details" button sa anumang user
   - Makikita lahat ng user information
   - Files, activity, at bots

## Database Models Added

### UserActivity
Nag-track ng user logins at disk usage:
```
- user_id
- login_time
- disk_usage (MB)
- ip_address
```

### UploadedFile
Nag-track ng lahat ng uploaded files:
```
- user_id
- bot_id
- filename
- file_size (MB)
- uploaded_at
- file_path
```

### Admin
Admin account management:
```
- username
- password_hash
- is_admin
- created_at
```

## Changes sa Existing Files

### app.py
- Added 3 new database models
- Added admin routes
- Added user activity tracking sa login
- Added file tracking sa upload
- Added helper functions

### Routes Added
- `/admin/login` - Admin login page
- `/admin/dashboard` - Main admin dashboard
- `/admin/user/<user_id>` - Detailed user information
- `/admin/api/users` - JSON API para sa users
- `/admin/api/user/<user_id>/files` - User files API
- `/admin/api/user/<user_id>/activity` - User activity API
- `/admin/logout` - Admin logout

## Security Notes

⚠️ **IMPORTANT:**
1. Change the default admin password immediately after first login
2. Use strong passwords para sa admin account
3. Make sure SECRET_KEY sa app config is changed
4. In production, use environment variables para sa admin credentials

## UI Features

- Modern gradient design
- Responsive layout (mobile-friendly)
- Real-time data refresh
- Search functionality
- Sortable tables
- Color-coded status badges
- Disk usage visualization
- Smooth animations at transitions

## Disk Usage Calculation

Ang disk usage ay kinakalkula based sa:
- Lahat ng bot folders ng user
- Total file sizes sa storage
- Tracked sa UserActivity model

## Auto-Refresh

Dashboard automatically refreshes every 30 seconds para sa latest data

## Next Steps

1. Mag-test ng admin panel
2. Change default admin password
3. Monitor user activities
4. Track storage usage
5. Manage user accounts

---

Created for Bot Hosting Panel Administration
Enjoy managing your platform! 🚀
