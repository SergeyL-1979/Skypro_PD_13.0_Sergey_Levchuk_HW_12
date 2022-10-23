#!/usr/bin/env python
# -*- coding: utf-8 -*-

# `loader` - для загрузки фото
from json import JSONDecodeError
from flask import Blueprint, request, render_template
import logging
from functions import add_content

loader_img = Blueprint("loader_img", __name__, template_folder='templates', static_folder='static')


# Создаем множество расширений
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


@loader_img.route("/post")
def page_post_form():
    return render_template('post_form.html')


@loader_img.route("/post", methods=["POST"])
def page_post_upload():
    try:
        # Получаем файл
        picture = request.files.get("picture")
        # Получаем текст из формы
        content = request.form.get("content")
        # Получаем имя файла у загруженного файла
        filename = picture.filename
        # Получаем расширение файла
        extension = filename.split(".")[-1]
        if not picture or not content:
            logging.error(f'Расширение *.{extension} - ЗАПРЕЩЕНЫ!!!. Отсутствуют данные')
            return f'''<h1> Отсутствуют данные или расширения *.{extension} - ЗАПРЕЩЕНЫ!</h1>
                            <p>Вернитесь <a href="/post" class="link">назад</a></p>'''
        # Если расширение файла в белом списке
        if extension in ALLOWED_EXTENSIONS:
            # Сохраняем картинку под родным именем в папку uploads
            picture.save(f'./uploads/images/{picture.filename}')
            picture_url = f'uploads/images/{picture.filename}'
            add_content({'pic': picture_url, 'content': content})
            logging.info('POST SAVE')
            return render_template("post_uploaded.html", picture=picture, content=content)
        else:
            logging.info(f'{picture.filename}: не изображение!')
            return render_template("post_uploaded.html", extension=extension)
    except FileNotFoundError:
        logging.error('Файл отсуствует')
        return 'Файл отсуствует'
    except JSONDecodeError:
        return 'Невалидный файл'

