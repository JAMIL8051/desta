from flask import Flask, render_template, request
#import store_to_db
import urllib.request 


my_request = urllib.request.urlopen("https://desta.vercel.app/about")
my_HTML = my_request.read().decode('utf-8')







# app = Flask(__name__) # Creating a flask application

# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template("form.html")
# @app.route("/result",methods = ['POST', 'GET'])
# def result():
#     output = request.form.to_dict()
#     name = output['fname']
#     email = output['email']
#     user_interest = output['interest']
#     store_to_db.send_results_to_user(email, user_interest)
    


#     return render_template("form.html", name = name)
    



# if __name__== "__main__":
#     app.run(debug=True, port =5000)