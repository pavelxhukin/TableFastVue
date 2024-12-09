from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

classes = [ 
    {
        "id" : 1 ,
        "title" : "Math",
        "type" : "lection",
    },
    {
        "id" : 2 ,
        "title" : "Phisics",
        "type" : "Practic text"
    }
]

@app.get("/classes", tags=["Занятия"],summary=["получить все занятия"])
def get_classes():
    return classes


@app.get("/classes/{class_id}", tags=["Занятия"],summary=["получить конкретнуя книгу"])
def get_class(class_id: int):
    for element in classes:
        if element["id"] == class_id:
            return element
    return {"404":"видимо такой книги нет"}


class NewClass(BaseModel):
    title: str
    type: str

@app.post("/classes")
def create_class(new_class: NewClass):
    classes.append({
        "id": len(classes) + 1,
        "title": new_class.title,
        "type": new_class.type,
    })
