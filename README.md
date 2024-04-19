### Тестовое задание. Backend.
Стажировка в Климат Холдинг.

# Документация API для кофейни

## Установка и запуск
Для установки и запуска проекта выполните следующие шаги:

1. ```git clone https://github.com/Quatry/coffeehouse.git```
2. ```pip install -r requirements.txt```
3. ```python manage.py migrate```
4. ```python manage.py runserver```
5. Перейти по ```http://localhost:8000/api```

## CoffeeHouse (Кофейня)

### Модель CoffeeHouse

Модель представляет кофейню с основными характеристиками.

#### Поля модели:

- **name**: Название кофейни (`CharField`)
- **schedule**: Расписание работы кофейни (`CharField`)
- **date_created**: Дата создания записи (`DateTimeField`, автоматически заполняется при создании)
- **info**: Дополнительная информация о кофейне (`TextField`)
- **slug**: Уникальный идентификатор (`SlugField`, уникальный)

### URL-шаблоны (`api.coffeehouse.urls`)

#### `GET` Возвращает список всех кофеен.
```localhost:8000/api/```

#### `POST` Создает новую кофейню.
```localhost:8000/api/add_coffee_house```


#### `GET` Возвращает информацию о конкретной кофейне по его уникальному идентификатору.
```localhost:8000/api/<slug:slug>/```


#### `PUT`, `DELETE` Изменяет или удаляет информацию о конкретной кофейне по его уникальному идентификатору.
```localhost:8000/api/<slug:slug>/edit```


## Menu (Меню)

### Модель Menu

Модель представляет меню кофейни с набором блюд.

#### Поля модели:

- **name**: Название меню (`CharField`)
- **coffeehouse**: Ссылка на кофейню (`ForeignKey`)
- **slug**: Уникальный идентификатор (`SlugField`, уникальный)

### URL-шаблоны (`api.menu.urls`)

#### `POST` Добавляет новое меню для конкретной кофейни.
```localhost:8000/api/<slug:c_h_slug>/menu/add/```


#### `GET` Возвращает информацию о конкретном меню по его уникальному идентификатору.
```localhost:8000/api/<slug:c_h_slug>/menu/<slug:slug>/```


#### `PUT`, `DELETE` Изменяет или удаляет информацию о конкретном меню по его уникальному идентификатору.
```localhost:8000/api/<slug:c_h_slug>/menu/<slug:slug>/edit/```


## MenuItem (Элемент меню)

### Модель MenuItem

Модель представляет отдельный пункт в меню кофейни.

#### Поля модели:

- **name**: Название пункта меню (`CharField`)
- **measure_unit**: Единица измерения (`CharField`, выбор из предопределенных значений)
- **units**: Количество единиц (`IntegerField`)
- **menu**: Ссылка на меню (`ForeignKey`)
- **photo**: Фотография блюда (`ImageField`)

### URL-шаблоны (`api.menuitems.urls`)

#### `POST` Добавляет новый пункт меню в конкретное меню.
```localhost:8000/api/<slug:c_h_slug>/menu/<slug:menu_slug>/items/add/```


#### `GET`Возвращает информацию о конкретном пункте меню по его уникальному идентификатору.
```localhost:8000/api/<slug:c_h_slug>/menu/<slug:menu_slug>/items/<slug:id>/```


#### `PUT`, `DELETE` Изменяет или удаляет информацию о конкретном пункте меню по его уникальному идентификатору.
```localhost:8000/api/<slug:c_h_slug>/menu/<slug:menu_slug>/items/<slug:id>/edit/```

