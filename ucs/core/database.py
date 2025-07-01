from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager
from dotenv import load_dotenv
from pathlib import Path
import os

# ── 1. определяем корень репозитория ────────────────────────────────
ROOT_DIR = Path(__file__).resolve().parents[2]   # .../user-update-sys

# ── 2. грузим .env один-единственный раз ────────────────────────────
ENV_PATH = ROOT_DIR / ".env"
load_dotenv(ENV_PATH)          # override=False по умолчанию


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()