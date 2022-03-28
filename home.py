from flask import Flask
from flask import escape
 
myobj = Flask(__name__)
name = "Lisa"
city_name = ["Paris", "London", "Rome", "Tahiti"]
 
@myobj.route("/")
def home():
   return '''
   <html>
      <h1>
         <title> Home </title>
      <h1>
   <body>
      <h1>Welcome, ''' + name + '''!</h1>
      <a href="www.google.com/"> not google</a>
      <ul>
         <li>''' + city_name[0] +  '''</li>
         <li>''' + city_name[1] + '''</li>  
         <li>''' + city_name[2] + '''</li> 
         <li>''' + city_name[3] + '''</li>  
      </ul>
   </html>
   '''
myobj.run()
