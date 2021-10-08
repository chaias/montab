from db import db

class MontabModel(db.Model):
    __tablename__ = 'montab'
#MONCOD  NOT NULL NUMBER(2)
#MONNOM           VARCHAR2(30)
#MONABR           VARCHAR2(5)
#MONABR1          VARCHAR2(2)
#MONDOL  NOT NULL VARCHAR2(1)

    moncod = db.Column(db.Integer, primary_key=True)
    monnom = db.Column(db.String(30))
    monabr = db.Column(db.String(5))
    monabr1 = db.Column(db.String(2))
    mondol = db.Column(db.String(1))

    def __init__(self,moncod,monnom,monabr,monabr1,mondol):
        self:moncod = moncod
        self:monnom = monnom
        self:monabr = monabr
        self:monabr1 = monabr1
        self:mondol = mondol

    def json(self):
        return {'moncod' : self.moncod,
                'monnom' : self.monnom,
                'monabr' : self.monabr,
                'monabr1' : self.monabr1,
                'mondol' : self.mondol}
    @classmethod
    def find_by_moncod(cls, moncod):
        return cls.query.filter_by(moncod=moncod).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
