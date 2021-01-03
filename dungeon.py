#dungeon.locationToString: A look up table for converting location ids to their names.
def locationToString(loc):
	if loc=="tutorial":
		return "Tutorial"
	elif loc=="hill":
		return "The Hill"
	else:
		return "Invalid Location"

#dungeon.Game: Most of the game data is stored here.
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

	#Displays a save card
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

	#Sets a save path and loads it
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


	def tutorial(self):
		print("Welcome to Dungeons, a basic text game.")
		print("-- You are in a bright room. there is a table --")
		while True:
			print("TUTORIAL: Type \"view table\"")
			command=input("><>").strip().lower().split(" ")
			if (command[0]=="view" or command[0]=="v") and command[1]=="table":
				break
			else:
				print("TUTORIAL: You can't do that now.")
		print("TUTORIAL: Good! You can also type \"v\" for short.")
		print("-- On the table is a key and a ticket --")
		print("TUTORIAL: I would take the ticket. You might need it for later...")
		while True:
			print("TUTORIAL: Enter \"get ticket\"")
			command=input("><>").strip().lower().split(" ")
			if (command[0]=="get" or command[0]=="g") and command[1]=="ticket"):
				break
			else:
				print("TUTORIAL: You can't do that now.")
		print("TUTORIAL: Good! Like \"view\" can be \"v\", \"get\" can be shortened to \"g\"")
		print("-- You take the ticket. --")
		print("TUTORIAL: I wonder what kind of key it is. Is it a house hey?") 
		print("Somthing mystic? Take a closer look.") 
		while True:
			print("TUTORIAL: Type \"v key\"")
			command=input("><>").strip().lower().split(" ")
			if command==["v", "key"]:
				break
			elif command[0]=="view":
				print("TUTORIAL: Try useing the shortened version.")
			else:
				print("TUTORIAL: You can't do that now.")
		print("-- The key is like a house key. 'brass` you assume. --")
		print("TUTORIAL: Well... now what? There might be more stuff in the room")
		print("that you dont know about. Try listing the objects.")
		while True:
			print("TUTORIAL: List objects with \"list obj\" or \"l o\"")
			command=input("><>").strip().lower().split(" ")
			if command[1]=="object" or command[1]=="objects":
				print("Hint: type \"obj\"")
			if command==["l","obj"] or command==["list","o"]:
				print("Tip: Dont combine the long and short versions of commands.")
				print("THe code processing commands might not catch it.")
			if command
