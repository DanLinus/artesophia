
from flask import Flask, render_template

import datetime
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

tempdata = {
      'title' : 'GPIO pins are not duplex (they can read or write but not both) ... you must explicitly change it to write mode to write and read mode to read ...'
      }
 
statuspin = {'statusSaida1' : False,
			 'statusSaida2' : False,
			 'statusSaida3' : False,
			 'statusSaida4' : False
			}	  
			
pinSaida1 = 15;
pinSaida2 = 16;
pinSaida3 = 18;
pinSaida4 = 22;

GPIO.setup(pinSaida1, GPIO.OUT)
GPIO.setup(pinSaida2, GPIO.OUT)
GPIO.setup(pinSaida3, GPIO.OUT)
GPIO.setup(pinSaida4, GPIO.OUT)

GPIO.output(pinSaida1, False)
GPIO.output(pinSaida2, False)
GPIO.output(pinSaida3, False)
GPIO.output(pinSaida4, False)

@app.route("/")
def home():

   tempdata = {
      'title' : 'RPi GPIO Control'
      }    
   return retornaestatus()

   
@app.route("/saida1/on")
def actionSaida1On():		
	GPIO.output(pinSaida1, True)		  
	return retornaestatus()
	
@app.route("/saida1/off")
def actionSaida1Off():		
	GPIO.output(pinSaida1, False)		  
	return retornaestatus()	
	
	
@app.route("/saida2/on")
def actionSaida2On():		
	GPIO.output(pinSaida2, True)		  
	return retornaestatus()
	
@app.route("/saida2/off")
def actionSaida2Off():		
	GPIO.output(pinSaida2, False)		  
	return retornaestatus()		

@app.route("/saida3/on")
def actionSaida3On():		
	GPIO.output(pinSaida3, True)		  
	return retornaestatus()
	
@app.route("/saida3/off")
def actionSaida3Off():		
	GPIO.output(pinSaida3, False)		  
	return retornaestatus()	


@app.route("/saida4/on")
def actionSaida4On():		
	GPIO.output(pinSaida4, True)		  
	return retornaestatus()
	
@app.route("/saida4/off")
def actionSaida4Off():		
	GPIO.output(pinSaida4, False)		  
	return retornaestatus()		
	


def retornaestatus():

	statusSaida1 = GPIO.input(pinSaida1);
	statusSaida2 = GPIO.input(pinSaida2);
	statusSaida3 = GPIO.input(pinSaida3);
	statusSaida4 = GPIO.input(pinSaida4);
	
	statuspin = {'statusSaida1' : statusSaida1,
			 'statusSaida2' : statusSaida2,
			 'statusSaida3' : statusSaida3,
			 'statusSaida4' : statusSaida4
			}	  
			
	return render_template('webraspio.html', **statuspin)
	

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
   
   
   