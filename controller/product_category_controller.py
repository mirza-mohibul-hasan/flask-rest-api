from app import app

@app.route("/product/category")
def categoryProduct():
    return "Category Product"