from fastapi import FastAPI

app = FastAPI(
    title = "Trading app"
)

fake_users = [
    {"id": 1, "role" : "admin", "name": "John"},
    {"id": 2, "role" : "investor", "name": "Matt"},
    {"id": 3, "role" : "trader", "name": "Hew"}
]

@app.get("/users/user_id")
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]

fake_trade = [
    {"id": 1, "user_id" : 1, "currency": "BTC", "side": "buy", "price": 123,"ammount": 100.32},
    {"id": 2, "user_id" : 3, "currency": "BTC", "side": "buy", "price": 125,"ammount": 101.52}
]

@app.get("/trades")
def get_treades(limit: int = 1, offset: int = 1):
    return fake_trade[limit:][:offset]

fake_users2 = [
    {"id": 1, "role" : "admin", "name": "John"},
    {"id": 2, "role" : "investor", "name": "Matt"},
    {"id": 3, "role" : "trader", "name": "Hew"}
]

@app.post("/users/user_id")
def change_user_name(user_id: int, new_name: str):
    curr_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))[0]
    curr_user["name"] = new_name
    return {"status" : 200, "data": curr_user}