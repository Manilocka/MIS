from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    user_id: int = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    password: str
    username: str
    date_of_birth: str = None
    country: str = None
    subscription_type: str = None
    registration_date: str = None

class Genre(SQLModel, table=True):
    genre_id: int = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    description: str = None

class Artist(SQLModel, table=True):
    artist_id: int = Field(default=None, primary_key=True)
    name: str
    bio: str = None
    photo_url: str = None
    genre_id: int = Field(default=None, foreign_key="genres.genre_id")

class Album(SQLModel, table=True):
    album_id: int = Field(default=None, primary_key=True)
    title: str
    cover_art_url: str = None
    release_date: str = None
    artist_id: int = Field(default=None, foreign_key="artists.artist_id")

class Song(SQLModel, table=True):
    song_id: int = Field(default=None, primary_key=True)
    title: str
    duration: int
    file_url: str
    bitrate: int = None
    release_date: str = None
    album_id: int = Field(default=None, foreign_key="albums.album_id")
    genre_id: int = Field(default=None, foreign_key="genres.genre_id")

class Playlist(SQLModel, table=True):
    playlist_id: int = Field(default=None, primary_key=True)
    title: str
    description: str = None
    cover_image_url: str = None
    created_date: str = None
    user_id: int = Field(default=None, foreign_key="users.user_id")

class PlaylistSongs(SQLModel, table=True):
    playlist_id: int = Field(foreign_key="playlists.playlist_id", primary_key=True)
    song_id: int = Field(foreign_key="songs.song_id", primary_key=True)
    added_date: str = None

class SongArtists(SQLModel, table=True):
    song_id: int = Field(foreign_key="songs.song_id", primary_key=True)
    artist_id: int = Field(foreign_key="artists.artist_id", primary_key=True)

class UserFollows(SQLModel, table=True):
    user_id: int = Field(foreign_key="users.user_id", primary_key=True)
    artist_id: int = Field(foreign_key="artists.artist_id", primary_key=True)
    follow_date: str = None

class UserLikes(SQLModel, table=True):
    user_id: int = Field(foreign_key="users.user_id", primary_key=True)
    song_id: int = Field(foreign_key="songs.song_id", primary_key=True)
    like_date: str = None

class ListeningHistory(SQLModel, table=True):
    history_id: int = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="users.user_id")
    song_id: int = Field(default=None, foreign_key="songs.song_id")
    listen_date: str = None
    listen_duration: int = None