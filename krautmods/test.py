responses = [
				{"query":"how are you", "response":"Can\'t complain how about you?"},
				{"query":"who are you", "response":"I am "+" and I am an IRC bot"},
				{"query":"who made you","response":"Dayvi Schuster"},
				{"query":"are you alive","response":"Is any of us trully alive?"},
				{"query":"will you take over the world","response":"yes"},
			]
msg = "who are you"
for rDict in responses:
	if(str(msg).lower().find(rDict.get("query")) != -1):
		print(rDict.get("response"))
