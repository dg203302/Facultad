import random
from flask import Flask,request,render_template,session
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config.from_pyfile('config.py')
db=SQLAlchemy(app)
@app.route('/')
def inicio():
    return render_template('paginainicial.html')
@app.route('/accesodesp',methods=['GET','POST'])
def accesodesp():
    if request.method=='POST':
        session['sucursal_seleccionada']=request.form.get('sucursales')
        return render_template('funcionesdespachante.html', sucursal=db.session.query(Sucursal).filter(Sucursal.id==session['sucursal_seleccionada']).first()) #ineficiente
    else:
        return render_template('accesodesp.html', sucursales=db.session.query(Sucursal).all(), sucursal_seleccionada=None)
@app.route('/registrarrecepcion', methods=['GET','POST'])
def registrarrecepcion():
    if request.method=='POST':
        numerodeenvio=random.randint(0,1000)
        peso=request.form.get('peso')
        nombre=request.form.get('nombre')
        direccion=request.form.get('direccion')
        sucu=db.session.query(Sucursal).filter(Sucursal.id==session['sucursal_seleccionada']).first() #ineficiente
        nuevopaquete=Paquete(numeroenvio=numerodeenvio,peso=peso,nomdestinatario=nombre,dirdestinatario=direccion,observaciones='',idsucursal=sucu.id)
        db.session.add(nuevopaquete)
        db.session.commit()
        return render_template('registrocorrecto.html', paquete=nuevopaquete)
    else:
        return render_template('registrarrecepcionpaquete.html', sucu=db.session.query(Sucursal).filter(Sucursal.id==session['sucursal_seleccionada']).first())
@app.route('/registrarsalida', methods=['POST','GET'])
def registrarsalida():
    
    return
#@app.route('/regsitrarllegada')
if __name__=='__main__':
    with app.app_context():
        from models import Paquete,Transporte,Repartidor,Sucursal
        db.create_all()
        app.run(debug=True)