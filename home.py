from flask import Flask
from flask import escape
 
myobj = Flask(__name__)
name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]
 
@myobj.route("/")
def home():
   return '''
   <html>
      <head>
         <title>WelcomeLisa!</title>
      <head>
   <body>
      <h1>Welcome ''' + name + '''!</h1>
      <a href="www.google.com">notgoogle</a>
      <ul>
         <li>''' + city_names[0] + '''</li>
         <li>''' + city_names[1] + '''</li>
         <li>''' + city_names[2] + '''</li>
         <li>''' + city_names[3] + '''</li>

      </ul>
   </html>
   '''
myobj.run()
