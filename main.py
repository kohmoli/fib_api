from fastapi import FastAPI

app = FastAPI()

@app.get('/fib')
def fib(n: int):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a+b
    
    return { 'result': a }
