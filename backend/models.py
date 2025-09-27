from extensions import db
from datetime import datetime
import enum
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Role(enum.Enum):
    user = "user"
    assistant = "assistant"
    system = "system"

class UserRole(enum.Enum):
    homeowner = "homeowner"
    fundi = "fundi"

class JobStatus(enum.Enum):
    open = "open"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    jobs = db.relationship("Job", back_populates="user", cascade="all, delete-orphan")
    quotes = db.relationship("Quote", back_populates="user", cascade="all, delete-orphan")

class Job(db.Model):
    __tablename__ = "jobs"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.Float, nullable=False)
    preferred_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum(JobStatus), default=JobStatus.open)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship("User", back_populates="jobs")
    quotes = db.relationship("Quote", back_populates="job", cascade="all, delete-orphan")

class Quote(db.Model):
    __tablename__ = "quotes"
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey("jobs.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    price = db.Column(db.Float, nullable=False)
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    job = db.relationship("Job", back_populates="quotes")
    user = db.relationship("User", back_populates="quotes")

class Conversation(db.Model):
    __tablename__ = "conversations"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    title = db.Column(db.String(150), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    messages = db.relationship("Message", back_populates="conversation", cascade="all, delete-orphan")

class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    conversation_id = db.Column(db.String, db.ForeignKey("conversations.id"), nullable=False)
    role = db.Column(db.Enum(Role), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    conversation = db.relationship("Conversation", back_populates="messages")
