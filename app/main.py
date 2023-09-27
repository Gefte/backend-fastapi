from fastapi import FastAPI, HTTPException
from typing import List, Dict

app = FastAPI()

def fibonacci_recursive(qtd_elementos: int) -> List[int]:
    if qtd_elementos <= 0:
        return []
    elif qtd_elementos == 1:
        return [0]
    elif qtd_elementos == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < qtd_elementos:
            next_element = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_element)
        return fib_sequence

@app.get("/health", response_model=Dict)
def read_root():
    return {"status": "Estou saudável"}


@app.get("/fibonacci/{qtd_elementos}", response_model=List[int])
def get_fibonacci_sequence(qtd_elementos: int):
    if qtd_elementos <= 0:
        raise HTTPException(status_code=400, detail="A quantidade de elementos deve ser maior que zero")
    return fibonacci_recursive(qtd_elementos)