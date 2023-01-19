# 9.3
def test(func):
    def new_function():
        print('실행중인 함수:', func.__name__)
        print('start')
        print('end')
    return new_function

@test
def say():
    print('hi')
say()


# 9.4
class OopsException(Exception):
    pass

words = ['Oops','oops']
for word in words:
    if word.isupper():
        raise OopsException(word)
try:
    raise OopsException('Caught an oops')
except OopsException as err:
    print(err)






































































