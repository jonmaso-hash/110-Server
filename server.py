from flask import Flask, jsonify, request

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

    #----------PRODUCTS---------

products = [
    {
        "_id": 1,
        "title": "Nintendo Switch",
        "price": 499.99,
        "category": "Electronics",
        "image": "https://picsum.photos/seed/1/300/300"
    },
    {
        "_id": 2,
        "title": "Smart Refrigerator",
        "price": 999.99,
        "category": "kitchen",
        "image": "https://picsum.photos/seed/2/300/300"
    },
    {
        "_id": 3,
        "title": "Bluetooth Speaker",
        "price": 79.99,
        "category": "Electornics",
        "image": "https://picsum.photos/seed/3/300/300"
    }
]

#Get /api/products, endpoint that return a list of products
@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify({
        "success": True,
        "message": "Products retrieved successfully",
        "products": products
    }), 200 #ok

#GET /api/products/3
@app.route("/api/products/<int:product_id>")
def get_products_by_id(product_id):
    for product in products:
        if product["_id"] == product_id:
            return jsonify({
                "success": True,
                "message": "Product retrieved successfully",
                "data": product
            }), 200 #0k
       
    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404 #Not Found

#POST /api/products
@app.route("/api/products",methods=["POST"])
def create_product():
    new_product = request.get_json()
    print(new_product)
    products.append(new_product)
    return jsonify({
        "success": True,
        "message": "Product successfully created",
        "data": new_product
    }), 201 #CREATED

#DELETE /api/products/<int.product_id>
@app.route("/api/products/<int:product_id>",methods=["DELETE"])
def delete_product(product_id):
    for index, product in enumerate(products):
        if product["_id"] == product_id:
            products.pop(index)
            print("We found the product")
            return jsonify({
                "success": True,
                "message": "Product deleted successfully"
            }), 202 #ok

    return jsonify({
        "success": False,
        "message": "Product Not Found"
    }), 404 #not found

    #Put /api/products/<int:product_id>
@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()

    for product in products:
        if product["_id"] == product_id:
            product["title"] = data["title"]
            product["price"] = data["price"]
            product["category"] = data["category"]
            product["image"] = data["image"]

            return jsonify({
                "success": True,
                "message": "Product updated successfully",
                "data": product
            }), 200

    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404

    
    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404 #not found





#Path Parameter
#Is a dymaic part of the URL used to identify a specific item or resource within an API.
#http://127.0.0.1:5000/greet/john
@app.route("/greet/<string:name>", methods=["GET"])
def greet(name):
    print(f"this is the name {name}")
    return jsonify({"message": f"Hello {name}"
    }), 200 #OK

# ----- Coupons --------
#http://127.0.0.1:5000/coupons
coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]

@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    data = request.get_json()

    if not data or "_id" not in data or "code" not in data or "discount" not in data:
        return jsonify({
            "success": False,
            "message": "Coupon must include _id, code, and discount"
        }), 400

    for coupon in coupons:
        if coupon["_id"] == data["_id"]:
            return jsonify({
                "success": False,
                "message": "Coupon with this ID already exists"
            }), 409

    coupons.append(data)

    return jsonify({
        "success": True,
        "data": data
    }), 201

@app.route("/api/coupons/<int:id>", methods=["GET"])
def get_coupon_by_id(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            return jsonify({
                "success": True,
                "data": coupon
            }), 200

    return jsonify({
        "success": False,
        "message": "Coupon not found"
    }), 404



if __name__ =="__main__":
    app.run (debug=True)
    #when this file is run directly: _name_ =="__main__"
    #when this file is imported as a module: _name_ == "server.py"

#POST /api/coupons
#GET /api/coupons<int:id>