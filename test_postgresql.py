# Тест подключения к PostgreSQL
# Этот файл можно использовать для проверки подключения к PostgreSQL

from sqlmodel import create_engine, SQLModel, Session, select

# Подключение к PostgreSQL (замените на ваши данные)
# engine = create_engine('postgresql://postgresql:{DB_PASSWORD}@localhost:5432/{DB_NAME}')

# Пример с локальным PostgreSQL (если установлен)
# engine = create_engine('postgresql://postgres:password@localhost:5432/music_db')

def test_connection():
    """Тестирует подключение к PostgreSQL"""
    try:
        # Создаем подключение
        with engine.connect() as conn:
            print("✅ Подключение к PostgreSQL успешно!")
            
            # Выполняем простой запрос
            result = conn.execute("SELECT version();")
            version = result.fetchone()
            print(f"📊 Версия PostgreSQL: {version[0]}")
            
        return True
    except Exception as e:
        print(f"❌ Ошибка подключения к PostgreSQL: {e}")
        return False

def test_sqlmodel():
    """Тестирует работу SQLModel с PostgreSQL"""
    try:
        # Создаем таблицы
        SQLModel.metadata.create_all(engine)
        print("✅ Таблицы созданы успешно!")
        
        # Тестируем сессию
        with Session(engine) as session:
            print("✅ Сессия SQLModel работает!")
            
        return True
    except Exception as e:
        print(f"❌ Ошибка SQLModel: {e}")
        return False

if __name__ == "__main__":
    print("🔧 Тестирование PostgreSQL подключения...")
    print("⚠️  Раскомментируйте строку с engine для тестирования")
    print("📝 Пример: engine = create_engine('postgresql://user:password@localhost:5432/dbname')")
