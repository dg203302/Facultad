import random, datetime
from flask import Flask,request,render_template,session,redirect,url_for
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
        session['sucursal_seleccionada']=request.form.get('sucursal')
        return redirect(url_for('funcionesdespachante'))
    else:
        return render_template('accesodesp.html', sucursales=db.session.query(Sucursal).all())
@app.route('/funcionesdespachante')
def funcionesdespachante():
    return render_template('funcionesdespachante.html', sucursal=db.session.query(Sucursal).filter(Sucursal.id==session['sucursal_seleccionada']).first())
@app.route('/registrarrecepcion', methods=['GET','POST'])
def registrarrecepcion():
    if request.method=='POST':
        numerodeenvio=random.randint(0,1000)
        if int(request.form.get('peso'))>0:
            peso=request.form.get('peso')
            nombre=request.form.get('nombre')
            direccion=request.form.get('direccion')
            sucu=db.session.query(Sucursal).filter(Sucursal.id==session['sucursal_seleccionada']).first()
            nuevopaquete=Paquete(numeroenvio=numerodeenvio,peso=peso,nomdestinatario=nombre,dirdestinatario=direccion,observaciones='',idsucursal=sucu.id)
            db.session.add(nuevopaquete)
            db.session.commit()
            return render_template('registrocorrecto.html', paquete=nuevopaquete)
        else:
            return render_template('error_ingreso_datos.html')
    else:
        return render_template('registrarrecepcionpaquete.html', sucu=db.session.query(Sucursal).filter(Sucursal.id==session['sucursal_seleccionada']).first())
@app.route('/registrarsalida', methods=['POST','GET'])
def registrarsalida():
    if request.method=='POST':
        session['sucursal_seleccionada_destino']=request.form.get('sucursal_dest')
        return redirect(url_for('seleccionarpaquete'))
    else:
        paquetes=db.session.query(Paquete).all()
        i=0
        while i<len(paquetes):
            if paquetes[i].entregado!=False or paquetes[i].idtransporte!=None:
                i+=1
            else:
                break
        if i==len(paquetes):
            return render_template('sinpaquetesdisponibles.html')
        else:
            return render_template('registrarsalidatranspo.html', sucursalesdest=db.session.query(Sucursal).filter(Sucursal.id!=session['sucursal_seleccionada']).all())
@app.route('/seleccionarpaquete', methods=['GET','POST'])
def seleccionarpaquete():
    if request.method=='POST':
        session['paquetes_seleccionados']=request.form.getlist('paquetes')
        numetr=random.randint(0,100)
        fechasal=datetime.datetime.now()
        sucu=db.session.query(Sucursal).filter(Sucursal.id==session['sucursal_seleccionada_destino']).first()
        nuevotranspo=Transporte(numerotransporte=numetr, fechahorasalida=fechasal, fechahorallegada=None, idsucursal=sucu.id)
        for ids in session['paquetes_seleccionados']:
            paq=db.session.query(Paquete).filter(Paquete.id==ids).first()
            if paq:
                nuevotranspo.paquetes.append(paq)
        db.session.add(nuevotranspo)
        db.session.commit()
        return render_template('transporteregistrado.html', transp=nuevotranspo)
    else:
        return render_template('seleccionarpaquete.html', paquetes=db.session.query(Paquete).filter(Paquete.entregado==False and Paquete.idrepartidor==None))
@app.route('/registrarllegada', methods=['GET','POST'])
def registrarllegada():
    if request.method=='POST':
        session['transporte_llegado']=request.form.get('transporte_llegado')
        transporte_lleg=db.session.query(Transporte).filter(Transporte.id==session['transporte_llegado']).first()
        transporte_lleg.fechahorallegada=datetime.datetime.now()
        paquetes=transporte_lleg.paquetes
        for paquete in paquetes:
            paquete.entregado=True
        db.session.commit()
        return render_template('exitoregistrollegada.html', transp=transporte_lleg)
    else:
        transports=db.session.query(Transporte).filter(Transporte.idsucursal==session['sucursal_seleccionada']).all()
        i=0
        while i<len(transports):
            if transports[i].fechahorallegada!=None:
                i+=1
            else:
                break
        if len(transports)==i:
            return render_template('sintransportesdisponibles.html', sucu=db.session.query(Sucursal).filter(Sucursal.id==session['sucursal_seleccionada']).first())
        else:
            return render_template('registrodellegada.html', transportes=db.session.query(Transporte).filter(Transporte.idsucursal==session['sucursal_seleccionada']).all())
if __name__=='__main__':
    with app.app_context():
        from models import Paquete,Transporte,Repartidor,Sucursal
        db.create_all()
        app.run(debug=True)