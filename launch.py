import dungeon

with open("developer-settings","r") as f:
	for line in f:
		line=line.strip().split("=")
		if line[0]=="debug":
			env_debug=line[1]=="true"
newsave=False

def debug(message):
	if env_debug:
		print("[Debug] "+message)

while True:
	print("Welcome to DUNGEONS!")
	print()
	print("Enter path to a save or type \"New\" or \"Quit\"")
	choice=imput("><>")
	if choice.lower()=="new":
		print("00:00 Day 00 Level 00")
		print("The Hill")
		print("----------, $----")
		print()
		choice=input("Create new save? [Y/n] ")
		choice=choice.lower()
		if choice=="" or choice=="y" or choice=="yes":
			newsave=True
			break
	elif choice.lower()=="exit" or choice.lower()=="quit":
		print("OK, Bye!")
	else:
		print("Sorry, we don't support loading and saveing yet...")

if newsave:
	while True:
		print("Enter a name:")
		playername=input("  >>")
		if playername=="":
			print("Error 001: Name cannot be empty")
		elif len(playername)>10:
			print("Error 002: Name must be 10 or less letters.")
		elif len(playername)<2:
			print("Error 003: Name must be at least three letters.")
		else:
			print("Cool name!")
			break
print("One moment...")
debug("Set hour to 20")
debug("Set minute to 0")
debug("Set name to \""+playername"\"")
debug("Set money to 3000")
debug("Set location to \"hill\"")
thisGame=new dungeon.Game()
thisGame.setSave(20,0,playername,300,"hill")
main.start(thisGame)
