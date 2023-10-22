from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


app = FastAPI()


class InvalidNumberException(Exception):
    pass

@app.exception_handler(InvalidNumberException)
async def unicorn_exception_handler(request: Request, exc: InvalidNumberException):
    return JSONResponse(
        status_code=422,
        content={ 'status': 422, 'message': 'value is not a valid integer' },
    )


@app.get('/fib')
def fib(n: int):
    if n < 1:
        raise InvalidNumberException()

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a+b
    
    return { 'result': a }
