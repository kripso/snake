import tkinter,random,time
class game():

	def __init__(self):
		self.canvasWidth=900
		self.canvasHeight=800

		self.canvas=tkinter.Canvas(width=self.canvasWidth,height=self.canvasHeight,bg='white')
		self.canvas.pack()

		self.margin=10
		self.max_lenght=1
		self.init()

		button = tkinter.Button (width=15,height=2,  text='New game', font='Arial 15 bold', activeforeground='#1010D2', command=self.grid)
		button.place (x=self.canvasWidth/2-self.canvasWidth/4, y=(0+self.margin*6-1)/2, anchor="c")

		self.grid()
		self.snake_move()

		self.canvas.bind_all('<Left>',self.moveleft)
		self.canvas.bind_all('<Right>',self.moveright)
		self.canvas.bind_all('<Up>',self.moveup)
		self.canvas.bind_all('<Down>',self.movedown)

		self.canvas.mainloop()

	def init(self):
		self.control=1
		self._control=0
		self.move=0
		self.n=-1
		self.n1=-1
		self.obs_number=0
		self.obs_coords=[]
		self.fruit_number=0
		self._fruit_number=[0]
		self.i=-1
		self.i1=-1
		self.n=-1
		self.i=-1
		self.canvas.create_text(self.canvasWidth/2,(0+self.margin*6-1)/2,text='Actual length: '+str(self.n-self.i+1),font='Arial 20 bold', tags='text')
		self.canvas.create_text(self.canvasWidth/4+self.canvasWidth/2,(0+self.margin*6-1)/2,text='Max length: '+str(self.max_lenght),font='Arial 20 bold', tags='text')

	def grid(self):
		self.canvas.delete('all')

		if self.control==0:
			self.init()
			self.snake_move()

		self.init()

		self._grid=self.canvas.create_rectangle(0+self.margin*2-1,0+self.margin*6-1,self.canvasWidth-self.margin*2+1,self.canvasHeight-self.margin*2+1,tags='grid')

		self.snake()
		n=(int((self.canvasHeight/100)*(self.canvasWidth)/100))//2
		print(n)
		for i in range(int(n)):	
			self.obstacles()
		
		for i in range(3):
			self.add_fruits()

	def obstacles(self):

		x=random.randrange(0+self.margin*3+1, self.canvasWidth-self.margin*3-1,self.margin)
		y=random.randrange(0+self.margin*7+1, self.canvasHeight-self.margin*3-1,self.margin)

		self.canvas.create_rectangle(x-self.margin,y-self.margin,x+self.margin,y+self.margin,fill='black',tags='obs'+str(self.obs_number))
		self.obs_number+=1
		self.obs_coords.append([x,y])

		tagged_objects = self.canvas.find_withtag('snake'+str(self.n+1))
		overlapping_objects = self.canvas.find_overlapping(*self.canvas.coords('obs'+str(self.obs_number-1)))
		
		if tagged_objects[0] == overlapping_objects[0]:
			self.obs_number-=1
			self.obs_coords.remove(self.obs_coords[len(self.obs_coords)-1])
			self.canvas.delete('obs'+str(self.obs_number))
			self.obstacles()


	def snake(self):
		self.canvas.create_oval(self.canvasWidth/2-self.margin,self.canvasHeight/2-self.margin+self.margin,
								self.canvasWidth/2+self.margin,self.canvasHeight/2+self.margin+self.margin,
								tags='snake'+str(self.n+1),fill='blue')
	def add_lenght(self):
		x1, y1, x2, y2 = self.canvas.coords('snake'+str(self.n))

		self.n+=1

		if self.move==1:
			self.canvas.create_oval(x1-self.margin/2-2,y1,
									x2-self.margin/2-2,y2,
									tags='snake'+str(self.n),fill='blue')

		elif self.move==2:
			self.canvas.create_oval(x1+self.margin/2+2,y1,
									x2+self.margin/2+2,y2,
									tags='snake'+str(self.n),fill='blue')
		
		elif self.move==3:
			self.canvas.create_oval(x1,y1-self.margin/2-2,
									x2,y2-self.margin/2-2,
									tags='snake'+str(self.n),fill='blue')
		
		elif self.move==4:
			self.canvas.create_oval(x1,y1+self.margin/2+2,
									x2,y2+self.margin/2+2,
									tags='snake'+str(self.n),fill='blue')
	def add_fruits(self):

		x1=random.randrange(0+self.margin*3+1, self.canvasWidth-self.margin*3-1,self.margin)
		y1=random.randrange(0+self.margin*7+1, self.canvasHeight-self.margin*3-1,self.margin)

		self.canvas.create_oval(x1-self.margin,y1-self.margin,x1+self.margin,y1+self.margin,fill='red',tags='fruit'+str(self.fruit_number))

		self.fruit_number+=1
		self._fruit_number.append(self.fruit_number)

		for i in range(len(self.obs_coords)):
			tagged_objects1 = self.canvas.find_withtag('obs'+str(i))
			overlapping_objects1 = self.canvas.find_overlapping(*self.canvas.coords('fruit'+str(self.fruit_number-1)))

			for item in overlapping_objects1:
				if item in tagged_objects1:
					self.canvas.delete('fruit'+str(self.fruit_number-1))
					self.add_fruits()

	def snake_move(self):

		if self.move!=0:
			self.n+=1
			self.i+=1
			self.canvas.delete('text')
			self.canvas.create_text(self.canvasWidth/2,(0+self.margin*6-1)/2,text='Actual length: '+str(self.n-self.i+1),font='Arial 20 bold', tags='text')

			if self.n-self.i+1 > self.max_lenght:
				self.max_lenght+=1
			self.canvas.create_text(self.canvasWidth/4+self.canvasWidth/2,(0+self.margin*6-1)/2,text='Max length: '+str(self.max_lenght),font='Arial 20 bold', tags='text')
				

			x1, y1, x2, y2 = self.canvas.coords('snake'+str(self.n))

			#narazenie

			for i in range(len(self.obs_coords)):
				tagged_objects1 = self.canvas.find_withtag('obs'+str(i))
				overlapping_objects1 = self.canvas.find_overlapping(*self.canvas.coords('snake'+str(self.n)))

				for item in overlapping_objects1:
					if item in tagged_objects1:
						print('game over')
						self.control=0
						
			#zjedenie seba
			if self.n-1 - self.i>4:
				for i in range(self.i,self.n-7):
					tagged_objects = self.canvas.find_withtag('snake'+str(self.n))
					overlapping_objects = self.canvas.find_overlapping(*self.canvas.coords('snake'+str(i)))

					for item in overlapping_objects:
						if item in tagged_objects:
							for x in range(self.i,i+1):
								self.canvas.delete('snake'+str(x))
							self.i=i
			#zjedenie ovocia
			for i in range(len(self._fruit_number)):
				tagged_objects1 = self.canvas.find_withtag('fruit'+str(self._fruit_number[i]))
				overlapping_objects1 = self.canvas.find_overlapping(*self.canvas.coords('snake'+str(self.n)))

				for item in overlapping_objects1:
					if item in tagged_objects1:
						self.add_lenght()
						self.canvas.delete('fruit'+str(self._fruit_number[i]))
						self.add_fruits()
					
	#		print(y2,self.canvasHeight-self.margin*2+self.margin+1,self.canvasHeight-self.margin*2+self.margin+1-y2==25,self.canvasHeight-self.margin*2+self.margin+1-y2==15)

	#		if  0+self.margin*2-self.margin-1-x1==15 or x2-self.canvasWidth-self.margin*2+self.margin+1==15 or y1-0+self.margin*6-self.margin-1==15 or y1-0+self.margin*6-self.margin-1==11 or self.canvasHeight-self.margin*2+self.margin+1-y2==15:
	#			self._control=1
	#			self.canvas.after(30,self.pause_for_moving)

			if x1<=0+self.margin*2-1 or x2>=self.canvasWidth-self.margin*2+1 or y1<=0+self.margin*6-1 or y2 >=self.canvasHeight-self.margin*2+1:

				if self.control==1:
					self.canvas.after(35,self.snake_move)

					if self.move==1:
						self.canvas.create_oval(self.canvasWidth-self.margin*2-self.margin*2,y1,
												self.canvasWidth-self.margin*2,y2,
												tags='snake'+str(self.n+1),fill='blue')
					
						self.canvas.delete('snake'+str(self.i))

					elif self.move==2:
						self.canvas.create_oval(0+self.margin*2+self.margin*2,y1,
												0+self.margin*2,y2,
												tags='snake'+str(self.n+1),fill='blue')
					
						self.canvas.delete('snake'+str(self.i))
					elif self.move==3:
						self.canvas.create_oval(x1,self.canvasHeight-self.margin*2-self.margin*2-2,
												x2,self.canvasHeight-self.margin*2,
												tags='snake'+str(self.n+1),fill='blue')
					
						self.canvas.delete('snake'+str(self.i))

					elif self.move==4:
						self.canvas.create_oval(x1,0+self.margin*6,
												x2,0+self.margin*6+self.margin*2+2,
												tags='snake'+str(self.n+1),fill='blue')
					
						self.canvas.delete('snake'+str(self.i))
			else:
				if self.control==1:
					self.canvas.after(35,self.snake_move)

					if self.move==1:
						self.canvas.create_oval(x1-self.margin/2-2,y1,
												x2-self.margin/2-2,y2,
												tags='snake'+str(self.n+1),fill='blue')
					
						self.canvas.delete('snake'+str(self.i))

					elif self.move==2:
						self.canvas.create_oval(x1+self.margin/2+2,y1,
												x2+self.margin/2+2,y2,
												tags='snake'+str(self.n+1),fill='blue')
					
						self.canvas.delete('snake'+str(self.i))
					elif self.move==3:
						self.canvas.create_oval(x1,y1-self.margin/2-2,
												x2,y2-self.margin/2-2,
												tags='snake'+str(self.n+1),fill='blue')
					
						self.canvas.delete('snake'+str(self.i))

					elif self.move==4:
						self.canvas.create_oval(x1,y1+self.margin/2+2,
												x2,y2+self.margin/2+2,
												tags='snake'+str(self.n+1),fill='blue')
					
						self.canvas.delete('snake'+str(self.i))
		else:
			self.canvas.after(50,self.snake_move)
			
	def pause_for_moving(self):
		self._control=0

	def moveleft(self,event):
		if self._control==0:
			if self.move!=2:
				self.move=1
				self._control=1
				self.canvas.after(35,self.pause_for_moving)


	def moveright(self,event):
		if self._control==0:
			if self.move!=1:
				self.move=2
				self._control=1
				self.canvas.after(35,self.pause_for_moving)

	def moveup(self,event):
		if self._control==0:
			if self.move!=4:
				self.move=3
				self._control=1
				self.canvas.after(35,self.pause_for_moving)

	def movedown(self,event):
		if self._control==0:
			if self.move!=3:
				self.move=4
				self._control=1
				self.canvas.after(35,self.pause_for_moving)

game()