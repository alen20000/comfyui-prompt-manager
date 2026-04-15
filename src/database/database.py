import sqlite3
import os
from config import path

from src.repository.statements import Statement_builder
from src.utils.decorators.db import db_operation
'''
功能:資料庫API
'''

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

            sql = Statement_builder.build_table()

            conn.execute(sql)
            conn.commit() 
    
    def add_prompt(self,**kwargs):
        '''新增欄位'''

        with self._get_conn() as conn:
            sql,values = Statement_builder.build_insert(kwargs)

            conn.execute(sql, values)
            conn.commit()

    def get_all_prompts(self):  
        '''查閱 全部資料'''

        with self._get_conn() as conn:
            sql = Statement_builder.build_get_all_prompt()
            cursor = conn.execute(sql) #要建實例，保存回傳值
            return  [dict(row) for row in cursor.fetchall()]

    def update_prompt(self, id, **kwargs: dict):
            '''
            更新 row 內 屬性
            Args:
                id(int):要跟新資料ID
                data(dic):更新欄位與數值
            '''
            sql,values = Statement_builder.update_prompt(id,kwargs)

            with self._get_conn() as conn:
                conn.execute(sql, values)
                conn.commit()

    def delete_prompt(self,id):
        '''刪除 row'''

        with self._get_conn() as conn:
            conn.execute(Statement_builder.build_delect(),(int(id),))  # 傳參要為int並放入turple，逗號不能省
            conn.commit()



if __name__ == "__main__":
    db = Database()
    # db.add_prompt(
    # prompt="測試1號", 
    # prompt_class="quality", 
    # comment="elf in forest",
    # is_word= False
    # )
    update_dic = {"prompt" : "測試三號"}
    update_id = "7"

    db.update_prompt(int(update_id),**update_dic)
    result = db.delete_prompt(6) 
    result2 = db.get_all_prompts()
    print(result2)
    pass

'''
py -m src.database.database  根目錄調用指令
'''