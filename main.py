from fastapi import Body, FastAPI

app=FastAPI();

@app.get("/")
async def root():
    return {"message":"Welcome to  !!!! my api"}
@app.get("/post")
def get_post():
    return {"id":"Sachin",
            "data":"This is your post"}
@app.post("/create-post")
def create_post(pay_load:dict=Body(...)):
    print(pay_load)
    return {"new_post":f"message:{pay_load['message']}" ,
            "content":f"{pay_load['list']}"}