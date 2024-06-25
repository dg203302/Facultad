from appweb import db
class Paquete(db.Model):
    __tablename__='paquete'
    __id=db.Column(db.Integer, primary_key=True)
    __numeroenvio=db.Column(db.Integer, primary_key=False, nullable=False)
    __peso=db.Column(db.Float, nullable=False)
    __nomdestinatario=db.Column(db.String(120), nullable=False)
    __dirdestinatario=db.Column(db.String(120), nullable=False)
    __entregado=db.Column(db.Boolean, default=False)
    __observaciones=db.Column(db.String(120))
    __idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.__id'))
    __idtransporte=db.Column(db.Integer, db.ForeignKey('transporte.__id'))
    __idrepartidor=db.Column(db.Integer, db.ForeignKey('repartidor.__id'))
    def getidrepartidor(self):
        return self.__idrepartidor
    def getid(self):
        return self.__id
    def getidtransporte(self):
        return self.__idtransporte
    def getestado(self):
        return self.__entregado
    def __repr__(self):
        return f'{self.__numeroenvio}'
class Transporte(db.Model):
    __tablename__='transporte'
    __id=db.Column(db.Integer, primary_key=True)
    __numerotransporte=db.Column(db.Integer, primary_key=False, nullable=False)
    __fechahorasalida=db.Column(db.DateTime, nullable=False)
    __fechahorallegada=db.Column(db.DateTime, nullable=False)
    __idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.__id'))
    __paquetes=db.relationship('Paquete', backref='transporte', cascade='all, delete-orphan', lazy=True)
    def getidsucursal(self):
        return self.__idsucursal
    def getid(self):
        return self.__id
    def getfechahorallegada(self):
        return self.__fechahorallegada
    def actfechallegada(self,fechallegada):
        self.__fechahorallegada=fechallegada
    def getpaquetes(self):
        return self.__paquetes
class Repartidor(db.Model):
    __tablename__='repartidor'
    __id=db.Column(db.Integer, primary_key=True)
    __nombre=db.Column(db.String(120), nullable=False)
    __dni=db.Column(db.String(120), nullable=False, unique=True)
    __idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.__id'))
    __paquetes=db.relationship('Paquete', backref='repartidor', cascade='all, delete-orphan')
class Sucursal(db.Model):
    __tablename__='sucursal'
    __id=db.Column(db.Integer, primary_key=True)
    __numero=db.Column(db.String(120), nullable=False, unique=True)
    __provincia=db.Column(db.String(120), nullable=False)
    __localidad=db.Column(db.String(120), nullable=False)
    __direccion=db.Column(db.String(120), nullable=False, unique=True)
    __paquetes=db.relationship('Paquete', backref='sucursal', cascade='all, delete-orphan')
    __transportes=db.relationship('Transporte', backref='sucursal', cascade='all, delete-orphan')
    __repartidores=db.relationship('Repartidor', backref='sucursal', cascade='all, delete-orphan')
    def getid(self):
        return self.__id
    def getprovincia(self):
        return self.__provincia
    def getlocalidad(self):
        return self.__localidad