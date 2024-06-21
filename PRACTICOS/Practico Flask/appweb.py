from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config.from_pyfile('config.py')
db=SQLAlchemy(app)
if __name__=='__main__':
    with app.app_context():
        from models import Sucursal,Repartidor,Paquete,Transporte
        db.create_all()
    app.run(debug=True)