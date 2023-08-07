# views.py
from flask import Blueprint, jsonify
from injector import inject

from ..services import GreetingService

bp = Blueprint('main', __name__)

@bp.route('/')
@inject
def index(greeting_service: GreetingService):
    greeting = greeting_service.get_greeting()
    return jsonify({'message': greeting})
