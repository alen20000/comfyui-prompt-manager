from database import Database


data = {
    "title": "森林精靈",
    "positive": "",
    "negative": "",
    "note": "測試用",
    "tags": "奇幻"
}

db = Database()

# db.add_promt(title="測試", positive="test")
# db.add_promt(data)
result = db.get_all_prompts()
db.update_prompt(1,{"title":"dog"})
print(result)