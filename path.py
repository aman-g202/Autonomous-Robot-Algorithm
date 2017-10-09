from random import randint

class Node:
 
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1
        self.t_l = 0
        self.t_f = 0
        self.t_r = 0
        self.t_b = 0
        self.front = None
        self.back = None
        self.left = None
        self.right = None  
        self.next = None
        self.vertex = 0

class LinkedList:

	def __init__(self):
		self.head = None
		self.end = None
		self.slist = []
		self.temp = 0
		self.countnode = 1
		self.vertexcount = 0

	def append(self, x1, y1, t1, *sdata):
		new_node = Node(x1,y1)
		print(hex(id(new_node)))
		sdata = list(sdata)
		self.countnode = 1
		new_node.vertex = self.vertexcount
		self.vertexcount += 1

		# Conditions to take the decision for the robot wheather to go LEFT, FRONT, RIGHT

		if(sdata.count(1) > 2):
			if(sdata[1] == 1 and sdata[3] == 1 and sdata[4] == 0):
				guess = randint(1,2)
				if(guess == 1):
					sdata[1] = 0
				elif(guess == 2):
					sdata[3] = 0
			
			elif(sdata[1] == 1 and sdata[4] == 1 and sdata[3] == 0):
				guess = randint(1,2)
				if(guess == 1):
					sdata[1] = 0
				elif(guess == 2):
					sdata[4] = 0

			elif(sdata[1] == 1 and sdata[3] == 1 and sdata[4] == 1):
				guess = randint(1,3)
			
				if(guess == 1):
					sdata[1] = 0
					sdata[4] = 0
				elif(guess == 2):
					sdata[3] = 0
					sdata[4] = 0
				elif(guess == 3):
					sdata[1] = 0
					sdata[3] = 0					
		print(sdata)		

		# <!----------------------------------------------------------------------------------------!>

		if(self.temp == 0):
			self.slist = sdata
			self.temp = 1
		else:
			if(self.slist[1] == 1 and self.slist[3] == 0 and self.slist[4] == 0):
				new_node.back = self.end  # mapping addresses between current and previous node
				self.end.front = new_node	# mapping addresses between current and previous node
				self.slist = sdata
				new_node.t_f = t1     # To set time taken to visit next front node

			elif(self.slist[4] == 1 and self.slist[1] == 0 and self.slist[3] == 0):
				new_node.back = self.end  # mapping addresses between current and previous node
				self.end.right = new_node	# mapping addresses between current and previous node 
				self.slist = sdata
				new_node.t_r = t1	# To set time taken to visit next right node

			elif(self.slist[3] == 1 and self.slist[1] == 0 and self.slist[4] == 0):
				new_node.back = self.end	# mapping addresses between current and previous node
				self.end.left = new_node	# mapping addresses between current and previous node
				self.slist = sdata
				new_node.t_l = t1	# To set time taken to visit next left node
			# print(self.slist)	


		if self.head is None:       # To set pointer to First Node
			self.head = new_node 
			self.end = new_node
			# print(hex(id(self.end)))
			return

		last = self.head
		while last.next:
			last = last.next
		
		last.next = new_node
		self.end = new_node

		# print(hex(id(self.end)))
		# print(self.end.x)
		# print(hex(id(new_node.left)))

		checknode = self.head
		while checknode.next:
			if(abs(x1 - checknode.x) < 0.05 and abs(y1 - checknode.y) < 0.05):
				print("Oouch! we already came to this node, This is node - {0}".format(self.countnode))
			self.countnode+=1	
			checknode = checknode.next	

	def atPos(self, x1, y1, t1, pos):

		# new_node = Node(x1,y1,t1)

		move = self.head

		for i in range(1,pos):
			move = move.next

		move.x = x1
		move.y = y1
		move.t = t1
			

	def printList(self):
		temp = self.head
		while (temp):
			print('node - {0} : {1} {2} {3} {4} {5} {6}'.format(temp.vertex, temp.x, temp.y,
			 hex(id(temp.left)), hex(id(temp.front)), hex(id(temp.right)), hex(id(temp.back))))
			print( "Time Taken :")
			print('{0} {1} {2} {3}'.format(temp.t_l,temp.t_f,temp.t_r,temp.t_b))
			temp = temp.next

if(__name__ == '__main__'):
		
	llist = LinkedList()
	llist.append(1,2,0.1,0,0,0,0,1,0,1,0)
	llist.append(3,6,0.2,0,0,0,1,0,0,1,0)
	llist.append(3.03,6.04,0.3,0,1,0,1,1,0,1,0)

	# llist.atPos(10,30,1.1,2)

	llist.printList()		