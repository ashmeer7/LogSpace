import sys
sys.path.insert(0, '../../src/server')

from database import db

COLLECTION = "test"

def insert_test():
    test_document = {"_id": "test_data", "name": "first test"}
    test_fail_document = {"_id": "test_data", "name": "second test"}

    # Check a normal insert.
    if not db.insert(COLLECTION, test_document):
        print "insert_test: Normal insert failed"
        return False

    # Check a conflicting insert.
    if db.insert(COLLECTION, test_fail_document):
        print "insert_test: Conflicting insert failed"
        return False

    return True

def find_test():
    # Setup test.
    db.insert(COLLECTION, {"name": "test_data"})

    selector = {"name": "test_data"}
    fail_selector = {"name": "fail_data"}

    # Check a normal find.
    if len(db.find(COLLECTION, selector)) != 1:
        print "find_test: Normal selection failed"
        return False

    # Check an empty find.
    if len(db.find(COLLECTION, fail_selector)) != 0:
        print "find_test: Empty selection failed"
        return False

    return True

def find_stress_test():
    # Setup test.
    num_documents = 50

    for i in range(num_documents):
        db.insert(COLLECTION, {"name": i})

    # Check that all the documents are returned.
    if len(db.find(COLLECTION)) != num_documents:
        print "find_stress_test: All document selection failed."
        return False

    # Check that the correct number of documents are returned.
    limit = 7
    if len(db.find(COLLECTION, limit=limit)) != limit:
        print "find_stress_test: Limited document selection failed."
        return False

    return True

def clean():
    db.drop(COLLECTION)

def run_tests():
    result = True
    clean()

    result = result and insert_test()
    clean()

    result = result and find_test()
    clean()

    result = result and find_stress_test()
    clean()

    if result:
        print "Test completed"

run_tests()
