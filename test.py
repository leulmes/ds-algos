
def foo():
    x = 5
    print("x before: ", x)
    bar(x)
    print("x after: ", x)

def bar(i):
    i += 1
    print("x in bar: ", i)

foo()