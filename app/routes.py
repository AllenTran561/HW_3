from app import myobj
from flask import render_template, flash, Flask, redirect, url_for, request


name  =  'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myobj.route("/", methods = ['GET', 'POST'])
def home():
   if (request.method == 'POST'):
      flash(request.form["city"])
      return redirect(url_for('home'))
   return render_template("home.html", name = name, city_names= city_names)
    
if __name__ == "__main__":
   my_obj.run(debug = True)
