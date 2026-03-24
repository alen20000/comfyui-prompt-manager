from flask import Flask
from routes.prompt import prompt_bp


app = Flask(__name__)
app.register_blueprint(prompt_bp, url_prefix = '/test')


if __name__ == '__main__':
    app.run(debug=True)