#!/usr/bin/env python
# -*- coding: utf-8 -*-

# `loader` - для загрузки фото
import os
from flask import Blueprint, request, render_template
import logging
from functions import add_content

loader_img = Blueprint("loader_img", __name__, template_folder='templates', static_folder='static')
logging.basicConfig(filename='log_info.log', level=logging.INFO, encoding='utf-8')

# Создаем множество расширений
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


@loader_img.route("/post")
def page_post_form():
    return render_template('post_form.html')


@loader_img.route("/post", methods=["POST"])
def page_post_upload():
    # Получаем файл
    picture = request.files.get("picture")
    # Получаем текст из формы
    content = request.form.get("content")
    # Получаем имя файла у загруженного файла
    filename = picture.filename
    # Получаем расширение файла
    extension = filename.split(".")[-1]
    # Если расширение файла в белом списке
    if extension in ALLOWED_EXTENSIONS:
        # Сохраняем картинку под родным именем в папку uploads
        picture.save(f'./uploads/images/{picture.filename}')
        picture_url = f'uploads/images/{picture.filename}'
        add_content({'pic': picture_url, 'content': content})
        logging.info('POST SAVE')
        return render_template("post_uploaded.html", picture=picture, content=content)
    elif picture == picture:
        logging.error(f'Расширение *.{extension} - ЗАПРЕЩЕНЫ!!!. Отсутствуют данные')
        return f'''<h1> Отсутствуют данные </h1> <strong>Расширения *.{extension} - ЗАПРЕЩЕНЫ</strong>
                <p>Вернитесь <a href="/post" class="link">назад</a></p>'''
    else:
        logging.info(f'{picture.filename}: не изображение!')
        return render_template("post_uploaded.html", extension=extension)

