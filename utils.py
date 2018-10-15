import logging

logging.basicConfig(filename='utils.log',level=logging.DEBUG)

class Utils(object):

	def __init__(self):
		logging.info("Initialized")

	def example(self):
		logging.debug("Example log")
		return True

if __name__ == '__main__':
	utils = Utils()
	utils.example()
	print("Hello")