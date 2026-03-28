from flask import Blueprint,render_template
# 注意：這裡我們先不 import Database，先讓網址跑通！

# 1. 定義藍圖零件 (變數名, 內部身分證)
prompt_bp = Blueprint('prompt', __name__)


@prompt_bp.route('/', methods=['GET'])
def test_connection():
    '''
    Main page    
    '''
    return render_template('index.html')