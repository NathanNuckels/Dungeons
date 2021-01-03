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
