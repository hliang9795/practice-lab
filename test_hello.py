import hello

def test_greet():
    assert hello.greet('Alice') == 'Hello, Alice!'

def test_greet_many():
    assert hello.greet_many(['Alice', 'Bob']) == ['Hello, Alice!', 'Hello, Bob!']

if __name__ == '__main__':
    test_greet()
    test_greet_many()
    print('tests passed')
