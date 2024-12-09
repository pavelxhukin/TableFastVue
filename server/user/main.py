from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def get_user():
    return {"data":"hello poetry from user app!"}