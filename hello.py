def greet(name):
    return f"Hello, {name}!"

def greet_many(names):
    return [greet(name) for name in names]

if __name__ == '__main__':
    print(greet_many(['World', 'Tester']))
