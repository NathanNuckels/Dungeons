import sys
import dungeon
def generateSaveCard(path):
	file=[]
	with open(path,"r") as f:
		for line in f:
			file.append(line.strip())
	strHour=("0"*(2-len(file[1])))+file[1]
	strMinute=("0"*(2-len(file[2])))+file[2]
	strDay=("0"*(3-len(file[0])))+file[0]
	strName=file[3]+("_"*(10-len(file[3])))
	strMoney=("0"*(4-len(file[4])))+file[4]
	strLoc=dungeon.locationToString(file[5])
	strItems=("0"*(2-len(eval(file[6]))))+str(len(eval(file[6])))
	print()
	print(strHour+":"+strMinute+" Day "+strDay)
	print(strLoc)
	print(strName+", $"+strMoney+", "+strItems+" Items")
	print()
	
def start(game):
	if game.location=="tutorial":
		game.tutorial()
	else:
		print("Nathan: I havn't programed that path yet.")
		print("\n1 "+game.name.upper()+": Ok, I'll just leave here.")
		input()
		sys.exit()
