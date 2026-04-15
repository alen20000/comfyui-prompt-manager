from flask import Flask
from routes.prompt import prompt_bp
import webbrowser
from threading import Timer
import os
app = Flask(__name__)
# TODO: 當 Blueprint 過多，考慮用動態註冊
app.register_blueprint(prompt_bp, url_prefix = '/')


def open_web():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == '__main__':
    #不設置這判斷環境變量 ，flask父進程偵測變化時，子進程會重新調用。
    #子進程進入時，會在記憶體端設置一個環境變數 "WERKZEUG_RUN_MAIN=true"
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        Timer(1, open_web).start()
    app.run(debug=True)