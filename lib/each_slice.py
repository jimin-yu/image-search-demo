# return generator object
def each_slice(list, size):
    batch = 0
    while batch * size < len(list):
        yield list[batch * size:(batch + 1) * size]
        batch += 1   



