import string, secrets

from sqlalchemy.orm import Session
from . import crud

def gen_key(l: int = 5):
    s = string.ascii_letters + string.digits
    return "".join(secrets.choice(s) for _ in range(l))

def check_unique(db: Session):
    key = gen_key()
    while crud.get_db_url_by_key(db, key):
        key = gen_key()
    return key