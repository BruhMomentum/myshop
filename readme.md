# ТЗ
## Интернет магазин
1. Одна товарная категория телефоны
2. Две таблицы в бд: Производитель, Товар. Связь 1 ко многим
3. Покупателей хранить в базе юзеров Django
4. Postgres будет в контейнере

## Web интерфейс
1. Одна главная страница
2. Адаптивный дизайн в стиле DNS

## Требования к админке
1. Полный CRUD к товарам

## Требования к оформлению корзины
1. Отдельная страница на заказ (можно поменять количество товаров и опции удалить из корзины)

## Требования к заказа
1. С юзера брать email, адрес доставки

## Что нужно знать
MTV - model template view. База данных, взаимодействие с фронтом, встроеные джанго компоненты.

## Архитектура интернет магазина
Будет 3 app, shop главный, корзина и заказ, под каждый url, вьюшку.