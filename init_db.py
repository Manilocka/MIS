
from sqlmodel import SQLModel, create_engine, Session, select
from models import *
from db import init_data

def create_database():
    """Создание базы данных и таблиц"""
    print("Создание базы данных...")
    

    engine = create_engine("sqlite:///./music_db.sqlite")
    

    SQLModel.metadata.create_all(engine)
    print("Таблицы созданы")
    

    print("Заполнение тестовыми данными...")
    init_data()
    print("База данных готова к использованию")

def show_database_info():
    """Показать информацию о базе данных"""
    engine = create_engine("sqlite:///./music_db.sqlite")
    
    with Session(engine) as session:
        print("\nСтатистика базы данных:")
        print("-" * 30)
        

        tables = [
            ("Пользователи", User),
            ("Артисты", Artist),
            ("Песни", Song),
            ("Альбомы", Album),
            ("Плейлисты", Playlist),
            ("Жанры", Genre)
        ]
        
        for table_name, model in tables:
            count = len(session.exec(select(model)).all())
            print(f"{table_name:15}: {count:3} записей")
        
        print("-" * 30)
        print("Готово к работе!")

if __name__ == "__main__":

    
    try:
        create_database()
        show_database_info()
        
    except Exception as e:
        print(f"Ошибка инициализации: {e}")
