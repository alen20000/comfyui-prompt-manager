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
    keys = ['ID','PROMPT','PROMPT_CLASS','COMMENT','IS_WORD']
    formatted_data = [dict(zip(keys, row)) for row in raw_data]
    return jsonify(formatted_data)

# def delete_primpts():
