import sqlite3
import os
from config import path
from src.statements import Prompt_sql

class Database:
    def __init__(self):

        os.makedirs(path.DATA_PATH,exist_ok=True)
        self._init_tables()

    def _get_conn(self):

        conn = sqlite3.connect(path.DB_PATH) #調用才開，要用with 觸發內層exit()
        conn.row_factory =sqlite3.Row  # 這是 把 sqlite3 的 Row Class 指派 conn的 row_factory屬性
        return conn
    
    def _init_tables(self):
        '''建立資料表'''
        with self._get_conn()  as conn:

            sql = (Prompt_sql.CREAT_TABLE)
            
            conn.execute(sql)
            conn.commit() 
    
    def add_promt(self, title, positive, negative="",note="",tags=""):
        '''新增 row'''

        with self._get_conn() as conn:
            sql = Prompt_sql.ADD_PROMPT
            conn.execute(sql, (title, note, positive,negative, tags,))
            conn.commit()

    def get_all_prompts(self):  
        '''查閱 row'''

        with self._get_conn() as conn:
            sql = Prompt_sql.GET_ALL_PROMPT
            cursor = conn.execute(sql) #要建實例，保存回傳值
            return  [dict(row) for row in cursor.fetchall()]

    def update_prompt(self, id, data: dict):
            '''
            更新 row 內 屬性
            Args:
                id(int):要跟新資料ID
                data(dic):更新欄位與數值
            '''

            keys = ",".join([f"{k} = ?"for k in data.keys()])
            values = tuple(data.values())+(id,)

            sql = Prompt_sql.UPDATE_PROMPT.format(keys=keys)

            with self._get_conn() as conn:
                conn.execute(sql, values)
                conn.commit()

    def delete_prompt(self,id):
        '''刪除 row'''

        with self._get_conn() as conn:
            conn.execute(Prompt_sql.DELETE_PROMPT,(int(id),))  # 傳參要為int並放入turple 
            conn.commit()
