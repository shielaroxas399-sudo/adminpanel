"""
ADMIN CONTROL PANEL - Standalone Application
Manage users, files, activities, and bots from a centralized dashboard
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime, timedelta
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin_panel.db'

db = SQLAlchemy(app)

# ═══════════════════════════════════════════════════════════════════════
# DATABASE MODELS
# ═══════════════════════════════════════════════════════════════════════

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    balance = db.Column(db.Float, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    activities = db.relationship('UserActivity', backref='user', lazy=True)
    uploaded_files = db.relationship('UploadedFile', backref='user', lazy=True)
    bots = db.relationship('HostedBot', backref='owner', lazy=True)

class HostedBot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bot_id = db.Column(db.String(36), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bot_name = db.Column(db.String(100), nullable=False)
    main_file = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='stopped')
    process_id = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=True)
    upload_path = db.Column(db.String(200), nullable=False)

class UserActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    login_time = db.Column(db.DateTime, default=datetime.utcnow)
    disk_usage = db.Column(db.Float, default=0)
    ip_address = db.Column(db.String(50))

class UploadedFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bot_id = db.Column(db.String(36), nullable=True)
    filename = db.Column(db.String(200), nullable=False)
    file_size = db.Column(db.Float, default=0)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    file_path = db.Column(db.String(500))

# ═══════════════════════════════════════════════════════════════════════
# ADMIN ROUTES
# ═══════════════════════════════════════════════════════════════════════

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        admin = Admin.query.filter_by(username=username).first()
        
        if admin and check_password_hash(admin.password_hash, password):
            session['admin_id'] = admin.id
            session['admin_username'] = admin.username
            return jsonify({'message': 'Login successful'}), 200
        
        return jsonify({'error': 'Invalid credentials'}), 401
    
    return render_template('admin_login.html')

@app.route('/dashboard')
def dashboard():
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    users = User.query.all()
    user_data = []
    
    for user in users:
        disk_usage = sum(f.file_size for f in user.uploaded_files)
        latest_activity = UserActivity.query.filter_by(user_id=user.id).order_by(UserActivity.login_time.desc()).first()
        last_login = latest_activity.login_time if latest_activity else user.created_at
        
        file_count = len(user.uploaded_files)
        bot_count = len(user.bots)
        running_bots = sum(1 for bot in user.bots if bot.status == 'running')
        
        user_data.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at,
            'last_login': last_login,
            'disk_usage': round(disk_usage, 2),
            'file_count': file_count,
            'bot_count': bot_count,
            'running_bots': running_bots,
            'balance': user.balance
        })
    
    return render_template('admin_dashboard.html', users=user_data)

@app.route('/user/<int:user_id>')
def user_detail(user_id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    activities = UserActivity.query.filter_by(user_id=user_id).order_by(UserActivity.login_time.desc()).limit(20).all()
    files = UploadedFile.query.filter_by(user_id=user_id).order_by(UploadedFile.uploaded_at.desc()).all()
    bots = HostedBot.query.filter_by(user_id=user_id).all()
    
    return render_template('admin_user_detail.html', user=user, activities=activities, files=files, bots=bots)

@app.route('/api/users', methods=['GET'])
def get_users():
    if 'admin_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    users = User.query.all()
    user_list = []
    
    for user in users:
        disk_usage = sum(f.file_size for f in user.uploaded_files)
        latest_activity = UserActivity.query.filter_by(user_id=user.id).order_by(UserActivity.login_time.desc()).first()
        last_login = latest_activity.login_time if latest_activity else user.created_at
        
        user_list.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at.isoformat(),
            'last_login': last_login.isoformat(),
            'disk_usage': round(disk_usage, 2),
            'files_count': len(user.uploaded_files),
            'bots_count': len(user.bots),
            'balance': user.balance
        })
    
    return jsonify(user_list), 200

@app.route('/api/user/<int:user_id>/files', methods=['GET'])
def get_user_files(user_id):
    if 'admin_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    files = UploadedFile.query.filter_by(user_id=user_id).order_by(UploadedFile.uploaded_at.desc()).all()
    
    file_list = [{
        'id': f.id,
        'filename': f.filename,
        'size': f.file_size,
        'uploaded_at': f.uploaded_at.isoformat(),
        'bot_id': f.bot_id
    } for f in files]
    
    return jsonify(file_list), 200

@app.route('/api/user/<int:user_id>/activity', methods=['GET'])
def get_user_activity(user_id):
    if 'admin_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    activities = UserActivity.query.filter_by(user_id=user_id).order_by(UserActivity.login_time.desc()).limit(50).all()
    
    activity_list = [{
        'login_time': a.login_time.isoformat(),
        'disk_usage': a.disk_usage,
        'ip_address': a.ip_address
    } for a in activities]
    
    return jsonify(activity_list), 200

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ═══════════════════════════════════════════════════════════════════════
# INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Create default admin account if it doesn't exist
        if not Admin.query.filter_by(username='admin').first():
            admin = Admin(
                username='admin',
                password_hash=generate_password_hash('admin123'),
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()
            print("✅ Default admin account created: username=admin, password=admin123")
            print("⚠️  IMPORTANT: Change the default admin password immediately!")
    
    print("\n🚀 Admin Control Panel Started")
    print("📊 Access at: http://localhost:5000/login")
    print("👤 Username: admin")
    print("🔑 Password: admin123\n")
    
    app.run(debug=False, host='0.0.0.0', port=5000)
