from flask_restful import Resource
# from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):
    # @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        
        if store:
            return store.json(), 200
        
        return {'message': 'Store {} not found'.format(name)}, 404

    # @jwt_required()
    def post(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            return {'message': "An itstoreem {} already exist".format(name)}, 400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {"message": "An error occured inserting the item"}, 500

        return store.json(), 201

    # @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()

        return {'message': 'Item deleted.'}, 200

class StoreList(Resource):
    def get(self):
        return {'stores': [item.json() for item in StoreModel.query.all()]}
