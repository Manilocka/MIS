from sqlmodel import SQLModel, create_engine, Session, select
from models import *
def create_db_and_tables():

    # Base.metadata.create_all(engine)
    SQLModel.metadata.create_all(engine)

def init_data():
    with Session(engine) as session:

        existing_genres = session.exec(select(Genre)).first()
        if existing_genres:
            print("Данные уже существуют, пропускаем инициализацию")
            return
        

        pop = Genre(name="Pop", description="Popular music")
        kpop = Genre(name="Kpop", description="Korean popular music")
        session.add_all([pop, kpop])
        session.commit()
        

        artist1 = Artist(name="Luka", bio="Pop artist", photo_url="/images/luka.jpg", genre_id=1)
        artist2 = Artist(name="Hyuona", bio="K-pop artist", photo_url="/images/hyuona.jpg", genre_id=2)
        session.add_all([artist1, artist2])
        session.commit()
        
 
        album1 = Album(title="Round 5", cover_art_url="/covers/round5.jpg", release_date="2024-01-01", artist_id=1)
        album2 = Album(title="B-side", cover_art_url="/covers/bside.jpg", release_date="2024-02-01", artist_id=2)
        session.add_all([album1, album2])
        session.commit()
        
   
        song1 = Song(title="Ruler of my heart", duration=219, file_url="/music/song1.mp3", bitrate=320, release_date="2024-01-01", album_id=1, genre_id=1)
        song2 = Song(title="All in", duration=259, file_url="/music/song2.mp3", bitrate=320, release_date="2024-02-01", album_id=2, genre_id=2)
        session.add_all([song1, song2])
        session.commit()
        
    
        user1 = User(email="stacy@example.com", password="1234", username="i_love_hyuona", date_of_birth="1990-01-01", country="USA", subscription_type="premium", registration_date="2025-01-01")
        user2 = User(email="jessica@example.com", password="1235", username="i_love_luka", date_of_birth="1992-05-15", country="Canada", subscription_type="free", registration_date="2025-03-04")
        session.add_all([user1, user2])
        session.commit()

       
        playlist1 = Playlist(title="Alien Stage", description="My favorite songs", cover_image_url="/playlists/alien_stage.jpg", created_date="2025-01-01", user_id=1)
        session.add(playlist1)
        session.commit()        
        
        print("Данные успешно инициализированы!")

def get_all_users():
    """Получить всех пользователей"""
    with Session(engine) as session:
        return session.exec(select(User)).all()

def get_all_songs():
    """Получить все песни"""
    with Session(engine) as session:
        return session.exec(select(Song)).all()

def get_songs_by_artist(artist_name: str):
    """Получить песни конкретного артиста"""
    with Session(engine) as session:
        statement = select(Song).join(Album).join(Artist).where(Artist.name == artist_name)
        return session.exec(statement).all()

def get_all_genres():
    """Получить все жанры"""
    with Session(engine) as session:
        return session.exec(select(Genre)).all()

def get_all_artists():
    """Получить всех артистов"""
    with Session(engine) as session:
        return session.exec(select(Artist)).all()

def get_all_albums():
    """Получить все альбомы"""
    with Session(engine) as session:
        return session.exec(select(Album)).all()

def get_all_playlists():
    """Получить все плейлисты"""
    with Session(engine) as session:
        return session.exec(select(Playlist)).all()

def get_user_by_email(email: str):
    """Получить пользователя по email"""
    with Session(engine) as session:
        return session.exec(select(User).where(User.email == email)).first()

if __name__ == '__main__':
   
    create_db_and_tables()
    init_data()
    
    # Все пользователи
    print("\n1. Все пользователи:")
    users = get_all_users()
    for user in users:
        print(f"   - {user.username} ({user.email})")
    
    # Песни конкретного артиста
    print("\n2. Песни артиста Luka:")
    songs = get_songs_by_artist("Luka")
    for song in songs:
        print(f"   - {song.title} ({song.duration} сек)")
    
    # Все жанры
    print("\n3. Все жанры:")
    genres = get_all_genres()
    for genre in genres:
        print(f"   - {genre.name}: {genre.description}")
    
    # Поиск пользователя по email
    print("\n4. Пользователь с email stacy@example.com:")
    user = get_user_by_email("stacy@example.com")
    if user:
        print(f"   - {user.username} ({user.email})")
    else:
        print("   - Пользователь не найден")