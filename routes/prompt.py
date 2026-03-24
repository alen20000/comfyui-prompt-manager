from flask import Blueprint, jsonify, request
# 注意：這裡我們先不 import Database，先讓網址跑通！

# 1. 定義藍圖零件 (變數名, 內部身分證)
prompt_bp = Blueprint('prompt', __name__)

# 2. 寫一個測試用的門牌
@prompt_bp.route('show', methods=['GET'])
def test_connection():
    return jsonify({"message": "連線成功！這是你的第一個 Blueprint"})