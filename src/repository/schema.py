# schema.py

class PromptTable:
    #定義資料表
    TABLE_NAME = "prompts"

    # 定義欄位名稱
    ID = "id"
    PROMPT = "prompt"
    PROMPT_CLASS = "prompt_class"
    COMMENT = "comment"
    IS_WORD = "is_word" # 是否是單字 


    COLUMN_DEFINITIONS ={
        ID : "INTEGER PRIMARY KEY AUTOINCREMENT",
        PROMPT : "TEXT NOT NULL",
        PROMPT_CLASS : "TEXT",
        COMMENT : "TEXT",
        IS_WORD : "INTEGER NOT NULL DEFAULT 0 CHECK ({col} IN (0, 1))"
    }

    # 方便組裝使用的清單
    ALL_COLUMNS = [ID,PROMPT, PROMPT_CLASS, COMMENT, IS_WORD]