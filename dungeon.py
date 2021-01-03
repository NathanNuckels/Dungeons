import sys
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

	def save(self):
		print("Saveing...")
		with open(self.savePath,'w+') as f:
			f.write(str(self.day)+"\n"+str(self.hour)+"\n"+str(self.minute)+"\n"+self.name+"\n"+str(self.money)+"\n"+self.location+"\n"+str(self.inventory)+"\n")
		print("Done!")


	def tutorial(self):
		print("Welcome to Dungeons, a basic text game.")
		print("-- You are in a bright room. there is a table --")
		while True:
			print("TUTORIAL: Type \"view table\"")
			command=input("><>").strip().lower().split(" ")
			if len(command)==2:
				if (command[0]=="view" or command[0]=="v") and command[1]=="table":
					break
				else:
					print("TUTORIAL: You can't do that now.")
			else:
				print("TUTORIAL: You can't do that now.")
		print("TUTORIAL: Good! You can also type \"v\" for short.")
		print("-- On the table is a key and a ticket --")
		print("TUTORIAL: I would take the ticket. You might need it for later...")
		while True:
			print("TUTORIAL: Enter \"get ticket\"")
			command=input("><>").strip().lower().split(" ")
			if len(command)==2:
				if (command[0]=="get" or command[0]=="g") and command[1]=="ticket":
					break
				else:
					print("TUTORIAL: You can't do that now.")
			else:
				print("TUTORIAL: You can't do that now.")
		self.inventory=[["ticket",1]]
		print("SYSTEM gave yoy TICKET x 1")
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
		print("TUTORIAL: I guess you should take the key. try to do it with out me telling")
		print("you what to type")
		while True:
			command=input("><>")
			if command=="get key" or command=="g key": #This direct way will only be used for tutorials
				break
			else:
				print("TUTORIAL: You can't do that now.")
		self.inventory=[["ticket",1],["key",1]]
		print("SYSTEM gave you a KEY x 1")
		print("TUTORIAL: Well... now what? There might be more stuff in the room")
		print("that you dont know about. Try listing the objects.")
		while True:
			print("TUTORIAL: List objects with \"list obj\" or \"l o\"")
			command=input("><>").strip().lower().split(" ")
			if len(command)==2:
				if command[1]=="object" or command[1]=="objects":
					print("Hint: type \"obj\"")
				if command==["l","obj"] or command==["list","o"]:
					print("Tip: Dont combine the long and short versions of commands.")
					print("THe code processing commands might not catch it.")
				if command==["list","obj"] or command==["l","o"]:
					break
				else:
					print("TUTORIAL: You cant do that now.")
			else:
				print("TUTORIAL: You can't do that now.")
		print("table\ndoor")
		print("TUTORIAL: Note that you can also list caracters (l c) and your inventory (l i)")
		print("TUTORIAL: The key might go with the door! try putting it in!")
		while True:
			print("TUTORIAL: enter \"use key on door\" or \"u key > door\"")
			command=input("><>").lower().strip().split(" ")
			if len(command)==4:
				if command[0]=="use" and command[1]=="key" and command[3]=="door":
					break
				else:
					print("TUTORIAL: You can't do that now.")
			else:
				print("TUTORIAL: You can't do that now.")
		print("Tip: Normally, you don't want to mix short and long commands but")
		print("this is an exeption. You CAN enter \"u key on door\" if you want.")
		print("-- The door opens --")
		print("TUTORIAL: Use \"walk\" or \"w\" to move")
		while True:
			print("TUTORIAL: Use \"w outside\"")
			command=input("><>")
			if command=="w outside" or command=="walk outside":
				break
			else:
				print("TUTORIAL: You can't do that now.")
		print("-- You walk outside. There is a bus --")
		print("TUTORIAL: Go to the bus. You know what to do!")
		while True:
			command=input("><>").lower()
			if command=="walk bus" or command=="w bus":
				break
			else:
				print("TUTORIAL: You can't do that now.")
		print("SYSTEM: You you 1) walk in the bus or 2) walk to the bus")
		print("TUTORIAL: Sometimes the game will want more information. Pick 1")
		while True:
			command=input("><>")
			if command=="1":
				break
			else:
				print("TUTORIAL: Pick 1")
		print("-- You walk in the bus --")
		print("BUS-DRIVER: Got a ticket?")
		print("TUTORIAL: To give someone an item, you can use \"give\". Instead of shortening")
		print("to \"g\" it shortens to \"gv\"")
		while True:
			print("TUTORIAL: Use \"give ticket to bus-driver\" or \"gv ticket > bus-driver\"")
			command=input("><>").lower().split(" ")
			if len(command)==4:
				if command[0]=="give" or command=="gv":
					if command[1]=="ticket":
						if len(command)==2:
							print("SYSTEM: Give ticket to who?")
						else:
							if command[3]=="bus-driver":
								break
							else:
								print("SYSTEM: That player isn't here")
					else:
						print("SYSTEM: You do not have that item.")
			else:
				print("TUTORIAL: You can't do that now.")
		print(self.name.upper()+": Here.")
		print("BUS-DRIVER: To... where is this?")
		print(" --- And the story goes deeper... --- ")
		print("TUTORIAL: You should save.")
		print(".....\n")
		print(self.savePath)
		self.displaySave()
		print("\n")
		self.day=0
		self.hour=20
		self.minute=0
		self.location="hill"
		self.money=3000
		self.inventory=[]
		self.displaySave()
		print("SYSTEM: Would you like to save the game?")
		choice=input("[y/N] ><>").lower()
		if choice=="y" or choice=="yes":
			self.save()
		else:
			print("SYSTEM: Are you sure? the game will exit after the tutorial!")
			choice=input(" ![Y/n]! ><>").lower()
			if choice=="y" or choice=="yes" or choice=="":
				self.save()
		sys.exit()
