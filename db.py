from sqlmodel import SQLModel, create_engine, Session
from models import *

engine = create_engine('postgresql://postgresql:{DB_PASSWORD}@localhost:5432/{DB_NAME}')

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def init_data():
    with Session(engine) as session:

        if session.exec(Genre.select()).first():
            return
        
        pop = Genre(name="Pop", description="Popular music")
        kpop = Genre(name="Kpop", description="Korean popular music")
        session.add_all([pop, kpop])
        session.commit()
        
        artist1 = Artist(name="Luka", genre_id=1)
        artist2 = Artist(name="Hyuona", genre_id=2)
        session.add_all([artist1, artist2])
        session.commit()
        
        album1 = Album(title="Round 5", artist_id=1)
        album2 = Album(title="B-side", artist_id=2)
        session.add_all([album1, album2])
        session.commit()
        
        song1 = Song(title="Ruler of my heart", duration=219, file_url="/music/song1.mp3", album_id=1, genre_id=1)
        song2 = Song(title="All in", duration=259, file_url="/music/song2.mp3", album_id=2, genre_id=2)
        session.add_all([song1, song2])
        session.commit()
        
        user1 = User(email="stacy@example.com", password="1234", username="i_love_hyuona", registration_date="2025-01-01")
        user2 = User(email="jessica@example.com", password="1235", username="i_love_luka", registration_date="2025-03-04")
        session.add(user1, user2)
        session.commit()

        playlist1 = Playlist(title="Alien Stage", user_id=1)
        session.add(playlist1)
        session.commit()        
        
        print("все ок")