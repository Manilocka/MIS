"""
Примеры использования API музыкальной системы
Демонстрирует основные операции с базой данных через API
"""

import requests
import json
from datetime import datetime

# Базовый URL API
BASE_URL = "http://localhost:8000"

def test_api():
    """Тестирование основных функций API"""
    
    print("🎵 Тестирование API музыкальной системы")
    print("=" * 50)
    
    # 1. Получение всех пользователей
    print("\n1. Получение всех пользователей:")
    try:
        response = requests.get(f"{BASE_URL}/users")
        users = response.json()
        print(f"Найдено пользователей: {len(users)}")
        for user in users[:3]:  # Показываем первых 3
            print(f"  - {user['username']} ({user['email']})")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    # 2. Получение всех артистов
    print("\n2. Получение всех артистов:")
    try:
        response = requests.get(f"{BASE_URL}/artists")
        artists = response.json()
        print(f"Найдено артистов: {len(artists)}")
        for artist in artists:
            print(f"  - {artist['name']}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    # 3. Получение всех песен
    print("\n3. Получение всех песен:")
    try:
        response = requests.get(f"{BASE_URL}/songs")
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
        response = requests.get(f"{BASE_URL}/genres")
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
        response = requests.post(f"{BASE_URL}/users", json=new_user)
        if response.status_code == 200:
            user = response.json()
            print(f"  ✅ Пользователь создан: {user['username']} (ID: {user['user_id']})")
        else:
            print(f"  ❌ Ошибка создания пользователя: {response.status_code}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    # 6. Создание нового жанра
    print("\n6. Создание нового жанра:")
    try:
        new_genre = {
            "name": "Rock",
            "description": "Rock music genre"
        }
        response = requests.post(f"{BASE_URL}/genres", json=new_genre)
        if response.status_code == 200:
            genre = response.json()
            print(f"  ✅ Жанр создан: {genre['name']} (ID: {genre['genre_id']})")
        else:
            print(f"  ❌ Ошибка создания жанра: {response.status_code}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    # 7. Получение песен по жанру
    print("\n7. Получение песен по жанру (Pop):")
    try:
        # Сначала найдем ID жанра Pop
        response = requests.get(f"{BASE_URL}/genres")
        genres = response.json()
        pop_genre_id = None
        for genre in genres:
            if genre['name'].lower() == 'pop':
                pop_genre_id = genre['genre_id']
                break
        
        if pop_genre_id:
            response = requests.get(f"{BASE_URL}/songs/genre/{pop_genre_id}")
            songs = response.json()
            print(f"  Найдено песен в жанре Pop: {len(songs)}")
            for song in songs:
                print(f"    - {song['title']}")
        else:
            print("  Жанр Pop не найден")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    # 8. Получение альбомов артиста
    print("\n8. Получение альбомов артиста:")
    try:
        # Сначала найдем ID артиста
        response = requests.get(f"{BASE_URL}/artists")
        artists = response.json()
        if artists:
            artist_id = artists[0]['artist_id']
            response = requests.get(f"{BASE_URL}/albums/artist/{artist_id}")
            albums = response.json()
            print(f"  Альбомы артиста {artists[0]['name']}: {len(albums)}")
            for album in albums:
                print(f"    - {album['title']} ({album['release_date']})")
        else:
            print("  Артисты не найдены")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\n" + "=" * 50)
    print("✅ Тестирование завершено!")
    print(f"🌐 Веб-интерфейс доступен по адресу: {BASE_URL}")
    print(f"📚 API документация: {BASE_URL}/docs")

def create_sample_data():
    """Создание примеров данных для демонстрации"""
    
    print("\n🎯 Создание примеров данных...")
    
    # Создание жанра
    try:
        genre_data = {
            "name": "Electronic",
            "description": "Electronic music"
        }
        response = requests.post(f"{BASE_URL}/genres", json=genre_data)
        if response.status_code == 200:
            print("✅ Жанр Electronic создан")
    except:
        pass
    
    # Создание пользователя
    try:
        user_data = {
            "email": "demo@example.com",
            "password": "demo123",
            "username": "demouser",
            "country": "Russia",
            "subscription_type": "premium",
            "registration_date": "2025-01-01"
        }
        response = requests.post(f"{BASE_URL}/users", json=user_data)
        if response.status_code == 200:
            print("✅ Пользователь demouser создан")
    except:
        pass

if __name__ == "__main__":
    print("Запуск примеров использования API...")
    print("Убедитесь, что сервер запущен на http://localhost:8000")
    print()
    
    try:
        # Проверяем доступность сервера
        response = requests.get(f"{BASE_URL}/users")
        if response.status_code == 200:
            test_api()
            create_sample_data()
        else:
            print("❌ Сервер недоступен. Запустите приложение командой: python main.py")
    except requests.exceptions.ConnectionError:
        print("❌ Не удается подключиться к серверу.")
        print("   Убедитесь, что приложение запущено: python main.py")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
