import pytest
from db_requests import DatabaseRequests


@pytest.fixture(scope="module")
def db():
    """Fixture that provides a DatabaseRequests instance for tests."""
    return DatabaseRequests()


def test_get_all_users_returns_list(db):
    users = db.get_all_users()
    assert isinstance(users, list)


def test_get_all_artists_returns_list_and_has_name(db):
    artists = db.get_all_artists()
    assert isinstance(artists, list)
    if artists:
        assert hasattr(artists[0], "name")


def test_get_all_songs_returns_list_and_duration_ok(db):
    songs = db.get_all_songs()
    assert isinstance(songs, list)
    for song in songs:
        assert hasattr(song, "title")
        # duration should be an integer number of seconds (non-negative)
        assert hasattr(song, "duration")
        assert isinstance(song.duration, int)
        assert song.duration >= 0


def test_get_all_genres_returns_list_and_description(db):
    genres = db.get_all_genres()
    assert isinstance(genres, list)
    if genres:
        assert hasattr(genres[0], "name")
        assert hasattr(genres[0], "description")


def test_get_songs_by_genre_pop(db):
    # Find Pop genre if present; otherwise skip the test
    genres = db.get_all_genres()
    pop_genre = None
    for g in genres:
        if getattr(g, "name", "").lower() == "pop":
            pop_genre = g
            break

    if not pop_genre:
        pytest.skip("Pop genre not found in the database")

    songs = db.get_songs_by_genre(pop_genre.genre_id)
    assert isinstance(songs, list)


def test_get_albums_by_first_artist(db):
    artists = db.get_all_artists()
    if not artists:
        pytest.skip("No artists in DB to test albums retrieval")

    first = artists[0]
    albums = db.get_albums_by_artist(first.artist_id)
    assert isinstance(albums, list)


def test_expected_song_titles_for_known_artists(db):
    """Check that expected mappings (if artist exists) have at least one matching song."""
    artists = db.get_all_artists()
    songs = db.get_all_songs()
    artist_by_name = {a.name: a for a in artists}

    expected = {
        "Luka": "Ruler of my heart",
        "Hyuona": "All in",
        "Ivan": "Paratise",
    }

    for artist_name, expected_title in expected.items():
        artist = artist_by_name.get(artist_name)
        if not artist:
            # If the artist isn't present in the DB, skip this particular check
            continue

        matches = [s for s in songs if s.artist_id == artist.artist_id and s.title == expected_title]
        assert matches, f"Expected song '{expected_title}' for artist '{artist_name}' not found"
