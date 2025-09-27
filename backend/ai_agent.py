import os
import openai
from extensions import db
from models import Conversation, Message, Role

openai.api_key = os.getenv("OPENAI_API_KEY")

DEFAULT_SYSTEM_PROMPT = (
    "You are MTAA Assistant: helpful, concise, and context-aware. "
    "Keep answers practical and friendly for users looking for local artisans and jobs."
)

def generate_agent_reply(conversation, user_message, model="gpt-4o-mini"):
    # store user message
    user_msg = Message(conversation_id=conversation.id, role=Role.user, content=user_message)
    db.session.add(user_msg)
    db.session.commit()

    # build messages history for the LLM (last N messages to limit token use)
    msgs = [
        {"role": "system", "content": DEFAULT_SYSTEM_PROMPT}
    ]
    # include last 20 messages
    history = Message.query.filter_by(conversation_id=conversation.id).order_by(Message.created_at.asc()).all()
    for m in history[-20:]:
        msgs.append({"role": m.role.value, "content": m.content})

    # call OpenAI
    try:
        resp = openai.ChatCompletion.create(
            model=model,
            messages=msgs,
            max_tokens=512,
            temperature=0.2,
        )
        assistant_text = resp.choices[0].message["content"].strip()
    except Exception as e:
        assistant_text = f"Error generating response: {str(e)}"

    # store assistant message
    assistant_msg = Message(conversation_id=conversation.id, role=Role.assistant, content=assistant_text)
    db.session.add(assistant_msg)
    db.session.commit()

    return assistant_text
