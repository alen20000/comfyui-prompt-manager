import os


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #根目錄
DATA_PATH = os.path.join(BASE_PATH,'Data') #DB資料夾
DB_PATH = os.path.join(DATA_PATH,'database.db') #DB路徑
