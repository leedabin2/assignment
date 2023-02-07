# 7.1
def isqueuefull():
	global SIZE, queue, front, rear
	if rear == SIZE-1:
		return True
	else:
		return False


def isqueueempty():
	global SIZE, queue, front, rear
	if front == rear:
		return True
	else:
		return False

def enqueue(data):
	global SIZE, queue, front, rear
	if isqueuefull():
		print('만석입니다')
		return
	rear += 1
	queue[rear] = data

def dequeue():
	global SIZE, queue, front, rear
	if isqueueempty():
		print('대기 손님이 없습니다')
		return None
	front += 1
	data = queue[front]
	queue[front] = None

	for i in range(front+1,rear+1):
		queue[i-1] = queue[i]
		queue[i] = None
	front = -1
	rear -= 1

	return data

def peek():
	global SIZE, queue, front, rear
	if isqueueempty():
		print('대기 손님이 없습니다')
		return None

	return queue[front+1]

SIZE = 5
queue = [None for _ in range(SIZE)]
front = -1
rear = -1

if __name__ == "__main__":
	enqueue('정국')
	enqueue('뷔')
	enqueue('지민')
	enqueue('진')
	enqueue('슈가')
	print('대기 줄 상태 : ',queue)

	for _ in range(rear+1):
		print(f'{dequeue()}님 식당에 들어감')
		print(f'대기 줄 상태 : {queue}')


print('식당 영업 종료')

# 7.2
def isqueuefull():
	global front, rear, SIZE, queue
	if (rear+1) % SIZE == front:
		return True
	return False

def isqueueempty():
	global front, rear, SIZE, queue
	if front == rear:
		return True
	return False

def enqueue(data):
	global front, rear, SIZE, queue
	if isqueuefull():
		print('대기 있음')
		return
	rear = (rear+1) % SIZE
	queue[rear] = data

def dequeue():
	global front, rear, SIZE, queue
	if isqueueempty():
		print('대기 없음')
		return None
	front = (front+1) % SIZE
	data = queue[front]
	queue[front] = None
	return data

def peek():
	global front, rear, SIZE, queue
	if isqueueempty():
		print('대기 없음')
		return None
	return queue[(front+1) % SIZE]

def esttime() :
	global front, rear, SIZE, queue
	sum = 0
	for i in range((front+1)% SIZE,(rear+1)%SIZE):
		sum += queue[i][1]
	return sum


SIZE = 6
queue = [None for _ in range(SIZE)]
front = 0
rear = 0


if __name__ == "__main__" :
	waittime = [('사용',9), ('고장',3), ('환불',4), ('환불',4), ('고장',3)]

	for call in waittime :
		print(f'귀하의 대기 예상시간은 {esttime()} 분입니다.')
		print(f'현재 대기 콜 : {queue}')
		enqueue(call)
		print(' ')
	print(f'최종 대기 콜 : {queue}')
	print("프로그램 종료!")

# 8.1
import random

class Treenode() :
	def __init__ (self) :
		self.left = None
		self.data = None
		self.right = None

root = None
snack_array = ['레쓰비캔커피','도시락','삼각김밥','코카콜라','삼다수','츄파츕스']
sell_amount = int(input('판매양:'))
sell_array = [random.choice(snack_array) for _ in range(sell_amount)]

print('오늘 판매된 물건(중복O) : ',sell_array)



node = Treenode()
node.data = sell_array[0]
root = node


for snack in sell_array[1:] :

	node = Treenode()
	node.data = snack

	current = root
	while True :
		if snack == current.data :
			break
		if snack < current.data :
			if current.left == None :
				current.left = node
				break
			current = current.left
		else :
			if current.right == None :
				current.right = node
				break
			current = current.right

print("이진 탐색 트리 구성 완료!")

def preorder(node) :
	if node == None :
		return
	print(node.data,end=' ')
	preorder(node.left)
	preorder(node.right)

print('오늘 판매된 종류(중복X) : ',end=' ')
preorder(root)