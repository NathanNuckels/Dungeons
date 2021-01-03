import main
import dungeon

#Load if debug is on
with open("developer-settings","r") as f:
	for line in f:
		line=line.strip().split("=")
		if line[0]=="debug":
			env_debug=line[1]=="true"

newsave=False

#writeEmpty: Writes an empty save file
def writeEmpty(path):
	global playername
	with open(path,'w+') as f:
		f.write("0\n20\n0\n"+playername+"\n3000\nhill\n[]")
#Print if debug is enabled
def debug(message):
	if env_debug:
		print("[Debug] "+message)

#LOAD shell loop
while True:
	print("Welcome to DUNGEONS!")
	print()
	print("Enter path to a save or type \"New\" or \"Quit\"")
	choice=input("><>")
	if choice.lower()=="new":
		print("00:00 Day 000")
		print("The Hill")
		print("----------, $----, 00 Items")
		print()
		choice=input("Create new save? [Y/n] ")
		choice=choice.lower()
		if choice=="" or choice=="y" or choice=="yes":
			newsave=True #Note that a new save is being made
			break #Quit the LOAD shell
	elif choice.lower()=="exit" or choice.lower()=="quit":
		print("OK, Bye!")
	else:
		print("Sorry, we don't support loading and saveing yet...")

if newsave:
	#Player name shell
	while True:
		print("Enter a name:")
		playername=input("  >>")
		if playername=="":
			print("Name cannot be empty")
		elif len(playername)>10:
			print("Name must be 10 or less letters.")
		elif len(playername)<2:
			print("Name must be at least three letters.")
		else:
			print("Cool name!")
			break #Quit to next opperation
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
	thisGame=dungeon.Game() #Load all game data
	print("Saveing game...")
	writeEmpty(path) #write empty file
	print("Loading game...")
	thisGame.setSave(path) #opens the empty file
	print("Lets go!\n")
	main.start(thisGame) #Starts the game. See /root/git/main.py
