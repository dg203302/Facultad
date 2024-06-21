from flask_sqlalchemy import SQLAlchemy
from appweb import db
class Sucursal(db.Model):
    __tablename__='sucursal'
    id=db.Column(db.Integer, primary_key=True)
    numero=db.Column(db.String(120), nullable=False, unique=True)
    provincia=db.Column(db.String(120), nullable=False)
    localidad=db.Column(db.String(120), nullable=False)
    direccion=db.Column(db.String(120), nullable=False, unique=True)
    paquetes=db.relationship('paquete', backref='sucursal', cascade='all, delete-orphan')
    transportes=db.relationship('transporte', backref='sucursal', cascade='all, delete-orphan')
    repartidores=db.relationship('repartidor', backref='sucursal', cascade='all, delete-orphan')
class Repartidor(db.Model):
    __tablename__='repartidor'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(120), nullable=False)
    dni=db.Column(db.String(120), nullable=False, unique=True)
    idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    paquetes=db.relationship('paquete', backref='repartidor', cascade='all, delete-orphan')
class Paquete(db.Model):
    __tablename__='paquete'
    id=db.Column(db.Integer, primary_key=True)
    peso=db.Column(db.Float, nullable=False)
    nomdestino=db.Column(db.String(120), nullable=False)
    dirdestino=db.Column(db.String(120), nullable=False)
    entregado=db.Column(db.Boolean, default=False)
    observaciones=db.Column(db.String(120))
    idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    idtransporte=db.Column(db.Integer, db.ForeignKey('transporte.id'))
    idrepartidor=db.Column(db.Integer, db.ForeignKey('repartidor.id'))
class Transporte(db.Model):
    __tablename__='transporte'
    id=db.Column(db.Integer, primary_key=True)
    fechahorasalida=db.Column(db.DateTime, nullable=False)
    fechahorallegada=db.Column(db.DateTime, nullable=False)
    idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    paquetes=db.relationship('paquete', backref='transporte', cascade='all, delete-orphan')