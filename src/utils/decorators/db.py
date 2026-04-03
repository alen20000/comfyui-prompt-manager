import sqlite3
from functools import wraps

def db_operation(func):
    """統一處理 DB 例外，印出錯誤訊息後 re-raise"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except sqlite3.IntegrityError as e:
            print(f"[DB 約束錯誤] {func.__name__}: {e}")
            raise
        except sqlite3.Error as e:
            print(f"[DB 錯誤] {func.__name__}: {e}")
            raise
    return wrapper