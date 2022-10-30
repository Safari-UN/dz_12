import json

""" Функция для открытия шаблона на чтение """
def load_posts(path='posts.json'):
    posts = []
    with open(path, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts

""" Функция для поиска в постах """
def search_post(substr):
    posts_found = []
    posts = load_posts()
    for post in posts:
        if substr in post['content']:
            posts_found.append(post)

    return posts_found

""" Функция для сохранения загруженых фото"""
def save_picture(picture):
    filename = picture.filename
    filetype = filename.split('.')[-1]

    if filetype not in ['jpg', 'jpeg', 'svg', 'png']:
        return
    """ Путь к сохраненным данным """
    picture.save(f'uploads/images/{filename}')

    return f'uploads/images/{filename}'


""" Функция для сохранения нового поста в список"""
def save_post_to_json(posts, path='posts.json'):
    with open(path, 'w+', encoding='utf-8') as file:
        json.dump(posts, file)


""" Функция для создания нового поста"""
def add_post(post):
    posts = load_posts()
    posts.append(post)
    save_post_to_json(posts)