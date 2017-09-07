test1 = "Hello Worl"
test2 = "Hello World"

def test(testparam, testparam2):
    if testparam == testparam2:
        return type(testparam)
    mylist = ["a", "b", "c", "d", "e"]
    for i in mylist:
        print i
    for i in range(0, len(mylist)):
        print i
    return False

print test(test1, test2)
