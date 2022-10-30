""" Импортируем функции """
from flask import Flask, send_from_directory
from main.view import main_blueprint
from loader.view import loader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

""" Регистрируем Блюпринты """
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

""" Функция для загрузки файлов из папки uploads """
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)

