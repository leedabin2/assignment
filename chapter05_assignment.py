import random
import math
class Node():
	def __init__(self):
		self.data = None
		self.link = None

def store_name_distance(start) :
	current = start
	if current == None :
		return

	while current.link != head:
		current = current.link
		x, y = current.data[1:]
		print(f'{current.data[0]} 편의점, 거리 : {math.sqrt(x*x + y*y)}')


def  storelist(store) :
	global memory, head, current, pre

	node = Node()
	node.data = store

	if head == None :
		head = node
		node.link = head
		return

	node_x, node_y = node.data[1:]
	node_distance = math.sqrt(node_x*node_x + node_y*node_y)
	head_x, head_y = head.data[1:]
	head_distance = math.sqrt(head_x*head_x + head_y*head_y)

	if head_distance > node_distance :
		node.link = head
		last = head
		while last.link != head :
			last = last.link
		last.link = node
		head = node
		return

	current = head
	while current.link != head :
		pre = current
		current = current.link
		curx, cury= current.data[1:]
		cur_distance = math.sqrt(curx*curx + cury*cury)
		if cur_distance > node_distance :
			pre.link = node
			node.link = current
			return

	current.link = node
	node.link = head


memory = []
head, current, pre = None, None, None


if __name__ == "__main__" :

	store_array = []
	storename = 'A'
	for _ in range(10) :
		store = (storename, random.randint(1, 100), random.randint(1, 100))
		store_array.append(store)
		storename = chr(ord(storename) + 1)

	for store in store_array :
		storelist(store)

	store_name_distance(head)



































































