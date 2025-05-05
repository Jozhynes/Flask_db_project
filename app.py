from flask import Flask, render_template, url_for, request
from sqlalchemy.orm import sessionmaker
from models import Products
from connection import session
app=Flask(__name__)
@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/product', methods=['GET','POST'])
def product():
    if request.method=='POST':
       productname=request.form ['name']
       description = request.form['description']
       myproducts=Products(productname,description)
       session.add(myproducts)
       session.commit()
       
       
    return render_template('products.html')
if __name__=="__main__":
 app.run(debug=True)