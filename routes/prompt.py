from flask import Blueprint,render_template,jsonify,request
from src.database.database import Database
'''
路由層API
'''
prompt_bp = Blueprint('prompt', __name__)

db = Database()    


# @prompt_bp.route('/', methods=['GET'])
# def test_connection():
#     '''
#     Main page    
#     '''
#     return render_template('index.html')

@prompt_bp.route('/get_all_prompts', methods=['GET'])
def get_all_prompts():
    '''
    查閱全部 prompt 資料

    資料小時候，直接回傳全部資料，資料量大時，應該要加上分頁功能
    '''
    raw_data = db.get_all_prompts()

    return jsonify({
        "status":"ok",
        "total":len(raw_data),
        "data":raw_data
    })

@prompt_bp.route('/add_prompt', methods=['POST'])
def add_prompt():
    '''
    新增 prompt 資料
    '''
    data: dict = request.get_json()

    db.add_prompt(**data)

    return  jsonify({
        "status":"ok",
        "message":"新增成功"
    })

@prompt_bp.route('/delete_prompt', methods=['DELETE'])
def delete_prompt():
    '''
    參數格式：{"id":<id>}  刪除指定ID的row
    '''
    data: dict = request.get_json()

    db.delete_prompt(**data)
    
    return jsonify({
        "status":"ok",
        "message":"刪除成功"
    })

@prompt_bp.route('/update_prompt', methods=['PUT'])
def update_prompt():
    '''
    更新 prompt 資料
    參數: ID 、要更新的欄位與數值
    '''
    deta: dict = request.get_json()

    db.update_prompt(**deta)
    
    return jsonify({
        "status":"ok",
        "message":"更新成功"
    })

# def delete_primpts():
