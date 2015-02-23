#!/usr/bin/python



import webapp
import random


class aleat(webapp.webApp):



	def process(self, parsedRequest):
		link = str(random.randrange(123456789))
		print link
		return ("200 OK", "<html><body><h1>Hello World!</h1>" +"<a href='"+ link + "'>dame otra</a>"+ 
                        "</body></html>")




	
if __name__ == "__main__":
	testAleat= aleat("localhost", 1234)


