# **ИДЕЯ:**

Привет! В этом проекте я хочу проанализировать имена в России (в особенности, в Москве), проверить некоторые гипотезы, такие, как:

1. Цикличность имен - наверное, многие сталкивались со случаями, что детей называют в честь их бабушек и т.д.?)
2. Связь популярности имен с некоторыми событиями - я нашла много сайтов, которые говорят, что популярность имен зависит от популярности фильмов или от значимых событий - это и надо будет проверить.
3. Чем ближе регионы России, тем более схожие у них популярные имена.
4. Посмотрим на корреляции популряности разных имен - когда одни имена становятся популярными, другие теряют свою популряность?
5. Посмотрим, насколько имена в Москве следуют за "трендами" имен по всему миру.
6. Ну и просто посомотрим самые популярные имена в Москве по годам и сделаем из этого некоторые выводы - например, кому можно жаловаться, что слишком много людей с его именем)

# **Технологии:**
1. API - для извлечения с сайта data.mos.ru - документация по ссылке: https://data.mos.ru/developers
2. Веб-скреппинг с помощью beautifulsoap для считывания таблиц с сайтов
3. Pandas - для работы с таблицами и отбора данных из них
4. Регулярные выражения - для прописывания условий для нахождения определенных имен
5. Numpy - для рассчитываний корреляций популярности имен
6. Geopandas - для постороения карты России и работы с ней
7. Networkx - для работы с графами и удобной визуализации
8. Простая визуализация данных с помощью matplotlib - для рисования графиков и диаграмм
9. SQL - для более эффективного выполнения запросов
10. Streamlit - для качественной демонстрации данных в интернете
11. Линейные регрессии - для предсказания поведения данных
12. Дополнительные библиотеки, как mtranslate или seaborn
13. Хорошее настроение и рабочий настрой!