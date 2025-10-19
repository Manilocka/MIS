"""
Файл с запросами к базе данных для музыкальной системы
Использует SQLModel для работы с базой данных
"""

from sqlmodel import SQLModel, Session, select
from models import *
from typing import List, Optional
import json

from database import engine

class DatabaseRequests:
    """Класс для работы с запросами к базе данных"""
    
    def __init__(self):
        self.engine = engine

    
    def get_all_users(self) -> List[User]:
        """Получить всех пользователей"""
        with Session(self.engine) as session:
            return session.exec(select(User)).all()
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Получить пользователя по ID"""
        with Session(self.engine) as session:
            return session.get(User, user_id)
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Получить пользователя по email"""
        with Session(self.engine) as session:
            return session.exec(select(User).where(User.email == email)).first()
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        """Получить пользователя по имени"""
        with Session(self.engine) as session:
            return session.exec(select(User).where(User.username == username)).first()
    
    def create_user(self, user_data: dict) -> User:
        """Создать нового пользователя"""
        with Session(self.engine) as session:
            user = User(**user_data)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
    
    def update_user(self, user_id: int, user_data: dict) -> Optional[User]:
        """Обновить данные пользователя"""
        with Session(self.engine) as session:
            user = session.get(User, user_id)
            if user:
                for key, value in user_data.items():
                    if hasattr(user, key):
                        setattr(user, key, value)
                session.add(user)
                session.commit()
                session.refresh(user)
                return user
            return None
    
    def delete_user(self, user_id: int) -> bool:
        """Удалить пользователя"""
        with Session(self.engine) as session:
            user = session.get(User, user_id)
            if user:
                session.delete(user)
                session.commit()
                return True
            return False
    

    
    def get_all_genres(self) -> List[Genre]:
        """Получить все жанры"""
        with Session(self.engine) as session:
            return session.exec(select(Genre)).all()
    
    def get_genre_by_id(self, genre_id: int) -> Optional[Genre]:
        """Получить жанр по ID"""
        with Session(self.engine) as session:
            return session.get(Genre, genre_id)
    
    def create_genre(self, genre_data: dict) -> Genre:
        """Создать новый жанр"""
        with Session(self.engine) as session:
            genre = Genre(**genre_data)
            session.add(genre)
            session.commit()
            session.refresh(genre)
            return genre
    
    def delete_genre(self, genre_id: int) -> bool:
        """Удалить жанр"""
        with Session(self.engine) as session:
            genre = session.get(Genre, genre_id)
            if genre:
                session.delete(genre)
                session.commit()
                return True
            return False
    

    
    def get_all_artists(self) -> List[Artist]:
        """Получить всех артистов"""
        with Session(self.engine) as session:
            return session.exec(select(Artist)).all()
    
    def get_artist_by_id(self, artist_id: int) -> Optional[Artist]:
        """Получить артиста по ID"""
        with Session(self.engine) as session:
            return session.get(Artist, artist_id)
    
    def get_artists_by_genre(self, genre_id: int) -> List[Artist]:
        """Получить артистов по жанру"""
        with Session(self.engine) as session:
            return session.exec(select(Artist).where(Artist.genre_id == genre_id)).all()
    
    def create_artist(self, artist_data: dict) -> Artist:
        """Создать нового артиста"""
        with Session(self.engine) as session:
            artist = Artist(**artist_data)
            session.add(artist)
            session.commit()
            session.refresh(artist)
            return artist
    
    def delete_artist(self, artist_id: int) -> bool:
        """Удалить артиста"""
        with Session(self.engine) as session:
            artist = session.get(Artist, artist_id)
            if artist:
                session.delete(artist)
                session.commit()
                return True
            return False
    

    
    def get_all_albums(self) -> List[Album]:
        """Получить все альбомы"""
        with Session(self.engine) as session:
            return session.exec(select(Album)).all()
    
    def get_album_by_id(self, album_id: int) -> Optional[Album]:
        """Получить альбом по ID"""
        with Session(self.engine) as session:
            return session.get(Album, album_id)
    
    def get_albums_by_artist(self, artist_id: int) -> List[Album]:
        """Получить альбомы артиста"""
        with Session(self.engine) as session:
            return session.exec(select(Album).where(Album.artist_id == artist_id)).all()
    
    def create_album(self, album_data: dict) -> Album:
        """Создать новый альбом"""
        with Session(self.engine) as session:
            album = Album(**album_data)
            session.add(album)
            session.commit()
            session.refresh(album)
            return album
    
    def delete_album(self, album_id: int) -> bool:
        """Удалить альбом"""
        with Session(self.engine) as session:
            album = session.get(Album, album_id)
            if album:
                session.delete(album)
                session.commit()
                return True
            return False
    

    
    def get_all_songs(self) -> List[Song]:
        """Получить все песни"""
        with Session(self.engine) as session:
            return session.exec(select(Song)).all()
    
    def get_song_by_id(self, song_id: int) -> Optional[Song]:
        """Получить песню по ID"""
        with Session(self.engine) as session:
            return session.get(Song, song_id)
    
    def get_songs_by_artist(self, artist_id: int) -> List[Song]:
        """Получить песни артиста"""
        with Session(self.engine) as session:
            statement = select(Song).join(Album).where(Album.artist_id == artist_id)
            return session.exec(statement).all()
    
    def get_songs_by_genre(self, genre_id: int) -> List[Song]:
        """Получить песни по жанру"""
        with Session(self.engine) as session:
            return session.exec(select(Song).where(Song.genre_id == genre_id)).all()
    
    def get_songs_by_album(self, album_id: int) -> List[Song]:
        """Получить песни альбома"""
        with Session(self.engine) as session:
            return session.exec(select(Song).where(Song.album_id == album_id)).all()
    
    def create_song(self, song_data: dict) -> Song:
        """Создать новую песню"""
        with Session(self.engine) as session:
            song = Song(**song_data)
            session.add(song)
            session.commit()
            session.refresh(song)
            return song
    
    def update_song(self, song_id: int, song_data: dict) -> Optional[Song]:
        """Обновить данные песни"""
        with Session(self.engine) as session:
            song = session.get(Song, song_id)
            if song:
                for key, value in song_data.items():
                    if hasattr(song, key):
                        setattr(song, key, value)
                session.add(song)
                session.commit()
                session.refresh(song)
                return song
            return None
    
    def delete_song(self, song_id: int) -> bool:
        """Удалить песню"""
        with Session(self.engine) as session:
            song = session.get(Song, song_id)
            if song:
                session.delete(song)
                session.commit()
                return True
            return False
    

    
    def get_all_playlists(self) -> List[Playlist]:
        """Получить все плейлисты"""
        with Session(self.engine) as session:
            return session.exec(select(Playlist)).all()
    
    def get_playlist_by_id(self, playlist_id: int) -> Optional[Playlist]:
        """Получить плейлист по ID"""
        with Session(self.engine) as session:
            return session.get(Playlist, playlist_id)
    
    def get_playlists_by_user(self, user_id: int) -> List[Playlist]:
        """Получить плейлисты пользователя"""
        with Session(self.engine) as session:
            return session.exec(select(Playlist).where(Playlist.user_id == user_id)).all()
    
    def create_playlist(self, playlist_data: dict) -> Playlist:
        """Создать новый плейлист"""
        with Session(self.engine) as session:
            playlist = Playlist(**playlist_data)
            session.add(playlist)
            session.commit()
            session.refresh(playlist)
            return playlist
    
    def delete_playlist(self, playlist_id: int) -> bool:
        """Удалить плейлист"""
        with Session(self.engine) as session:
            playlist = session.get(Playlist, playlist_id)
            if playlist:
                session.delete(playlist)
                session.commit()
                return True
            return False
    

    
    def add_song_to_playlist(self, playlist_id: int, song_id: int, added_date: str = None) -> bool:
        """Добавить песню в плейлист"""
        with Session(self.engine) as session:
            playlist_song = PlaylistSongs(
                playlist_id=playlist_id,
                song_id=song_id,
                added_date=added_date
            )
            session.add(playlist_song)
            session.commit()
            return True
    
    def remove_song_from_playlist(self, playlist_id: int, song_id: int) -> bool:
        """Удалить песню из плейлиста"""
        with Session(self.engine) as session:
            playlist_song = session.exec(
                select(PlaylistSongs).where(
                    PlaylistSongs.playlist_id == playlist_id,
                    PlaylistSongs.song_id == song_id
                )
            ).first()
            if playlist_song:
                session.delete(playlist_song)
                session.commit()
                return True
            return False
    
    def get_playlist_songs(self, playlist_id: int) -> List[Song]:
        """Получить песни плейлиста"""
        with Session(self.engine) as session:
            statement = select(Song).join(PlaylistSongs).where(PlaylistSongs.playlist_id == playlist_id)
            return session.exec(statement).all()
    

    
    def add_listening_history(self, user_id: int, song_id: int, listen_date: str = None, listen_duration: int = None) -> bool:
        """Добавить запись в историю прослушивания"""
        with Session(self.engine) as session:
            history = ListeningHistory(
                user_id=user_id,
                song_id=song_id,
                listen_date=listen_date,
                listen_duration=listen_duration
            )
            session.add(history)
            session.commit()
            return True
    
    def get_user_listening_history(self, user_id: int) -> List[ListeningHistory]:
        """Получить историю прослушивания пользователя"""
        with Session(self.engine) as session:
            return session.exec(select(ListeningHistory).where(ListeningHistory.user_id == user_id)).all()
    

    
    def add_user_like(self, user_id: int, song_id: int, like_date: str = None) -> bool:
        """Добавить лайк пользователя к песне"""
        with Session(self.engine) as session:
            like = UserLikes(
                user_id=user_id,
                song_id=song_id,
                like_date=like_date
            )
            session.add(like)
            session.commit()
            return True
    
    def remove_user_like(self, user_id: int, song_id: int) -> bool:
        """Удалить лайк пользователя к песне"""
        with Session(self.engine) as session:
            like = session.exec(
                select(UserLikes).where(
                    UserLikes.user_id == user_id,
                    UserLikes.song_id == song_id
                )
            ).first()
            if like:
                session.delete(like)
                session.commit()
                return True
            return False
    
    def get_user_likes(self, user_id: int) -> List[Song]:
        """Получить лайкнутые песни пользователя"""
        with Session(self.engine) as session:
            statement = select(Song).join(UserLikes).where(UserLikes.user_id == user_id)
            return session.exec(statement).all()
    

    
    def follow_artist(self, user_id: int, artist_id: int, follow_date: str = None) -> bool:
        """Подписаться на артиста"""
        with Session(self.engine) as session:
            follow = UserFollows(
                user_id=user_id,
                artist_id=artist_id,
                follow_date=follow_date
            )
            session.add(follow)
            session.commit()
            return True
    
    def unfollow_artist(self, user_id: int, artist_id: int) -> bool:
        """Отписаться от артиста"""
        with Session(self.engine) as session:
            follow = session.exec(
                select(UserFollows).where(
                    UserFollows.user_id == user_id,
                    UserFollows.artist_id == artist_id
                )
            ).first()
            if follow:
                session.delete(follow)
                session.commit()
                return True
            return False
    
    def get_user_follows(self, user_id: int) -> List[Artist]:
        """Получить артистов, на которых подписан пользователь"""
        with Session(self.engine) as session:
            statement = select(Artist).join(UserFollows).where(UserFollows.user_id == user_id)
            return session.exec(statement).all()
