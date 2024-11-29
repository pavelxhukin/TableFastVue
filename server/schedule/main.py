from fastapi import FastAPI


app = FastAPI()


@app.get("/info")
def get_info():
    return {"data":"some info to poetry from schedule"}