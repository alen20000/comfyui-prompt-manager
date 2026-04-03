from flask import Blueprint,render_template
from src.database.database import Database

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
    data = db.get_all_prompts()
    return render_template('partials/prompt_items.html', prompts=data)