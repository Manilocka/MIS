from sqlmodel import create_engine

# Central place for DB engine per simplified structure (database.py, models.py, schemas.py, main.py)
engine = create_engine("sqlite:///./music_db.sqlite")
