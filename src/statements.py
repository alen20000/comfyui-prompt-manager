class Prompt_sql():

    '''初始化DB'''
    CREAT_TABLE = """
            CREATE TABLE IF NOT EXISTS prompts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                note TEXT,
                positive TEXT,
                negative TEXT,
                tags TEXT,
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