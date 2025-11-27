# 🚀 Quick Start Guide - Admin Panel

## ⚡ 5-Minute Setup

### 1. Start the Server
```bash
python app.py
```

You'll see:
```
✅ Default admin account created: username=admin, password=admin123
⚠️  IMPORTANT: Change the default admin password immediately!
```

### 2. Open Browser
```
http://localhost:5000/admin/login
```

### 3. Login
```
Username: admin
Password: admin123
```

### 4. You're In! 🎉

---

## 📊 Dashboard Features

### Top Stats
```
┌─────────────────┬──────────────────┬────────────┬──────────────┐
│ Total Users     │ Total Disk (MB)  │ Total Bots │ Active Bots  │
├─────────────────┼──────────────────┼────────────┼──────────────┤
│ Auto-updating   │ Real-time size   │ Count      │ Running now  │
└─────────────────┴──────────────────┴────────────┴──────────────┘
```

### User Table
```
Username | Email | Created | Last Login | Disk | Files | Bots | Balance | Action
─────────┼───────┼─────────┼────────────┼──────┼───────┼──────┼─────────┼────────
john     | j@... | 2024... | 2024...    | 125MB| 5     | 2    | ₱500    | View
```

---

## 👤 User Detail Page

Click "View Details" para makita:

### 📁 Files Tab
- All uploaded files
- File sizes
- Upload dates
- Bot association

### 📊 Activity Tab
- Login history
- IP addresses
- Login timestamps

### 🤖 Bots Tab
- Bot names
- Bot IDs
- Status (running/stopped)
- Created dates
- Expiration dates

---

## 🔍 Search Users

```
Search Bar → Type username or email → Results filter in real-time
```

Example:
- Type: `john` → Shows john's profile
- Type: `gmail.com` → Shows all gmail users

---

## 💾 Database Tracking

**Automatically Tracked:**

✅ Every user login
- When
- From where (IP)
- Login timestamp

✅ Every file upload
- Filename
- Size (MB)
- Upload time
- Which bot it belongs to

✅ Each bot
- Name & ID
- Status
- Running/Stopped
- Expiration

---

## 🎨 Interface Overview

```
┌─────────────────────────────────────────────────┐
│ 🔐 Admin Panel                        [Logout]  │
├──────────────────────────────────────────────── │
│                                                  │
│ 📊 Dashboard      │ ┌──────────────────────┐   │
│ 👥 Users         │ │ Statistics Cards     │   │
│ 🚪 Logout        │ ├──────────────────────┤   │
│                  │ │ User List Table      │   │
│                  │ │ (searchable)         │   │
│                  │ └──────────────────────┘   │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## 🔐 Security Reminders

1. **Change Admin Password** (IMPORTANT)
   - Don't use default in production
   - Use strong password

2. **IP Whitelisting** (Optional)
   - Restrict admin access
   - Add to firewall

3. **HTTPS** (Production)
   - Enable SSL/TLS
   - Don't run on HTTP in production

4. **Regular Backups**
   - Backup database regularly
   - Backup uploaded files

---

## 📱 Mobile Friendly

Panel works on:
- ✅ Desktop
- ✅ Tablet
- ✅ Mobile

Responsive design adapts automatically.

---

## ⏰ Auto-Refresh

Dashboard automatically updates every 30 seconds.

Manual refresh: Press **F5** or **Ctrl+R**

---

## 🆘 Troubleshooting

### Can't login?
- Check username: `admin`
- Check password: `admin123`
- Clear browser cache

### Panel not showing data?
- Make sure server is running
- Refresh page (F5)
- Check database file exists

### Want to reset admin password?
1. Delete `hosting_panel.db`
2. Restart server
3. Default password reset to `admin123`

---

## 📈 What You Can Do

✅ Monitor all users in one place
✅ Track file uploads
✅ Check storage usage
✅ View login history
✅ Monitor bot status
✅ Search users
✅ View user balance
✅ Track user activity

---

## 🎯 Common Tasks

### View All Users
→ Dashboard → See table

### Check Specific User
→ Dashboard → Find user → Click "View Details"

### Monitor Disk Usage
→ Dashboard → Look at "Disk Usage" column

### Check User Files
→ User Details → Files Tab

### View Login History
→ User Details → Activity Tab

### Monitor Bots
→ User Details → Bots Tab

---

## 🚀 You're All Set!

Admin Panel is ready to use:
- Dashboard: `http://localhost:5000/admin/dashboard`
- User Management: Built in
- Activity Tracking: Automatic
- File Monitoring: Real-time

Start managing your platform! 🎉

---

**Need help?** Check ADMIN_SETUP.md for detailed information.
