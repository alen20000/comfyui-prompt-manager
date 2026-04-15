import src.repository.schema as schema
'''
statement模組 處理SQL邏輯組裝
SQL 語法表:https://www.1keydata.com/tw/sql/sql-syntax.html

這是一個 SQL語法映射器

'''
class Statement_builder():


    def build_table ():
        colums_sql = []

        for col, spec in schema.PromptTable.COLUMN_DEFINITIONS.items():
            # 如果 spec 裡面有 {col}，我們就用目前的 col 變數把它填進去
            # 這樣無論你以後改什麼名字，這裡都會自動同步！
            formatted_spec = spec.format(col=col) 
            colums_sql.append(f"{col} {formatted_spec}")
        list_to_str = ", ".join(colums_sql)
        print(list_to_str)

        sql = f"CREATE TABLE IF NOT EXISTS {schema.PromptTable.TABLE_NAME} ({list_to_str}) "
        return sql
    
    @staticmethod
    def build_insert (data:dict)-> tuple[str, tuple]:

        cols=",".join(data.keys())
        placeholders = ",".join(["?" for _ in range(len(data))])
        sql = f"INSERT INTO {schema.PromptTable.TABLE_NAME} ({cols}) VALUES ({placeholders})" 
        values = tuple(data.values())
        return sql, values
    
    @staticmethod
    def build_delect():
        sql = "DELETE FROM prompts WHERE id = ?"
        return sql
class Prompts_sql():

    '''初始化DB'''
    CREAT_TABLE = """
            CREATE TABLE IF NOT EXISTS prompts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prompt TEXT NOT NULL,
                comment TEXT NOT NULL,
                is_a_word INTEGER NOT NULL DEFAULT 0 ,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
    
    ADD_PROMPT = """
            INSERT INTO prompts (title, note, positive, negative, tags)
            VALUES (?, ?, ?, ?, ?)

            """
    
    GET_ALL_PROMPT = """
                SELECT * FROM prompts
            """
    
    UPDATE_PROMPT = """
        UPDATE prompts SET {keys} Where id = ?
        """
    
    DELETE_PROMPT = """
    DELETE FROM prompts WHERE id = ?
    """