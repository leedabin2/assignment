# 9.1
class graph() :
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printgraph(g):
	print(' ',end=' ')
	for v in range(5):
		print(store_array[v][0],end=' ')
	print('')
	for row in range(5):
		print(store_array[row][0],end= '    ')
		for col in range(5):
			print(g.graph[row][col],end='   ')
		print('')
	print('')

g1 = None
stack = []
visited_array = []
store_array= [['GS25', 30], ['CU', 60], ['7ELEVEN', 10], ['MINISTOP', 90], ['emart24', 40]]
GS25, CU , sevenELEVEN, MINISTOP, emart24 = 0, 1, 2, 3, 4


g1 = graph(5)
g1.graph[0][1] = 1; g1.graph[0][2] = 1
g1.graph[1][0] = 1;g1.graph[1][2] = 1;g1.graph[1][3] = 1
g1.graph[2][0] = 1; g1.graph[2][1] = 1; g1.graph[2][3] = 1
g1.graph[3][2] = 1; g1.graph[3][4] = 1
g1.graph[4][3] = 1

print('           < 편의점 그래프 >  ')
printgraph(g1)

current = 0
max_snack = current
maxcount = store_array[current][1]
stack.append(current)
visited_array.append(current)

while len(stack) != 0:
	next = None
	for vertex in range(5):
		if g1.graph[current][vertex] == 1:
			if vertex in visited_array:
				pass
			else:
				next = vertex
				break

	if next != None:
		current = next
		stack.append(current)
		visited_array.append(current)
		if store_array[current][1] > maxcount:
			maxcount = store_array[current][1]
			max_snack = current
	else:
		current = stack.pop()
print(f'허니버터칩 최대 보유 편의점(개수) : {store_array[max_snack][0]} ({store_array[max_snack][1]})')

print(' ')
# 9.2
class graph:
	def __init__ (self, size):
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printgraph(g):
	print(' ', end = ' ')
	for v in range(6) :
		print(cityAry[v], end = ' ')
	print()
	for row in range(6) :
		print(cityAry[row], end =' ')
		for col in range(6) :
			print(g.graph[row][col], end = '  ')
		print()
	print()

def findvertex(g, findvtx):
	stack = []
	visited_array = []

	current = 0
	stack.append(current)
	visited_array.append(current)

	while len(stack) != 0:
		next = None
		for vertex in range(6):
			if g.graph[current][vertex] != 0:
				if vertex in visited_array:
					pass
				else :
					next = vertex
					break

		if next != None:
			current = next
			stack.append(current)
			visited_array.append(current)
		else:
			current = stack.pop()

	if findvtx in visited_array:
		return True
	else :
		return False


g1 = None
cityAry = ['서울', '뉴욕', '런던', '북경', '방콕', '파리' ]
서울, 뉴욕, 런던, 북경, 방콕, 파리 = 0, 1, 2, 3, 4, 5



g1 = graph(6)
name_array = ['서울','뉴욕','북경','방콕','런던','파리']
서울,뉴욕,북경,방콕,런던,파리 = 0,1,2,3,4,5

g1 = graph(6)
g1.graph[서울][뉴욕] = 80;g1.graph[서울][북경] = 10
g1.graph[뉴욕][서울] = 80;g1.graph[뉴욕][북경] = 40;g1.graph[뉴욕][방콕] = 70
g1.graph[북경][서울] = 10;g1.graph[북경][뉴욕] = 40;g1.graph[북경][방콕] = 50
g1.graph[방콕][뉴욕] = 70;g1.graph[방콕][런던] = 30;g1.graph[방콕][북경] = 50;g1.graph[방콕][파리] = 20
g1.graph[런던][방콕] = 30;g1.graph[런던][파리] = 60
g1.graph[파리][방콕] = 20;g1.graph[파리][런던] = 60


print(' < 해저 케이블 연결을 위한 전체 연결도 >')
printgraph(g1)

# 가중치 간선 목록
edgearray = []
for i in range(6) :
	for k in range(6) :
		if g1.graph[i][k] != 0 :
			edgearray.append([g1.graph[i][k], i, k])

from operator import  itemgetter
edgearray = sorted(edgearray, key = itemgetter(0), reverse=False)

new_array = []
for i in range(0, len(edgearray), 2) :
	new_array.append(edgearray[i])

index = 0
while len(new_array) > 5:
	start = new_array[index][1]
	end = new_array[index][2]
	savecost = new_array[index][0]

	g1.graph[start][end] = 0
	g1.graph[end][start] = 0

	start_yn = findvertex(g1, start)
	end_yn = findvertex(g1, end)

	if start_yn and end_yn:
		del (new_array[index])
	else:
		g1.graph[start][end] = savecost
		g1.graph[end][start] = savecost
		index += 1

print(' < 가장 효율s적인 해저 케이블 연결도 >')
printgraph(g1)



