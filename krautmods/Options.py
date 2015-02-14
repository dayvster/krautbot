import os, configparser
class KrautOpts(object):
	section 		= ""
	argsDict 		= {}
	confObject 		= configparser.ConfigParser()

	def __init__(self):
		print("settings called")
	def getConfigLocation(self):
		currentLocation = os.path.split(os.getcwd())
		fileLoc = currentLocation[0]+os.path.sep+"conf/"
		return str(fileLoc)
	def overWriteConf(self,  section="default",**kwargs):
		self.section 		= section
		self.argsDict 		= kwargs
		self.confObject[section] = self.argsDict
		fl = self.getConfigLocation()
		with open(fl+str("kraut.cnf"), 'w') as configfile:
			self.confObject.write(configfile)
	def readConfFile(self):
		fl = self.getConfigLocation()
		with open(fl+str("kraut.cnf"), 'r') as configfile:
	