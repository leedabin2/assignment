
def isstackfull():
	global SIZE,stack,top
	if top >= SIZE:
		return True
	else:
		return False

def isstackempty():
	global SIZE, stack, top
	if top == -1:
		return True
	else:
		return False

def push(data):
	global SIZE, stack, top
	if isstackfull():
		return
	top += 1
	stack[top] = data

def pop():
	global SIZE, stack, top
	if isstackempty():
		return None
	data = stack[top]
	stack[top] = None
	top -= 1
	return data

def peek():
	global SIZE, stack, top
	if isstackempty():
		return None
	return stack[top]

# 전역 변수
SIZE = 6
stack = [None for _ in range(SIZE)]
top = -1

# 메인 함수
if __name__ == "__main__":

	colors = ['빨강','주황','노랑','초록','파랑','남색']

	print('과자집에 가는 길:',end=' ')
	for color in colors:
		push(color)
		print(f'{color}->',end=' ')
	print('과자집')

	print('우리집에 오는 길:',end=' ')
	for color in colors:
		color = pop()
		print(f'{color}->',end=' ')
	print('우리집')




































































