class Quiz(object):
	question 		= ""
	answer 			= ""
	user 			= ""
	points 			= ""
	winner			= ""
	category 		= ""
	numOfQuestions 	= 0
	scoreBoard 		= []
	alreadyAsked 	= []
	questionsDict	= {}

	def __init__(self, numOfQuestions=10, category="science"):
		self.numOfQuestions = numOfQuestions
		self.category 		= category
	
	def science(self):
		self.questionsDict = {
								"question":"what is the largest animal?", "answer":"blue whale"
							}
		return self.questionsDict
	
