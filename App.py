from flask import Flask
from routes.prompt import prompt_bp
import webbrowser
from threading import Timer
import os
app = Flask(__name__)
app.register_blueprint(prompt_bp, url_prefix = '/')


def open_web():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == '__main__':
    #不設置這個環境變量 ，父進程偵測變化，子進程會打開。
    #子進程打開時，會在記憶體得到一個環境變數 "WERKZEUG_RUN_MAIN=true"
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        Timer(1, open_web).start()
    app.run(debug=True)