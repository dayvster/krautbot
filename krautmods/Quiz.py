import random
class Quiz(object):	
	userAnswer 		= None
	currentQuestion = None
	questionsAsked 	= []

	def __init__(self):
		super(Quiz, self).__init__()
	
	def setUserAnswer(self, uAnswer):
		self.userAnswer = uAnswer

	def checkAnswer(self, questionNum):
		if(str(userAnswer) == str(self.questionDict()[questionNum].get("answer"))):
			return True
		else:
			return False
	def askQustion(self):
		self.currentQuestion = self.questionDict()
	def questionDict(self, qNum):
		lst = 	[ 	
					{"question":"what is 1+1", "answer":"2"},
					{"question":"what is 1+1", "answer":"2"},
					{"question":"what is 1+1", "answer":"2"},
					{"question":"what is 1+1", "answer":"2"},
					{"question":"what is 1+1", "answer":"2"},
					{"question":"what is 1+1", "answer":"2"},
					{"question":"what is 1+1", "answer":"2"},
					{"question":"what is 1+1", "answer":"2"},
					{"question":"what is 1+1", "answer":"2"},
					{"question":"what is 1+1", "answer":"2"},
				]
		return lst[qNum]

	def Test(self):
		print(self.questionDict(0).get("answer"))
q = Quiz()
q.Test()