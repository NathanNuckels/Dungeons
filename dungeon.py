def locationToString(loc):
	if loc=="hill":
		return "The Hill"
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


	def displaySave(self):
		strHour=("0"*(2-len(str(self.hour))))+str(self.hour)
		strMinute=("0"*(2-len(str(self.minute))))+str(self.minute)
		strDay=("0"*(3-len(str(self.day))))+str(self.day)
		strName=self.name+("_"*(10-len(self.name)))
		strMoney=("0"*(4-len(str(self.money))))+str(self.money)
		strLoc=locationToString(self.location)
		strItems=("0"*(2-len(self.inventory)))+str(len(self.inventory))
		print()
		print(strHour+":"+strMinute+" Day "+strDay)
		print(strLoc)
		print(strName+", $"+strMoney+", "+strItems+" Items")
		print()


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
		self.displaySave()
