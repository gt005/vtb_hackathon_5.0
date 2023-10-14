Для запуска бэкенда, требуется:
```
docker-compose up backend --build
```

Чтобы спарсить в бд все данные из файлов в папке dataset, в запущенном docker контейнере запустить:
```
python parser_handler.py
```