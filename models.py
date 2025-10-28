# models.py
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, date

# Схема
SCHEMA = "Ragozina"

class Base(SQLModel):
    metadata = SQLModel.metadata
    metadata.schema = SCHEMA


# ==============================
# USER
# ==============================
class User(Base, table=True):
    __tablename__ = "users"

    user_id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True, nullable=False)
    password: str = Field(nullable=False)
    username: str = Field(nullable=False)
    date_of_birth: Optional[date] = None
    country: Optional[str] = None
    subscription_type: Optional[str] = None
    registration_date: datetime = Field(nullable=False)


# ==============================
# GENRE
# ==============================
class Genre(Base, table=True):
    __tablename__ = "genres"

    genre_id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True, nullable=False)
    description: Optional[str] = None


# ==============================
# ARTIST
# ==============================
class Artist(Base, table=True):
    __tablename__ = "artists"

    artist_id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    bio: Optional[str] = None
    photo_url: Optional[str] = None
    genre_id: Optional[int] = Field(default=None, foreign_key=f"{SCHEMA}.genres.genre_id")


# ==============================
# ALBUM
# ==============================
class Album(Base, table=True):
    __tablename__ = "albums"

    album_id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)
    cover_art_url: Optional[str] = None
    release_date: Optional[date] = None
    artist_id: Optional[int] = Field(default=None, foreign_key=f"{SCHEMA}.artists.artist_id")


# ==============================
# SONG
# ==============================
class Song(Base, table=True):
    __tablename__ = "songs"

    song_id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)
    duration: int = Field(nullable=False)
    file_url: str = Field(nullable=False)
    bitrate: Optional[int] = None
    release_date: Optional[date] = None
    artist_id: Optional[int] = Field(default=None, foreign_key=f"{SCHEMA}.artists.artist_id")
    album_id: Optional[int] = Field(default=None, foreign_key=f"{SCHEMA}.albums.album_id")
    genre_id: Optional[int] = Field(default=None, foreign_key=f"{SCHEMA}.genres.genre_id")


# ==============================
# PLAYLIST
# ==============================
class Playlist(Base, table=True):
    __tablename__ = "playlists"

    playlist_id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)
    description: Optional[str] = None
    cover_image_url: Optional[str] = None
    created_date: datetime = Field(nullable=False)
    user_id: Optional[int] = Field(default=None, foreign_key=f"{SCHEMA}.users.user_id")


# ==============================
# PLAYLIST_SONGS
# ==============================
class PlaylistSongs(Base, table=True):
    __tablename__ = "playlist_songs"

    playlist_id: int = Field(foreign_key=f"{SCHEMA}.playlists.playlist_id", primary_key=True)
    song_id: int = Field(foreign_key=f"{SCHEMA}.songs.song_id", primary_key=True)
    added_date: datetime = Field(nullable=False)


# ==============================
# SONG_ARTISTS
# ==============================
class SongArtists(Base, table=True):
    __tablename__ = "song_artists"

    song_id: int = Field(foreign_key=f"{SCHEMA}.songs.song_id", primary_key=True)
    artist_id: int = Field(foreign_key=f"{SCHEMA}.artists.artist_id", primary_key=True)


# ==============================
# USER_FOLLOWS
# ==============================
class UserFollows(Base, table=True):
    __tablename__ = "user_follows"

    user_id: int = Field(foreign_key=f"{SCHEMA}.users.user_id", primary_key=True)
    artist_id: int = Field(foreign_key=f"{SCHEMA}.artists.artist_id", primary_key=True)
    follow_date: datetime = Field(nullable=False)


# ==============================
# USER_LIKES
# ==============================
class UserLikes(Base, table=True):
    __tablename__ = "user_likes"

    user_id: int = Field(foreign_key=f"{SCHEMA}.users.user_id", primary_key=True)
    song_id: int = Field(foreign_key=f"{SCHEMA}.songs.song_id", primary_key=True)
    like_date: datetime = Field(nullable=False)


# ==============================
# LISTENING_HISTORY
# ==============================
class ListeningHistory(Base, table=True):
    __tablename__ = "listening_history"

    history_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key=f"{SCHEMA}.users.user_id")
    song_id: Optional[int] = Field(default=None, foreign_key=f"{SCHEMA}.songs.song_id")
    listen_date: datetime = Field(nullable=False)
    listen_duration: Optional[int] = None