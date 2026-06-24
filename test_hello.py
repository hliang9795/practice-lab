import hello

def test_greet():
    assert hello.greet('Alice') == 'Hello, Alice!'

if __name__ == '__main__':
    test_greet()
    print('tests passed')
