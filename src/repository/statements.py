import src.repository.schema as schema
'''
statement模組 處理SQL邏輯組裝
SQL 語法表:https://www.1keydata.com/tw/sql/sql-syntax.html

這是一個 SQL語法映射器

'''
class Statement_builder():

    @staticmethod
    def build_table ():
        colums_sql = []

        for col, spec in schema.PromptTable.COLUMN_DEFINITIONS.items():
            # 如果 spec 裡面有 {col}，用目前的 col 變數把它填進去

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

    @staticmethod
    def build_get_all_prompt():
        sql = """
                SELECT * FROM prompts
            """
        return sql
    
    def update_prompt(id,data):
        keys = ",".join([f"{k} = ?"for k in data.keys()])
        print(keys)
        values = tuple(data.values())+(id,)
        sql = "UPDATE prompts SET {keys} Where id = ?".format(keys=keys)

        values = tuple(data.values()) + (int(id),)

        return sql,values

