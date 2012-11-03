import sys
sys.path.insert(0, '../../src/server')

from database import db
from database import DB

COLLECTION = "test"

def insert_test():
    test_document = {"_id": "test_data", "name": "first test"}
    test_fail_document = {"_id": "test_data", "name": "second test"}

    # Check a normal insert.
    if not db.insert(COLLECTION, test_document):
        print "Normal insert failed"
        return False

    # Check a conflicting insert.
    if db.insert(COLLECTION, test_fail_document):
        print "Conflicting insert failed"
        return False

    return True

def find_test():
    # Setup test.
    db.insert(COLLECTION, {"name": "test_data"})

    selector = {"name": "test_data"}
    fail_selector = {"name": "fail_data"}

    # Check a normal find.
    if len(db.find(COLLECTION, selector)) != 1:
        print "Normal selection failed"
        return False

    # Check an empty find.
    if len(db.find(COLLECTION, fail_selector)) != 0:
        print "Empty selection failed"
        return False

    return True

def clean():
    DB[COLLECTION].drop()

def run_tests():
    result = True

    result = result and insert_test()
    clean()

    result = result and find_test()
    clean()

    if result:
        print "Test completed"

run_tests()
