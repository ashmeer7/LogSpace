import pymongo

# TODO(danny): Replace host/port with production values.
CONNECTION = pymongo.Connection('localhost', 27017)
DB = CONNECTION.logs

class Database:
    def insert(self, collection, document):
        try:
            DB[collection].insert(document, safe=True)
            return True
        except pymongo.errors.OperationFailure:
            return False

    def find(self, collection, selector):
        return [item for item in DB[collection].find(selector)]

db = Database()
