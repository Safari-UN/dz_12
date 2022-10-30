from flask import Blueprint, render_template, request
from functions import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates', url_prefix='/')


""" Функция для открытие шаблона через блюпринт"""
@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


""" Поиск и вывод постов при обращении """
@main_blueprint.route('/search')
def search_page():
    substr = request.args.get('s')
    posts = search_post(substr)
    return render_template('post_list.html', posts=posts, substr=substr)