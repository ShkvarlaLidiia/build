def test (name):
    return f"Hello {name}"

def wrapper(cb):
    return cb("John")

result = wrapper(test)


print(result)

john = {
    "name": "John",
    "age": 23,

}

print(john["name"])