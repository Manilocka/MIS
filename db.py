from sqlmodel import SQLModel, Session, select
from models import *
from database import engine
def create_db_and_tables():
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
        

        artist1 = Artist(name="Luka", bio="Pop artist", photo_url="/static/images/luka.jpg", genre_id=1)
        artist2 = Artist(name="Hyuona", bio="K-pop artist", photo_url="/static/images/hyuona.jpg", genre_id=2)
        artist3 = Artist(name="Ivan", bio="K-pop artist", photo_url="/static/images/ivan.jpg", genre_id=2)
        session.add_all([artist1, artist2, artist3])
        session.commit()
        
 
        album1 = Album(title="Round 5", cover_art_url="/static/images/round5.jpg", release_date="2024-01-01", artist_id=1)
        album2 = Album(title="B-Side", cover_art_url="/static/images/B-Side.jpg", release_date="2024-02-01", artist_id=2)
        album3 = Album(title="Ivan Album", cover_art_url="/static/images/ivan_album.jpg", release_date="2024-03-01", artist_id=3)
        session.add_all([album1, album2, album3])
        session.commit()
        
   
        song1 = Song(title="Ruler of my heart", duration=219, file_url="/static/music/song1.mp3", bitrate=320, release_date="2024-01-01", album_id=1, genre_id=1)
        song2 = Song(title="Paratise", duration=259, file_url="/static/music/song2.mp3", bitrate=320, release_date="2024-02-01", album_id=2, genre_id=2)
        song3 = Song(title="All in", duration=180, file_url="/static/music/all_in.mp3", bitrate=320, release_date="2024-03-01", album_id=3, genre_id=2)
        session.add_all([song1, song2, song3])
        session.commit()
        
    
        user1 = User(email="stacy@example.com", password="1234", username="i_love_hyuona", date_of_birth="2003-07-03", country="USA", registration_date="2025-01-01")
        user2 = User(email="diana@example.com", password="1235", username="i_love_ivan", date_of_birth="2001-11-04", country="Canada", registration_date="2025-03-04")
        user3 = User(email="jessica@example.com", password="1235", username="i_love_luka", date_of_birth="2024-09-06", country="USA", registration_date="2025-03-04")
        session.add_all([user1, user2, user3])
        session.commit()

       
        playlist1 = Playlist(title="Alien Stage", description="My favorite songs", cover_image_url="/static/images/alien_stage.jpg", created_date="2025-01-01", user_id=1)
        session.add(playlist1)
        session.commit()        
        

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



def add_user(email: str, password: str, username: str, date_of_birth: str = None, 
             country: str = None, registration_date: str = None):
    """Добавить нового пользователя"""
    with Session(engine) as session:
        user = User(
            email=email, 
            password=password, 
            username=username,
            date_of_birth=date_of_birth,
            country=country,
            registration_date=registration_date
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        print(f"Пользователь {username} добавлен с ID: {user.user_id}")
        return user

def add_genre(name: str, description: str = None):
    """Добавить новый жанр"""
    with Session(engine) as session:
        genre = Genre(name=name, description=description)
        session.add(genre)
        session.commit()
        session.refresh(genre)
        print(f"Жанр {name} добавлен с ID: {genre.genre_id}")
        return genre

def add_artist(name: str, bio: str = None, photo_url: str = None, genre_id: int = None):
    """Добавить нового артиста"""
    with Session(engine) as session:
        artist = Artist(name=name, bio=bio, photo_url=photo_url, genre_id=genre_id)
        session.add(artist)
        session.commit()
        session.refresh(artist)
        print(f"Артист {name} добавлен с ID: {artist.artist_id}")
        return artist

def add_album(title: str, cover_art_url: str = None, release_date: str = None, artist_id: int = None):
    """Добавить новый альбом"""
    with Session(engine) as session:
        album = Album(title=title, cover_art_url=cover_art_url, release_date=release_date, artist_id=artist_id)
        session.add(album)
        session.commit()
        session.refresh(album)
        print(f"Альбом {title} добавлен с ID: {album.album_id}")
        return album

def add_song(title: str, duration: int, file_url: str = None, bitrate: int = None, 
             release_date: str = None, album_id: int = None, genre_id: int = None):
    """Добавить новую песню"""
    with Session(engine) as session:
        song = Song(
            title=title, 
            duration=duration, 
            file_url=file_url, 
            bitrate=bitrate,
            release_date=release_date, 
            album_id=album_id, 
            genre_id=genre_id
        )
        session.add(song)
        session.commit()
        session.refresh(song)
        print(f"Песня {title} добавлена с ID: {song.song_id}")
        return song

def add_playlist(title: str, description: str = None, cover_image_url: str = None, 
                 created_date: str = None, user_id: int = None):
    """Добавить новый плейлист"""
    with Session(engine) as session:
        playlist = Playlist(
            title=title, 
            description=description, 
            cover_image_url=cover_image_url,
            created_date=created_date, 
            user_id=user_id
        )
        session.add(playlist)
        session.commit()
        session.refresh(playlist)
        print(f"Плейлист {title} добавлен с ID: {playlist.playlist_id}")
        return playlist



def delete_user(user_id: int):
    """Удалить пользователя по ID"""
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()
            print(f"Пользователь {user.username} удален")
            return True
        else:
            print(f"Пользователь с ID {user_id} не найден")
            return False

def delete_genre(genre_id: int):
    """Удалить жанр по ID"""
    with Session(engine) as session:
        genre = session.get(Genre, genre_id)
        if genre:
            session.delete(genre)
            session.commit()
            print(f"Жанр {genre.name} удален")
            return True
        else:
            print(f"Жанр с ID {genre_id} не найден")
            return False

def delete_artist(artist_id: int):
    """Удалить артиста по ID"""
    with Session(engine) as session:
        artist = session.get(Artist, artist_id)
        if artist:
            session.delete(artist)
            session.commit()
            print(f"Артист {artist.name} удален")
            return True
        else:
            print(f"Артист с ID {artist_id} не найден")
            return False

def delete_album(album_id: int):
    """Удалить альбом по ID"""
    with Session(engine) as session:
        album = session.get(Album, album_id)
        if album:
            session.delete(album)
            session.commit()
            print(f"Альбом {album.title} удален")
            return True
        else:
            print(f"Альбом с ID {album_id} не найден")
            return False

def delete_song(song_id: int):
    """Удалить песню по ID"""
    with Session(engine) as session:
        song = session.get(Song, song_id)
        if song:
            session.delete(song)
            session.commit()
            print(f"Песня {song.title} удалена")
            return True
        else:
            print(f"Песня с ID {song_id} не найдена")
            return False

def delete_playlist(playlist_id: int):
    """Удалить плейлист по ID"""
    with Session(engine) as session:
        playlist = session.get(Playlist, playlist_id)
        if playlist:
            session.delete(playlist)
            session.commit()
            print(f"Плейлист {playlist.title} удален")
            return True
        else:
            print(f"Плейлист с ID {playlist_id} не найден")
            return False


def update_user(user_id: int, **kwargs):
    """Обновить данные пользователя"""
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            session.add(user)
            session.commit()
            print(f"Пользователь {user.username} обновлен")
            return user
        else:
            print(f"Пользователь с ID {user_id} не найден")
            return None

def update_song(song_id: int, **kwargs):
    """Обновить данные песни"""
    with Session(engine) as session:
        song = session.get(Song, song_id)
        if song:
            for key, value in kwargs.items():
                if hasattr(song, key):
                    setattr(song, key, value)
            session.add(song)
            session.commit()
            print(f"Песня {song.title} обновлена")
            return song
        else:
            print(f"Песня с ID {song_id} не найдена")
            return None




def get_songs_by_genre(genre_name: str):
    """Получить песни по жанру"""
    with Session(engine) as session:
        statement = select(Song).join(Genre).where(Genre.name == genre_name)
        return session.exec(statement).all()

def get_albums_by_artist(artist_name: str):
    """Получить альбомы артиста"""
    with Session(engine) as session:
        statement = select(Album).join(Artist).where(Artist.name == artist_name)
        return session.exec(statement).all()

def get_playlists_by_user(user_id: int):
    """Получить плейлисты пользователя"""
    with Session(engine) as session:
        return session.exec(select(Playlist).where(Playlist.user_id == user_id)).all()

def get_user_by_username(username: str):
    """Получить пользователя по имени"""
    with Session(engine) as session:
        return session.exec(select(User).where(User.username == username)).first()


if __name__ == '__main__':
    create_db_and_tables()
    init_data()
    