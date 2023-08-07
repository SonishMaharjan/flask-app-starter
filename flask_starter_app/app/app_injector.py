# injector.py
from injector import Binder, singleton

from .services import GreetingService

def configure(binder: Binder) -> None:
    binder.bind(GreetingService, to=GreetingService, scope=singleton)
