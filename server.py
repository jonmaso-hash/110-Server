from flask import Flask

app = Flask(__name__) #instance of Flask

#htpp://127.0.0.1:5000/
@app.route("/", methods=["GET"])
def index():
    return"Welcome to Flask Framework"

#htpp://127.0.0.1:5000/hello
@app.route("/hello",methods = ["GET"])
def hello():
    return  "Hello World from Flask"

#http://127.0.0.1:5000/cohort-63
@app.route("/cohort-63", methods =["GET"])
def cohort63():
    student_list = ["Robert","Barney", "Luis", "Lemuel", "John", "Angel"]
    return student_list

#http://127.0.0.1:5000/cohort-99
@app.route("/cohort-99", methods=["GET"])
def cohort99():
    student_list = ["Pam","Dwight","Michael","Angela"]
    return student_list

#http://127.0.0.1:5000/contact
@app.route("/contact", methods=["GET"])
def contact():
        information ={
            "email": "water@bottle.edu",
            "phone": "619 400797"
        }
        return information

#http://127.0.0.1:5000/course_information
@app.route("/course-information", methods=["GET"])
def course_information():
    course_data ={
        "title": "Introduction Web API with Flask",
        "duration": "4 Sessions",
        "level": "Beginner"
    }
    return course_data

# ----- Coupons --------
#http://127.0.0.1:5000/coupons
@app.route("/coupons", methods=["GET"])
def count():
    coupons_list = [
        {"_id": 1, "code": "WELCOME10", "discount": 10},
        {"_id": 2, "code": "SPOOKY25", "discount": 25},
        {"_id": 3, "code": "VIP50", "discount": 50}
    ]
    return coupons_list


if __name__ =="__main__":
    app.run (debug=True)
    #when this file is run directly: _name_ =="__main__"
    #when this file is imported as a module: _name_ == "server.py"