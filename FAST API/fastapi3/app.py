from fastapi import FastAPI
app =FastAPI()


@app.get("/")
def home_page():
    return{'message':"application root req"}

@app.post("/create")

def create_user():
    return {'message':"user cteate"}

@app.put("/update")

def update_user():
    return{'message':"data update"}


@app.get("/read")
def read_user():
    return{'message':"books read"}

@app.delete("/delete")
def delete_user():
     return{'message':"delete user"}