# Messenger app



## Сборка приложения

- Перейдите в директорию с приложением (если вы используете WSL, перейдите с WSL)
с помощью команды cd
- Перейдите в директорию
```
cd docker/hackathon-messenger_instances/
```
- Создайте файл .env
```
cp .env.sample .env
```
- Отредактируйте файл .env под свои нужды
- Запустите сборку
```
chmod +x build
./build
```

## Если вы запускаете любой скрипт в первый раз
```
chmod +x имя_скрипта
```
Например, перед первым запуском приложения, нужно выполнить
```
chmod +x start
```
## Управлениe приложением
### Запуск приложения
В папке docker/hackathon-messenger_instances/ запустите
```
./start
```

### Остановка приложения
В папке docker/hackathon-messenger_instances/ запустите
```
./stop
```

### Просмотреть логи бэкэнда
В папке docker/hackathon-messenger_instances/ запустите
```
./django_logs
```
## После запуска
- Вы найдете приложение по адресу http://localhost:$BACKEND_PORT$,
где BACKEND_PORT - значение переменной BACKEND_PORT в файле docker/hackathon-messenger_instances/.env
- Аналогично с FRONTEND
## Управление бэкэндом
### Консоль Django
Если вы хотите взаимодействовать непосредственно с файлом manage.py, запустите в папке backend/api/
```
./open_bash
```
После выполнения этой команды откроется терминал Linux, в котором в сможете взаимодействовать с manage.py
Если вы желаете из него выйти, выполните
```
exit
```
### Выполнение миграций
Запустите в папке backend/api/
```
./migrate
```
### Выполнение миграций
Запустите в папке backend/api/
```
./makemigrations
```
## Настройка
В файле frontend/src/app/restapi.ts измените значения на хост бэкэнда для веб сокета и для REST API. В случае, если вы запускаете локально, замените 98 в строках на порт BACKEND_PORT в docker/hackathon-messenger_instances/.env
