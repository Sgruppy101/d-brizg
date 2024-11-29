from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Annotated
import datetime

app = FastAPI()

class Order(BaseModel):
    number : int
    date : datetime.date
    device : str
    model : str
    discripthion : str
    FIO : str
    number_phone : str
    status : str
    

repo = [
    Order(
        number = 1,
        date = "2024-11-29",
        device = "телефон",
        model = "se",
        discripthion = "сломан",
        FIO = "Пабло",
        number_phone = "79221382832",
        status = "завершено"
    )
]

@app.get("/orders")
def all_orders():
    return repo

@app.post("/orders")
def create_orders(dto : Annotated[Order, Form()]):
    repo.append(dto)

#поиск по номеру
@app.get("/orders/{num}") 
def getByNum(num):
    return [o for o in repo if o.number == int(num)][0]

#поиск по параметру
@app.get("/filter/{param}") 
def getByNum(param):
    return [o for o in repo if 
            o.date  == param or
            o.device == param or
            o.model == param or
            o.discripthion == param or
            o.FIO == param or
            o.number_phone == param or
            o.status == param
            ]        


