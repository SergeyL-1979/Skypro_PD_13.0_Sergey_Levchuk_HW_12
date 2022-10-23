#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pprint import pprint


def load_json(path="posts.json"):
    """ Функция загрузки данных из JSON """
    dates = []
    with open(path, "r", encoding="utf-8") as file:
        dates = json.load(file)
    return dates


def search_content(subcontent):
    content_search = []
    posts = load_json('posts.json')
    for post in posts:
        if subcontent in post['content'].lower():
            content_search.append(post)
    return content_search


def save_json_post(posts, path='posts.json'):
    with open(path, 'w', encoding='utf=8') as file:
        json.dump(posts, file, indent=4, ensure_ascii=False)


def add_content(post):
    posts = load_json()
    posts.append(post)
    save_json_post(posts)
