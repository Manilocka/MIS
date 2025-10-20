from db_requests import DatabaseRequests
from datetime import datetime

def test_api():

    db = DatabaseRequests()

    print("\nПолучение всех пользователей:")
    try:
        users = db.get_all_users()
        print(f"Найдено пользователей: {len(users)}")
        for user in users[:3]:
            print(f"  - {user.username} ({user.email})")
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\nПолучение всех артистов:")
    try:
        artists = db.get_all_artists()
        print(f"Найдено артистов: {len(artists)}")
        for artist in artists:
            print(f"  - {artist.name}")
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\nПолучение всех песен:")
    try:
        songs = db.get_all_songs()
        print(f"Найдено песен: {len(songs)}")
        for song in songs:
            duration = f"{song.duration//60}:{song.duration%60:02d}"
            print(f"  - {song.title} ({duration})")
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\nПолучение всех жанров:")
    try:
        genres = db.get_all_genres()
        print(f"Найдено жанров: {len(genres)}")
        for genre in genres:
            print(f"  - {genre.name}: {genre.description}")
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\nПолучение песен по жанру (Pop):")
    try:
        genres = db.get_all_genres()
        pop_genre_id = None
        for genre in genres:
            if genre.name.lower() == 'pop':
                pop_genre_id = genre.genre_id
                break

        if pop_genre_id:
            songs = db.get_songs_by_genre(pop_genre_id)
            print(f"  Найдено песен в жанре Pop: {len(songs)}")
            for song in songs:
                print(f"    - {song.title}")
        else:
            print("  Жанр Pop не найден")
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\nПолучение альбомов артиста:")
    try:
        artists = db.get_all_artists()
        if artists:
            artist_id = artists[0].artist_id
            albums = db.get_albums_by_artist(artist_id)
            print(f"  Альбомы артиста {artists[0].name}: {len(albums)}")
            for album in albums:
                print(f"    - {album.title} ({album.release_date})")
        else:
            print("  Артисты не найдены")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    test_api()