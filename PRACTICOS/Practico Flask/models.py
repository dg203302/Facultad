from appweb import db
class Paquete(db.Model):
    __tablename__='paquete'
    id=db.Column(db.Integer, primary_key=True)
    numeroenvio=db.Column(db.Integer, primary_key=False, nullable=False)
    peso=db.Column(db.Float, nullable=False)
    nomdestinatario=db.Column(db.String(120), nullable=False)
    dirdestinatario=db.Column(db.String(120), nullable=False)
    entregado=db.Column(db.Boolean, default=False)
    observaciones=db.Column(db.String(120))
    idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    idtransporte=db.Column(db.Integer, db.ForeignKey('transporte.id'))
    idrepartidor=db.Column(db.Integer, db.ForeignKey('repartidor.id'))
class Transporte(db.Model):
    __tablename__='transporte'
    id=db.Column(db.Integer, primary_key=True)
    numerotransporte=db.Column(db.Integer, primary_key=False, nullable=False)
    fechahorasalida=db.Column(db.DateTime, nullable=False)
    fechahorallegada=db.Column(db.DateTime, nullable=False)
    idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    paquetes=db.relationship('Paquete', backref='transporte', cascade='all, delete-orphan', lazy=True)
class Repartidor(db.Model):
    __tablename__='repartidor'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(120), nullable=False)
    dni=db.Column(db.String(120), nullable=False, unique=True)
    idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    paquetes=db.relationship('Paquete', backref='repartidor', cascade='all, delete-orphan')
class Sucursal(db.Model):
    __tablename__='sucursal'
    id=db.Column(db.Integer, primary_key=True)
    numero=db.Column(db.String(120), nullable=False, unique=True)
    provincia=db.Column(db.String(120), nullable=False)
    localidad=db.Column(db.String(120), nullable=False)
    direccion=db.Column(db.String(120), nullable=False, unique=True)
    paquetes=db.relationship('Paquete', backref='sucursal', cascade='all, delete-orphan')
    transportes=db.relationship('Transporte', backref='sucursal', cascade='all, delete-orphan')
    repartidores=db.relationship('Repartidor', backref='sucursal', cascade='all, delete-orphan')