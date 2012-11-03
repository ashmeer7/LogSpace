import pymongo

class Database(object):

    def __init__(self):
        # Initialize the connection to the database.
        # TODO(danny): Replace host/port with production values.
        connection = pymongo.Connection('localhost', 27017)
        self.db = connection.logs

    def drop(self, collection):
        """
        Drop the given collection from the database.

        Args
          collection: string - The name of the collection.
        """
        self.db[collection].drop()

    def find(self, collection, selector=None, limit=0):
        """
        Find all documents in the given collection matching the selector.

        Args
          collection: string - The name of the collection.
          selector: dictionary - A dictionary of key-value pairs describing
              which documents to select from the collection.
          limit: int - The maximum number of documents to return.

        Return
          list - A list of documents matching the selector.
        """
        cursor = self.db[collection].find(spec=selector, limit=limit)
        return [item for item in cursor]

    def insert(self, collection, document):
        """
        Insert a document into the given collection.

        Args
          collection: string - The name of the collection.
          document: dictionary - A dictionary of key-value pairs to add into the
              collection.

        Return
          boolean - True if the document is successfully inserted.
        """
        try:
            self.db[collection].insert(document, safe=True)
            return True
        except pymongo.errors.OperationFailure:
            return False

db = Database()
