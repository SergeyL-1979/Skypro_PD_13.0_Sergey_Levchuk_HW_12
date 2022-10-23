#!/usr/bin/env python
# -*- coding: utf-8 -*-

# `main` - для показывания фото
from flask import Blueprint, render_template, request
import logging
from functions import search_content

main_bp = Blueprint("main_img", __name__, template_folder='templates', static_folder='static')


@main_bp.route('/')
def page_index():
    return render_template("index.html")


@main_bp.route("/search")
def page_search():

    sub = request.args.get('s').lower()
    posts = search_content(sub)

    if not sub:
        return f'''<h2> Строка поиска пуста. </h2>
                <p>Повторите запрос! Вернитесь <a href="/" class="link">назад</a></p>'''
    logging.info(f'Запросы поиска: {sub}')
    return render_template('post_list.html', posts=posts, sub=sub)


