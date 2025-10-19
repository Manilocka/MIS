from sqlmodel import Field, SQLModel


# Note: engine is defined in `database.py`

# class Base(SQLModel, table=False):
#     __table_args__ = {"schema": "karma"}
class User(SQLModel, table=True):
    __tablename__ = "users"
    user_id: int = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    password: str
    username: str
    date_of_birth: str = Field(default=None)
    country: str = Field(default=None)
    registration_date: str = Field(default=None)


class Genre(SQLModel, table=True):
    __tablename__ = "genres"
    genre_id: int = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    description: str = Field(default=None)


class Artist(SQLModel, table=True):
    __tablename__ = "artists"
    artist_id: int = Field(default=None, primary_key=True)
    name: str
    bio: str = Field(default=None)
    photo_url: str = Field(default=None)
    genre_id: int = Field(default=None, foreign_key="genres.genre_id")


class Album(SQLModel, table=True):
    __tablename__ = "albums"
    album_id: int = Field(default=None, primary_key=True)
    title: str
    cover_art_url: str = Field(default=None)
    release_date: str = Field(default=None)
    artist_id: int = Field(default=None, foreign_key="artists.artist_id")


class Song(SQLModel, table=True):
    __tablename__ = "songs"
    song_id: int = Field(default=None, primary_key=True)
    title: str
    duration: int
    file_url: str
    bitrate: int = Field(default=None)
    release_date: str = Field(default=None)
    album_id: int = Field(default=None, foreign_key="albums.album_id")
    genre_id: int = Field(default=None, foreign_key="genres.genre_id")


class Playlist(SQLModel, table=True):
    __tablename__ = "playlists"
    playlist_id: int = Field(default=None, primary_key=True)
    title: str
    description: str = Field(default=None)
    cover_image_url: str = Field(default=None)
    created_date: str = Field(default=None)
    user_id: int = Field(default=None, foreign_key="users.user_id")


class PlaylistSongs(SQLModel, table=True):
    __tablename__ = "playlist_songs"
    playlist_id: int = Field(foreign_key="playlists.playlist_id", primary_key=True)
    song_id: int = Field(foreign_key="songs.song_id", primary_key=True)
    added_date: str = Field(default=None)


class SongArtists(SQLModel, table=True):
    __tablename__ = "song_artists"
    song_id: int = Field(foreign_key="songs.song_id", primary_key=True)
    artist_id: int = Field(foreign_key="artists.artist_id", primary_key=True)


class UserFollows(SQLModel, table=True):
    __tablename__ = "user_follows"
    user_id: int = Field(foreign_key="users.user_id", primary_key=True)
    artist_id: int = Field(foreign_key="artists.artist_id", primary_key=True)
    follow_date: str = Field(default=None)


class UserLikes(SQLModel, table=True):
    __tablename__ = "user_likes"
    user_id: int = Field(foreign_key="users.user_id", primary_key=True)
    song_id: int = Field(foreign_key="songs.song_id", primary_key=True)
    like_date: str = Field(default=None)


class ListeningHistory(SQLModel, table=True):
    __tablename__ = "listening_history"
    history_id: int = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="users.user_id")
    song_id: int = Field(default=None, foreign_key="songs.song_id")
    listen_date: str = Field(default=None)
    listen_duration: int = Field(default=None)