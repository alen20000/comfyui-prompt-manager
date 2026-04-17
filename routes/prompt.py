from flask import Blueprint,render_template,jsonify
from src.database.database import Database
'''
路由層API
'''
prompt_bp = Blueprint('prompt', __name__)

db = Database()    


@prompt_bp.route('/', methods=['GET'])
def test_connection():
    '''
    Main page    
    '''
    return render_template('index.html')

@prompt_bp.route('/get_all_prompts', methods=['GET'])
def get_all_prompts():
    raw_data = db.get_all_prompts()

    return jsonify({
        "status":"ok",
        "total":len(raw_data),
        "data":raw_data
    })

# def delete_primpts():
