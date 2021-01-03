import main
import dungeon

with open("developer-settings","r") as f:
	for line in f:
		line=line.strip().split("=")
		if line[0]=="debug":
			env_debug=line[1]=="true"
newsave=False
def writeEmpty(path):
	global playername
	with open(path,'w+') as f:
		f.write("0\n20\n0\n"+playername+"\n3000\nhill\n[]")
def debug(message):
	if env_debug:
		print("[Debug] "+message)

while True:
	print("Welcome to DUNGEONS!")
	print()
	print("Enter path to a save or type \"New\" or \"Quit\"")
	choice=input("><>")
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
if newsave:
	print("Enter path to save game:")
	path=input("><>")
	print("One moment...")
	debug("Set hour to 20")
	debug("Set minute to 0")
	debug("Set name to \""+playername+"\"")
	debug("Set money to 3000")
	debug("Set location to \"hill\"")
	print("Creating game...")
	thisGame=dungeon.Game()
	print("Saveing game...")
	writeEmpty(path)
	print("Loading game...")
	thisGame.setSave(path)
	print("Lets go!\n")
	main.start(thisGame)
