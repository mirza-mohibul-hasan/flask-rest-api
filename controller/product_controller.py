from app import app

@app.route("/product/add")
def addProduct():
    return "Add Product"