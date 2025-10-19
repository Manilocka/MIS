from sqlmodel import create_engine


engine = create_engine("sqlite:///./music_db.sqlite")
