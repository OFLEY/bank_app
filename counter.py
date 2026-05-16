counter = 0
def increment():
    global counter
    counter += 1


def decrement():
    global counter
    counter -= 1

def show():
    print(counter)

show()
increment()
show()
decrement()
show()