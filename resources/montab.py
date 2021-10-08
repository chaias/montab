from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.montab import MontabModel

class Montab(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('monnom',
        required=True,
        help='El campo no puede ir vacio!!!')

    parser.add_argument('monabr',
        required=True,
        help='El campo no mondol debe ir lleno siempre!!!')

    parser.add_argument('monabr1',
        required=True,
        help='El campo no mondol debe ir lleno siempre!!!')

    parser.add_argument('mondol',
        required=True,
        help='El campo no mondol debe ir lleno siempre!!!')

    #@jwt_required
    def get(self,moncod):
        montab = MontabModel.find_by_moncod(moncod)
        if montab:
            return montab.json()
        return {'mensaje': 'Registro no encontrado!'}, 404

    def post(self,moncod):
        if MontabModel.find_by_moncod(moncod):
            return {'Mensaje': "Un item con el nombre '{}' ya existe!.".format(moncod)}, 400

        data = Montab.parser.parse_args()
        montab = MontabModel(moncod,**data)

        try:
            montab.save_to_db()
        except:
            return {"mensaje": "Ah ocurrido un error insertando el registro"}, 500

        return montab.json(),201

    def delete(self,montab):
        montab = MontabModel.find_by_moncod(moncod)
        if montab:
            montab.delete_from_db()
        return {'mensaje':'Registro Eliminado'}

    def put(self,moncod):
        data = Montab.parser.parse_args()

        montab = MontabModel.find_by_moncod(moncod)

        if montab is None:
            montab = MontabModel(moncod,**data)
        else:
            montab.monnom = data['monnom']
            montab.monabr = data['monabr']
            montab.monabr1 = data['monabr1']
            montab.mondol = data['mondol']

        montab.save_to_db()

        return montab.json()

class MontabList(Resource):
    def get(self):
        return {'montab': [x.json() for x in MontabModel.query.all()]}
