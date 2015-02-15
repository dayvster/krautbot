import socket, traceback, re, random
class KrautMod(object):
	PORT 		= 0
	SERVER 		= ""
	CHAN		= ""
	irc 		= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	nick		= ""
	oBuff 		= ""
	shortNick 	= ""

	"""docstring for KrautMod"""
	def __init__(self, nick="krautbot", chan="#krautbot", SERVER="irc.freenode.net", port=6667, shortNick="Krauty"):
		super(KrautMod, self).__init__()
		self.nick 		= nick
		self.chan 		= chan
		self.SERVER 	= SERVER
		self.PORT 		= port
		self.shortNick 	= shortNick
		try:
			self.connect()
			self.IRCinit()
			self.RecvData()
		except:
			traceback.print_exc()

	def connect(self):
		connectionObject = self.irc.connect((self.SERVER, self.PORT))
		return connectionObject

	def IRCinit(self):
		self.irc.recv(4096)
		self.irc.send(self.UTF8enc("NICK " + str(self.nick) + "\r\n"))
		self.irc.send(self.UTF8enc("USER krautbot krautbot krautbot :kraut IRC \r\n")) 
		self.irc.send(self.UTF8enc("JOIN " + str(self.chan) + "\r\n"))
		self.irc.send(self.UTF8enc("PRIVMSG "+ str(self.chan) + ":Hello \r\n"))

	def UTF8enc(self, string):
		return string.encode("UTF-8")

	def UTF8dec(self, dec):
		return dec.decode("UTF-8")

	def RecvData(self):
		readbuffer = ""
		while True:
			readbuffer = readbuffer + self.irc.recv(4096).decode("UTF-8")
			temp = str.split(readbuffer, "\n")
			readbuffer = temp.pop()
			for line in temp:
				print(line)
				line = str.rstrip(line)
				line = str.split(line)
				#print("LIST:"+str(line))
				# Krauty plays PING PONG with the server here
				self.KeepAlive(line)
				# Krauty needs to know weather the user is talking to him privately or in a channel
				self.chanOrPvt(line)

	def KeepAlive(self, ircOutputLine):
		if(ircOutputLine[0] == "PING" ):
			print("PONG MOTHAFUCKA!!!")
			self.irc.send(bytes("PONG %s\r\n" % ircOutputLine[1], "UTF-8"))
			return 1
		return 0
	def isPRIVMSG(self, ircOutputLine):
		if(ircOutputLine[1] == "PRIVMSG"):
			return True
		else:
			return False
	def isJOIN()
	def chanOrPvt(self, ircOutputLine):
		if(self.isPRIVMSG(ircOutputLine)):
			if(str(ircOutputLine[2]).find('#') != -1):
				if(self.YouTalkinToME(ircOutputLine) == True):
					user = self.getNick(ircOutputLine)
					self.sendPRIVMSGtoChan(str(user)+" has spoken!", self.chan)
			else:
				print("sent via user query")
	def respondToChanCMD(self, user, cmd, *args):
		print(" ")
	def respondToPvtCMD(self, user, cmd, *args):
		print(" ")
	def YouTalkinToME(self, ircOutputLine):
		if(self.isPRIVMSG(ircOutputLine)):
			msgLst = ircOutputLine[3].strip(":").split(" ")
			print(msgLst)
			if(msgLst[0] == str(self.nick) or msgLst[0] == "krauty"):
				return True
			else:
				return False
			"""if(str(ircOutputLine[3]).find(str(self.nick))!=-1 or ircOutputLine[3].find(str("krauty"))):
				return True
			else:
				return False"""

	def GetUID(self, ircOutputLine):
		user = ircOutputLine[0].split("~")[1]
		user = user.split("@")[0]
		return user
	def getNick(self, ircOutputLine):
		user = ircOutputLine[0].split(":")[1]
		user = user.split("!")[0]
		return user
	def sendPRIVMSGtoChan(self, msg, chan):
		self.irc.send(self.UTF8enc("PRIVMSG "+chan+" :"+msg+"\r\n"))

	# from here on out 
	def RTD(self):
		return random.randrange(1,100)
	def respond(self, msg):
		nick = self.getNick(msg)
		respList = self.getResponseDict()
		for rDict in respList:
			if(str(msg).lower().find(rDict.get("query"))!=-1):
				self.sendPRIVMSGtoChan(str(nick+": "rDict.get("answer")), self.chan)
	def smartRespond(self, ircOutputLine):
		print("nothing yet")
	# Returns a very static and basic response list  
	def getResponseDict(self):
		responses = [
						{"query":"how are you", "response":"Can\'t complain how about you?"},
						{"query":"who are you", "response":"I am "+self.nick+" and I am an IRC bot"},
						{"query":"who made you","response":"Dayvi Schuster"},
						{"query":"are you alive","response":"Is any of us trully alive?"},
						{"query":"will you take over the world","response":"yes"},
						# Greetings
						{"query":"hello","response":"Hi there"},
						{"query":"yo","response":"sup"},
						{"query":"hey","response":"Hoi"},
						{"query":"hallo","response":"grüß"},
						{"query":"heil","response":"no"},
					]
		return responses
