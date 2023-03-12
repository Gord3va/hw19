Урок 19. Декораторы и контроль доступа. Домашнее задание

Перед запуском основного приложения запустите create_data.py для создания и заполнения БД

* views жанров:

```
GET /genres — получить все жанры
GET /genres/3 — получить жанр по ID
POST /genres — создать жанр
PUT /genres/1 — изменить информацию о жанре
DELETE /genres/1 — удалить жанр
```

* views режиссеров

```
GET /directors — получить всех режиссеров
GET /directors/3 — получить режиссера по ID
POST /directors — создать режиссера
PUT /directors/1 — изменить информацию о режиссере
DELETE /directors/1 — удалить режиссера
```

* views фильмов

```
GET /movies — получить все фильмы
GET /movies/3 — получить фильм по ID
GET /movies?director_id=15 — получить все фильмы режиссера
GET /movies?genre_id=3 — получить все фильмы жанра
GET /movies?year=2007 — получить все фильмы за год
POST /movies — создать фильм
PUT /movies/1 — изменить информацию о фильме
DELETE /movies/1 — удалить фильм
```

* vies пользователей
```
GET /users — получить всех пользователей
GET /users/3 — получить пользователя по ID
POST /users — создать пользователя
PUT /users/1 — изменить информацию о пользователе
DELETE /users/1 — удалить пользователя
```

* vies авторизации
```
POST /auth/ — возвращает `access_token` и `refresh_token` или `401`
PUT /auth/ — возвращает `access_token` и `refresh_token` или `401`
```

* Ограничен доступ на чтение Authorized Required
```
GET /directors/ + /directors/id
GET /movies/ + /movies/id
GET /genres/ + /genres/id
```

* Ограничен доступ на редактирование Authorized Required + Role admin Required
```
POST/PUT/DELETE  /movies/ + /movies/id
POST/PUT/DELETE  /genres/ + /genres/id
POST/PUT/DELETE  /directors/ + /directors/id
```