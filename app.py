#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask, send_from_directory
# from functions import ...
import logging
from main.main_img import main_bp
from loader.loader_img import loader_img


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(main_bp, url_prefix='/')
app.register_blueprint(loader_img, url_prefix='/')


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


@app.errorhandler(413)
def page_not_found(e):
    logging.error(f'Ошибка - {e} Файл большого размера!')
    return '''<h1>Файл большеват</h1><p>Поищите поменьше, плиз!</p>
            <p>Повторите запрос! Вернитесь <a href="/" class="link">назад</a></p>''', 413


if __name__ == "__main__":
    app.run(debug=True)
