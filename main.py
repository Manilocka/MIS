
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlmodel import SQLModel, create_engine, Session, select
from typing import List
import uvicorn
from datetime import datetime

from db_requests import engine

from models import *
from db_requests import DatabaseRequests


app = FastAPI(
    title="Музыкальная система API",
    description="API для управления музыкальной базой данных",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


SQLModel.metadata.create_all(engine)


db_requests = DatabaseRequests()



def get_session():
    """Получить сессию базы данных"""
    with Session(engine) as session:
        yield session



@app.get("/users", response_model=List[User])
async def get_all_users():
    """Получить всех пользователей"""
    return db_requests.get_all_users()

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """Получить пользователя по ID"""
    user = db_requests.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user

@app.get("/users/email/{email}", response_model=User)
async def get_user_by_email(email: str):
    """Получить пользователя по email"""
    user = db_requests.get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user

@app.post("/users", response_model=User)
async def create_user(user: User):
    """Создать нового пользователя"""
    return db_requests.create_user(user.dict())

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    """Обновить данные пользователя"""
    updated_user = db_requests.update_user(user_id, user.dict())
    if not updated_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return updated_user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    """Удалить пользователя"""
    success = db_requests.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return {"message": "Пользователь удален"}



@app.get("/genres", response_model=List[Genre])
async def get_all_genres():
    """Получить все жанры"""
    return db_requests.get_all_genres()

@app.get("/genres/{genre_id}", response_model=Genre)
async def get_genre(genre_id: int):
    """Получить жанр по ID"""
    genre = db_requests.get_genre_by_id(genre_id)
    if not genre:
        raise HTTPException(status_code=404, detail="Жанр не найден")
    return genre

@app.post("/genres", response_model=Genre)
async def create_genre(genre: Genre):
    """Создать новый жанр"""
    return db_requests.create_genre(genre.dict())

@app.delete("/genres/{genre_id}")
async def delete_genre(genre_id: int):
    """Удалить жанр"""
    success = db_requests.delete_genre(genre_id)
    if not success:
        raise HTTPException(status_code=404, detail="Жанр не найден")
    return {"message": "Жанр удален"}



@app.get("/artists", response_model=List[Artist])
async def get_all_artists():
    """Получить всех артистов"""
    return db_requests.get_all_artists()

@app.get("/artists/{artist_id}", response_model=Artist)
async def get_artist(artist_id: int):
    """Получить артиста по ID"""
    artist = db_requests.get_artist_by_id(artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Артист не найден")
    return artist

@app.get("/artists/genre/{genre_id}", response_model=List[Artist])
async def get_artists_by_genre(genre_id: int):
    """Получить артистов по жанру"""
    return db_requests.get_artists_by_genre(genre_id)

@app.post("/artists", response_model=Artist)
async def create_artist(artist: Artist):
    """Создать нового артиста"""
    return db_requests.create_artist(artist.dict())

@app.delete("/artists/{artist_id}")
async def delete_artist(artist_id: int):
    """Удалить артиста"""
    success = db_requests.delete_artist(artist_id)
    if not success:
        raise HTTPException(status_code=404, detail="Артист не найден")
    return {"message": "Артист удален"}



@app.get("/albums", response_model=List[Album])
async def get_all_albums():
    """Получить все альбомы"""
    return db_requests.get_all_albums()

@app.get("/albums/{album_id}", response_model=Album)
async def get_album(album_id: int):
    """Получить альбом по ID"""
    album = db_requests.get_album_by_id(album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Альбом не найден")
    return album

@app.get("/albums/artist/{artist_id}", response_model=List[Album])
async def get_albums_by_artist(artist_id: int):
    """Получить альбомы артиста"""
    return db_requests.get_albums_by_artist(artist_id)

@app.post("/albums", response_model=Album)
async def create_album(album: Album):
    """Создать новый альбом"""
    return db_requests.create_album(album.dict())

@app.delete("/albums/{album_id}")
async def delete_album(album_id: int):
    """Удалить альбом"""
    success = db_requests.delete_album(album_id)
    if not success:
        raise HTTPException(status_code=404, detail="Альбом не найден")
    return {"message": "Альбом удален"}



@app.get("/songs", response_model=List[Song])
async def get_all_songs():
    """Получить все песни"""
    return db_requests.get_all_songs()

@app.get("/songs/{song_id}", response_model=Song)
async def get_song(song_id: int):
    """Получить песню по ID"""
    song = db_requests.get_song_by_id(song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Песня не найдена")
    return song

@app.get("/songs/artist/{artist_id}", response_model=List[Song])
async def get_songs_by_artist(artist_id: int):
    """Получить песни артиста"""
    return db_requests.get_songs_by_artist(artist_id)

@app.get("/songs/genre/{genre_id}", response_model=List[Song])
async def get_songs_by_genre(genre_id: int):
    """Получить песни по жанру"""
    return db_requests.get_songs_by_genre(genre_id)

@app.get("/songs/album/{album_id}", response_model=List[Song])
async def get_songs_by_album(album_id: int):
    """Получить песни альбома"""
    return db_requests.get_songs_by_album(album_id)

@app.post("/songs", response_model=Song)
async def create_song(song: Song):
    """Создать новую песню"""
    return db_requests.create_song(song.dict())

@app.put("/songs/{song_id}", response_model=Song)
async def update_song(song_id: int, song: Song):
    """Обновить данные песни"""
    updated_song = db_requests.update_song(song_id, song.dict())
    if not updated_song:
        raise HTTPException(status_code=404, detail="Песня не найдена")
    return updated_song

@app.delete("/songs/{song_id}")
async def delete_song(song_id: int):
    """Удалить песню"""
    success = db_requests.delete_song(song_id)
    if not success:
        raise HTTPException(status_code=404, detail="Песня не найдена")
    return {"message": "Песня удалена"}



@app.get("/playlists", response_model=List[Playlist])
async def get_all_playlists():
    """Получить все плейлисты"""
    return db_requests.get_all_playlists()

@app.get("/playlists/{playlist_id}", response_model=Playlist)
async def get_playlist(playlist_id: int):
    """Получить плейлист по ID"""
    playlist = db_requests.get_playlist_by_id(playlist_id)
    if not playlist:
        raise HTTPException(status_code=404, detail="Плейлист не найден")
    return playlist

@app.get("/playlists/user/{user_id}", response_model=List[Playlist])
async def get_playlists_by_user(user_id: int):
    """Получить плейлисты пользователя"""
    return db_requests.get_playlists_by_user(user_id)

@app.post("/playlists", response_model=Playlist)
async def create_playlist(playlist: Playlist):
    """Создать новый плейлист"""
    return db_requests.create_playlist(playlist.dict())

@app.delete("/playlists/{playlist_id}")
async def delete_playlist(playlist_id: int):
    """Удалить плейлист"""
    success = db_requests.delete_playlist(playlist_id)
    if not success:
        raise HTTPException(status_code=404, detail="Плейлист не найден")
    return {"message": "Плейлист удален"}



@app.post("/playlists/{playlist_id}/songs/{song_id}")
async def add_song_to_playlist(playlist_id: int, song_id: int):
    """Добавить песню в плейлист"""
    success = db_requests.add_song_to_playlist(playlist_id, song_id, datetime.now().isoformat())
    if not success:
        raise HTTPException(status_code=400, detail="Не удалось добавить песню в плейлист")
    return {"message": "Песня добавлена в плейлист"}

@app.delete("/playlists/{playlist_id}/songs/{song_id}")
async def remove_song_from_playlist(playlist_id: int, song_id: int):
    """Удалить песню из плейлиста"""
    success = db_requests.remove_song_from_playlist(playlist_id, song_id)
    if not success:
        raise HTTPException(status_code=400, detail="Не удалось удалить песню из плейлиста")
    return {"message": "Песня удалена из плейлиста"}

@app.get("/playlists/{playlist_id}/songs", response_model=List[Song])
async def get_playlist_songs(playlist_id: int):
    """Получить песни плейлиста"""
    return db_requests.get_playlist_songs(playlist_id)



@app.post("/users/{user_id}/listen/{song_id}")
async def add_listening_history(user_id: int, song_id: int, duration: int = None):
    """Добавить запись в историю прослушивания"""
    success = db_requests.add_listening_history(
        user_id, song_id, 
        datetime.now().isoformat(), 
        duration
    )
    if not success:
        raise HTTPException(status_code=400, detail="Не удалось добавить запись в историю")
    return {"message": "Запись добавлена в историю"}

@app.get("/users/{user_id}/history", response_model=List[ListeningHistory])
async def get_user_listening_history(user_id: int):
    """Получить историю прослушивания пользователя"""
    return db_requests.get_user_listening_history(user_id)



@app.post("/users/{user_id}/like/{song_id}")
async def add_user_like(user_id: int, song_id: int):
    """Добавить лайк пользователя к песне"""
    success = db_requests.add_user_like(user_id, song_id, datetime.now().isoformat())
    if not success:
        raise HTTPException(status_code=400, detail="Не удалось добавить лайк")
    return {"message": "Лайк добавлен"}

@app.delete("/users/{user_id}/like/{song_id}")
async def remove_user_like(user_id: int, song_id: int):
    """Удалить лайк пользователя к песне"""
    success = db_requests.remove_user_like(user_id, song_id)
    if not success:
        raise HTTPException(status_code=400, detail="Не удалось удалить лайк")
    return {"message": "Лайк удален"}

@app.get("/users/{user_id}/likes", response_model=List[Song])
async def get_user_likes(user_id: int):
    """Получить лайкнутые песни пользователя"""
    return db_requests.get_user_likes(user_id)



@app.post("/users/{user_id}/follow/{artist_id}")
async def follow_artist(user_id: int, artist_id: int):
    """Подписаться на артиста"""
    success = db_requests.follow_artist(user_id, artist_id, datetime.now().isoformat())
    if not success:
        raise HTTPException(status_code=400, detail="Не удалось подписаться на артиста")
    return {"message": "Подписка добавлена"}

@app.delete("/users/{user_id}/follow/{artist_id}")
async def unfollow_artist(user_id: int, artist_id: int):
    """Отписаться от артиста"""
    success = db_requests.unfollow_artist(user_id, artist_id)
    if not success:
        raise HTTPException(status_code=400, detail="Не удалось отписаться от артиста")
    return {"message": "Подписка удалена"}

@app.get("/users/{user_id}/follows", response_model=List[Artist])
async def get_user_follows(user_id: int):
    """Получить артистов, на которых подписан пользователь"""
    return db_requests.get_user_follows(user_id)




app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Главная страница с интерфейсом"""
    with open("static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())



if __name__ == "__main__":

    db_requests.init_data() 
    uvicorn.run(app, host="0.0.0.0", port=8000)
