## Туториал по установке этого софта

1. Клонировать репозиторий
```git clone https://github.com/Manilocka/MIS.git```

2. Прописать в терминал ```pip install -r requirements.txt``` 

3. В терминал прописать  
```uvicorn main:app --reload --host 0.0.0.0 --port 8000```
 для запуска приложения

4. Приложение запустится на указанном ранее порте (8000) по адресу ```http://localhost:8000/```

4. ```http://localhost:8000/docs``` ссылка на swagger ui