# utils.py

import time
import threading
from functools import wraps
from datetime import datetime

def capitalize(text: str) -> str:
    if not text:
        return ''
    return text[0].upper() + text[1:]

def debounce(wait):
    def decorator(func):
        timer = None

        @wraps(func)
        def debounced(*args, **kwargs):
            nonlocal timer

            def call_it():
                func(*args, **kwargs)

            if timer is not None:
                timer.cancel()
            timer = threading.Timer(wait, call_it)
            timer.start()

        return debounced
    return decorator

def throttle(wait):
    def decorator(func):
        last_time = 0

        @wraps(func)
        def throttled(*args, **kwargs):
            nonlocal last_time
            now = time.time()
            if now - last_time >= wait:
                last_time = now
                return func(*args, **kwargs)
        return throttled
    return decorator

def copy_to_clipboard(text: str):
    # No direct clipboard in Python standard, you need pyperclip or OS-specific tools
    try:
        import pyperclip
        pyperclip.copy(text)
    except ImportError:
        print("Install pyperclip module for clipboard support")

def format_date(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d")
