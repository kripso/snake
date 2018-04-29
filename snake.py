import tkinter,random,time
class game():

	def __init__(self):
		self.canvasWidth=1500
		self.canvasHeight=900

		self.canvas=tkinter.Canvas(width=self.canvasWidth,height=self.canvasHeight,bg='white')
		self.canvas.pack()

		self.margin=10
		self.control=1
		self._control=0
		self.move=0
		self.n=-1
		self.n1=-1
		self.fruit_number=0
		self._fruit_number=[0]
		self.i=-1
		self.i1=-1

		self.canvas.create_text(self.canvasWidth/2,self.margin,text=''+str(self.n-self.i+1),tags='text')

		self.grid()
		self.snake()
		self.add_fruits()
		self.add_fruits()
		self.add_fruits()
		self.snake_move()

		self.canvas.bind_all('<Left>',self.moveleft)
		self.canvas.bind_all('<Right>',self.moveright)
		self.canvas.bind_all('<Up>',self.moveup)
		self.canvas.bind_all('<Down>',self.movedown)
		self.canvas.bind_all('<space>',self.add_lenght)

		self.canvas.mainloop()


	def grid(self):
		self._grid=self.canvas.create_rectangle(0+self.margin*2-1,0+self.margin*6-1,self.canvasWidth-self.margin*2+1,self.canvasHeight-self.margin*2+1,tags='grid')

	def snake(self):
		self.canvas.create_oval(self.canvasWidth/2-self.margin,self.canvasHeight/2-self.margin+self.margin,
								self.canvasWidth/2+self.margin,self.canvasHeight/2+self.margin+self.margin,
								tags='snake'+str(self.n+1))
	def add_lenght(self):
		x1, y1, x2, y2 = self.canvas.coords('snake'+str(self.n))

		self.n+=1

		if self.move==1:
			self.canvas.create_oval(x1-self.margin/2-2,y1,
									x2-self.margin/2-2,y2,
									tags='snake'+str(self.n),fill='red')

		elif self.move==2:
			self.canvas.create_oval(x1+self.margin/2+2,y1,
									x2+self.margin/2+2,y2,
									tags='snake'+str(self.n),fill='blue')
		
		elif self.move==3:
			self.canvas.create_oval(x1,y1-self.margin/2-2,
									x2,y2-self.margin/2-2,
									tags='snake'+str(self.n),fill='green')
		

		elif self.move==4:
			self.canvas.create_oval(x1,y1+self.margin/2+2,
									x2,y2+self.margin/2+2,
									tags='snake'+str(self.n),fill='black')
	def add_fruits(self):

		x1=random.randrange(0+self.margin*3+1, self.canvasWidth-self.margin*3-1,self.margin)
		y1=random.randrange(0+self.margin*7+1, self.canvasHeight-self.margin*3-1,self.margin)

		self.canvas.create_oval(x1-self.margin,y1-self.margin,x1+self.margin,y1+self.margin,fill='orange',tags='fruit'+str(self.fruit_number))
		self.fruit_number+=1
		self._fruit_number.append(self.fruit_number)

	def snake_move(self):

		if self.move!=0:
			self.n+=1
			self.i+=1
			self.canvas.delete('text')
			self.canvas.create_text(self.canvasWidth/2,self.margin,text=''+str(self.n-self.i+1),tags='text')


			x1, y1, x2, y2 = self.canvas.coords('snake'+str(self.n))

			#narazenie


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

			if x1<=0+self.margin*2-1 or x2>=self.canvasWidth-self.margin*2+1 or y1<=0+self.margin*6-1 or y2 >=self.canvasHeight-self.margin*2+1:
				if self.control==1:
					self.canvas.after(35,self.snake_move)

					if self.move==1:
						self.canvas.create_oval(self.canvasWidth-self.margin*2-self.margin*2,y1,
												self.canvasWidth-self.margin*2,y2,
												tags='snake'+str(self.n+1),fill='red')
					
						self.canvas.delete('snake'+str(self.i))

					elif self.move==2:
						self.canvas.create_oval(0+self.margin*2+self.margin*2,y1,
												0+self.margin*2,y2,
												tags='snake'+str(self.n+1),fill='blue')
					
						self.canvas.delete('snake'+str(self.i))
					elif self.move==3:
						self.canvas.create_oval(x1,self.canvasHeight-self.margin*2-self.margin*2-2,
												x2,self.canvasHeight-self.margin*2,
												tags='snake'+str(self.n+1),fill='green')
					
						self.canvas.delete('snake'+str(self.i))

					elif self.move==4:
						self.canvas.create_oval(x1,0+self.margin*6,
												x2,0+self.margin*6+self.margin*2+2,
												tags='snake'+str(self.n+1),fill='black')
					
						self.canvas.delete('snake'+str(self.i))
			else:
				if self.control==1:
					self.canvas.after(35,self.snake_move)

					if self.move==1:
						self.canvas.create_oval(x1-self.margin/2-2,y1,
												x2-self.margin/2-2,y2,
												tags='snake'+str(self.n+1),fill='red')
					
						self.canvas.delete('snake'+str(self.i))

					elif self.move==2:
						self.canvas.create_oval(x1+self.margin/2+2,y1,
												x2+self.margin/2+2,y2,
												tags='snake'+str(self.n+1),fill='blue')
					
						self.canvas.delete('snake'+str(self.i))
					elif self.move==3:
						self.canvas.create_oval(x1,y1-self.margin/2-2,
												x2,y2-self.margin/2-2,
												tags='snake'+str(self.n+1),fill='green')
					
						self.canvas.delete('snake'+str(self.i))

					elif self.move==4:
						self.canvas.create_oval(x1,y1+self.margin/2+2,
												x2,y2+self.margin/2+2,
												tags='snake'+str(self.n+1),fill='black')
					
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
				self.canvas.after(90,self.pause_for_moving)

	def moveright(self,event):
		if self._control==0:
			if self.move!=1:
				self.move=2
				self._control=1
				self.canvas.after(90,self.pause_for_moving)

	def moveup(self,event):
		if self._control==0:
			if self.move!=4:
				self.move=3
				self._control=1
				self.canvas.after(90,self.pause_for_moving)

	def movedown(self,event):
		if self._control==0:
			if self.move!=3:
				self.move=4
				self._control=1
				self.canvas.after(90,self.pause_for_moving)

game()