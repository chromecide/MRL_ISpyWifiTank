from java.lang import String
from org.myrobotlab.service import Sphinx
from org.myrobotlab.service import Runtime
from ispyMotors import Motors

m = Motors()

#connect to the Tank Control port
m.init_connection()

#once we're connected
if m.is_connected:
	ear = Runtime.createAndStart("ear","Sphinx")

	# start listening for the words we are interested in
	ear.startListening("go forward|go backward|turn left|turn right|head up|head down|stop")
	
	# set up a message route from the ear --to--> python method "heard"
	ear.addListener("recognized", python.name, "heard", String().getClass()); 
	  
	# this method is invoked when something is 
	# recognized by the ear
	def heard(phrase):
	
	      print "heard ", phrase
	      
	      if phrase == "go forward":
	          m.moveForward()
	      elif phrase == "go backward":
	      	m.moveBackward()
	      elif phrase == "turn left":
	      	m.moveLeft()
	      	print "L"
	      elif phrase == "turn right":
	      	m.moveRight()
	      elif phrase == "head up":
	      	m.moveHeadUp()
	      elif phrase == "head down":
	      	m.moveHeadDown()
	      elif phrase =="stop":
	      	m.stopAll()