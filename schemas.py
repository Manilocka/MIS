from typing import Optional
from sqlmodel import SQLModel


class UserCreate(SQLModel):
    email: str
    password: str
    username: str
    date_of_birth: Optional[str] = None
    country: Optional[str] = None
    registration_date: Optional[str] = None

class GenreCreate(SQLModel):
    name: str
    description: Optional[str] = None

class ArtistCreate(SQLModel):
    name: str
    bio: Optional[str] = None
    photo_url: Optional[str] = None
    genre_id: Optional[int] = None

class AlbumCreate(SQLModel):
    title: str
    cover_art_url: Optional[str] = None
    release_date: Optional[str] = None
    artist_id: Optional[int] = None

class SongCreate(SQLModel):
    title: str
    duration: int
    file_url: Optional[str] = None
    bitrate: Optional[int] = None
    release_date: Optional[str] = None
    album_id: Optional[int] = None
    genre_id: Optional[int] = None

class PlaylistCreate(SQLModel):
    title: str
    description: Optional[str] = None
    cover_image_url: Optional[str] = None
    created_date: Optional[str] = None
    user_id: Optional[int] = None
