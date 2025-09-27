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
