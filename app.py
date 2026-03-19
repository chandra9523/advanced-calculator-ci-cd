from fastapi import FastAPI, HTTPException
import calculator

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Advanced Calculator API"}

@app.get("/add/{a}/{b}")
def add(a: float, b: float):
    return {"result": calculator.add(a, b)}

@app.get("/subtract/{a}/{b}")
def subtract(a: float, b: float):
    return {"result": calculator.subtract(a, b)}

@app.get("/multiply/{a}/{b}")
def multiply(a: float, b: float):
    return {"result": calculator.multiply(a, b)}

@app.get("/divide/{a}/{b}")
def divide(a: float, b: float):
    try:
        return {"result": calculator.divide(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/power/{a}/{b}")
def power(a: float, b: float):
    return {"result": calculator.power(a, b)}