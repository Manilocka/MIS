import database_requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000"

def test_api():
    # 1. Получение всех пользователей
    print("\n1. Получение всех пользователей:")
    try:
        response = database_requests.get(f"{BASE_URL}/users")
        users = response.json()
        print(f"Найдено пользователей: {len(users)}")
        for user in users[:3]: 
            print(f"  - {user['username']} ({user['email']})")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    # 2. Получение всех артистов
    print("\n2. Получение всех артистов:")
    try:
        response = database_requests.get(f"{BASE_URL}/artists")
        artists = response.json()
        print(f"Найдено артистов: {len(artists)}")
        for artist in artists:
            print(f"  - {artist['name']}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    # 3. Получение всех песен
    print("\n3. Получение всех песен:")
    try:
        response = database_requests.get(f"{BASE_URL}/songs")
        songs = response.json()
        print(f"Найдено песен: {len(songs)}")
        for song in songs:
            duration = f"{song['duration']//60}:{song['duration']%60:02d}"
            print(f"  - {song['title']} ({duration})")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    # 4. Получение всех жанров
    print("\n4. Получение всех жанров:")
    try:
        response = database_requests.get(f"{BASE_URL}/genres")
        genres = response.json()
        print(f"Найдено жанров: {len(genres)}")
        for genre in genres:
            print(f"  - {genre['name']}: {genre['description']}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    # 5. Создание нового пользователя
    print("\n5. Создание нового пользователя:")
    try:
        new_user = {
            "email": "test@example.com",
            "password": "test123",
            "username": "testuser",
            "country": "Russia",
            "subscription_type": "free",
            "registration_date": datetime.now().isoformat().split('T')[0]
        }
        response = database_requests.post(f"{BASE_URL}/users", json=new_user)
        if response.status_code == 200:
            user = response.json()
            print(f"  Пользователь создан: {user['username']} (ID: {user['user_id']})")
        else:
            print(f"  Ошибка создания пользователя: {response.status_code}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    # 6. Создание нового жанра
    print("\n6. Создание нового жанра:")
    try:
        new_genre = {
            "name": "Rock",
            "description": "Rock music genre"
        }
        response = database_requests.post(f"{BASE_URL}/genres", json=new_genre)
        if response.status_code == 200:
            genre = response.json()
            print(f"  Жанр создан: {genre['name']} (ID: {genre['genre_id']})")
        else:
            print(f"  Ошибка создания жанра: {response.status_code}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    # 7. Получение песен по жанру
    print("\n7. Получение песен по жанру (Pop):")
    try:
        response = database_requests.get(f"{BASE_URL}/genres")
        genres = response.json()
        pop_genre_id = None
        for genre in genres:
            if genre['name'].lower() == 'pop':
                pop_genre_id = genre['genre_id']
                break
        
        if pop_genre_id:
            response = database_requests.get(f"{BASE_URL}/songs/genre/{pop_genre_id}")
            songs = response.json()
            print(f"  Найдено песен в жанре Pop: {len(songs)}")
            for song in songs:
                print(f"    - {song['title']}")
        else:
            print(" Жанр Pop не найден")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    # 8. Получение альбомов артиста
    print("\n8. Получение альбомов артиста:")
    try:
        response = database_requests.get(f"{BASE_URL}/artists")
        artists = response.json()
        if artists:
            artist_id = artists[0]['artist_id']
            response = database_requests.get(f"{BASE_URL}/albums/artist/{artist_id}")
            albums = response.json()
            print(f"  Альбомы артиста {artists[0]['name']}: {len(albums)}")
            for album in albums:
                print(f"    - {album['title']} ({album['release_date']})")
        else:
            print("  Артисты не найдены")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    test_api()