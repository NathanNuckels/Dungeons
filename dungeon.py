class Game:
	def __init__(self):
		self.hour=0
		self.minute=0
		self.day=0
		self.name=""
		self.money=0
		self.location=""
		self.inventory=[]
		self.savePath=""
	def setSave(self,save):
		self.savePath=save		
		file=[]
		with open(save,"r") as f:
			for line in f:
				file.append(line.strip())
		self.day=int(file[0])
		self.hour=int(file[1])
		self.minute=int(file[2])
		self.name=file[3]
		self.money=int(file[4])
		self.location=file[5]
		self.inventory=eval(file[6])
		print("Day is "+str(self.day)+", TIme is "+str(self.hour)+":"+str(self.minute))
		print(self.name.upper()+" at "+self.location+" with $"+str(self.money))
		print("Holding:")
		print(self.inventory)
