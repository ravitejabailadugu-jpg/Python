from fastapi import FastAPI
app = FastAPI()

@app.get("/")

def home_page():
    return {"message":"welcome to the Fastapi Application"}

def about_page():
    return{"message":"welcome to the about page"}

def contant_page():
    return {"message":"welcome to the contant"}


