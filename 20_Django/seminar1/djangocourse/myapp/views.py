import logging

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request, *args, **kwargs):
    response = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Мой первый Django-сайт</title>
</head>
<body>

<h1>Мой первый Django-сайт</h1>

<p>Этот сайт был создан с использованием Django - мощного фреймворка для веб-разработки на Python.</p>

<h2>Обо мне</h2>

<p>Меня зовут Георгий, и я полный новичок в веб-разработке. Я начал изучать Django несколько месяцев назад и решил создать этот сайт, чтобы продемонстрировать свои навыки и поделиться своими знаниями.</p>

<p>Я надеюсь, что мой сайт будет полезен другим новичкам, которые, как и я, только начинают свой путь в веб-разработке.</p>

</body>
</html>
    """
    logger.info("index page was requested")
    return HttpResponse(response)


def about(request, *args, **kwargs):
    response = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Обо мне</title>
</head>
<body>

<h1>Обо мне</h1>

<p>Привет! Меня зовут Георгий, и я страстно люблю программирование. Я начал изучать программирование несколько лет назад, и с тех пор это стало моей страстью и образом жизни.</p>

<p>Я обожаю решать сложные задачи и находить элегантные решения. Программирование позволяет мне выражать свою креативность и логическое мышление, и я всегда стремлюсь узнать больше и развиваться в этой области.</p>

<p>Я надеюсь, что мой сайт поможет другим людям, которые также интересуются программированием, и что я смогу поделиться своими знаниями и опытом с сообществом.</p>

</body>
</html>
    """
    logger.info("about page was requested")
    return HttpResponse(response)
