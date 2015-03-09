import random, datetime, time, urllib3
class KrautCMDs(object):
	command		= ""
	user 		= ""
	group 		= ""
	cmdLst		= ""

	def __init__(self, user="nobody"):
		super(KrautCMDs, self).__init__()
		self.user = user
	def rollTheDie(self):
		rand = random.randrange(0,101)
		return rand

	def sammich(self):
		msgLst = 	[
						"Poof, you are a sandwhich!",
						"What? make it yourself!",
						"Naw",
						"Extra spit?",
					]
		rand = random.randrange(0,len(msgLst))
		return msgLst[rand]

	def lifeAnswer(self):
		ans = str(42)
		return ans

	def quit(self):
		if(self.user == "nixfox"):
			return True
		return False

	def time(self):
		fmt = "%d %B %Y at %H:%M:%S"
		time_now = datetime.datetime.now().strftime(fmt)
		return time_now

	def insult(self):
		insultLst = 	[
							"smells",
							"is a stupid person",
							"is an utter idiot",
							"is literally worse than Hitler",
							"has two mums",
							"has two dads",
						]

	def isUp(self, website):
		try:
			url = urllib3.PoolManager()
			url = url.request("GET", str(website)).status
			if(url == 200):
				return True
			return False
		except Exception as e:
			print(e)
			return False
		return False