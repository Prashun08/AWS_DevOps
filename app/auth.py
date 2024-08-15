from flask import session
import uuid

def login_user(user_id):
    session['user_id'] = user_id
    session['session_id'] = str(uuid.uuid4())

def logout_user():
    session.pop('user_id', None)
    session.pop('session_id', None)

def is_logged_in():
    return 'user_id' in session

def get_current_user():
    return session.get('user_id', None)
