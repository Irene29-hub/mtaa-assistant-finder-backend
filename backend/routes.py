from flask import Blueprint, jsonify, request, current_app
from extensions import db
from models import Conversation, Message, Role
from ai_agent import generate_agent_reply

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/conversations", methods=["POST"])
def create_conversation():
    data = request.get_json() or {}
    title = data.get("title", None)
    conv = Conversation(title=title)
    db.session.add(conv)
    db.session.commit()
    return jsonify({"id": conv.id, "title": conv.title}), 201

@bp.route("/conversations/<conv_id>/messages", methods=["GET"])
def get_messages(conv_id):
    conv = Conversation.query.get_or_404(conv_id)
    msgs = [
        {"id": m.id, "role": m.role.value, "content": m.content, "created_at": m.created_at.isoformat()}
        for m in conv.messages
    ]
    return jsonify({"conversation": {"id": conv.id, "title": conv.title}, "messages": msgs})

@bp.route("/conversations/<conv_id>/message", methods=["POST"])
def user_message(conv_id):
    conv = Conversation.query.get_or_404(conv_id)
    data = request.get_json() or {}
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "text required"}), 400

    reply = generate_agent_reply(conv, text)
    return jsonify({"reply": reply})

# Simple health check
@bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})
