import random
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_fib_1():
    """n=1のとき、1番目のフィボナッチ数は1である
    """
    response = client.get('/fib?n=1')
    assert response.status_code == 200
    assert response.json()['result'] == 1


def test_fib_2():
    """n=2のとき、2番目のフィボナッチ数は1である
    """
    response = client.get('/fib?n=2')
    assert response.status_code == 200
    assert response.json()['result'] == 1


def test_fib_k():
    """n=kのとき、k番目のフィボナッチ数は(k-2)番目と(k-1)番目の和である
    """
    i = random.randint(1, 100000)
    j, k = i+1, i+2
    
    response_i = client.get(f'/fib?n={i}')
    response_j = client.get(f'/fib?n={j}')
    response_k = client.get(f'/fib?n={k}')
    assert response_i.status_code == 200
    assert response_j.status_code == 200
    assert response_k.status_code == 200
    assert response_i.json()['result'] + response_j.json()['result'] == response_k.json()['result']


def test_fib_none():
    """nが与えられないとき、422エラーを返す
    """
    response = client.get(f'/fib')
    assert response.status_code == 422


def test_fib_invalid_number():
    """整数nが1未満であるとき、422エラーを返す
    """
    n = random.randint(-100000, 0)
    response = client.get(f'/fib?n={n}')
    assert response.status_code == 422


def test_fib_string():
    """nが文字列であるとき、422エラーを返す
    """
    n = chr(random.randint(65, 90)) # A-Z
    response = client.get(f'/fib?n={n}')
    assert response.status_code == 422
