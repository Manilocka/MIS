from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import *

engine = create_engine('postgresql://postgresql:{DB_PASSWORD}@localhost:5432/{DB_NAME}')

with Session(engine) as session:
    statement = select(User)
    users = session.exec(statement).all()
    for user in users:
        print(f"- {user.username} ({user.email})")

with Session(engine) as session:
    statement = select(Song).join(Album).join(Artist).where(Artist.name == "Luka")
    songs = session.exec(statement).all()
    for song in songs:
        print(f"- {song.title}")

with Session(engine) as session:
    statement = select(Genre)
    genres = session.exec(statement).all()
    for genre in genres:
        print(f"- {genre.name}")

with Session(engine) as session:
    statement = select(User).where(User.email == "stacy@example.com")
    user = session.exec(statement).first()
    print(user)