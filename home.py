from flask import Flask
from flask import escape
 
myapp_obj = Flask(__name__)
 
@myapp_obj.route("/")
def home():
   name = "Lisa"
   city_name = ["Paris", "London", "Rome", "Tahiti"]
   return '''
   <html>
   <body>
      <h1>Hello, ''' + name + '''!</h1>
      <a href="https://www.google.com/"> not google</a>
      <ul>
         <li>''' + city_name[0] +  '''</li>
         <li>''' + city_name[1] + '''</li>  
         <li>''' + city_name[2] + '''</li> 
         <li>''' + city_name[3] + '''</li>  
      </ul>
   </html>
   '''
myapp_obj.run()
