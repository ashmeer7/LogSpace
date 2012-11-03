import sys
sys.path.insert(0, "../../src/logs")
import entry

def assert_list_equal(list1, list2):
  condition = True
  for i in range(len(list1)):
    condition = condition and list1[i] == list2[i]
    if condition == False:
      return False
  for i in range(len(list2)):
    condition = condition and list1[i] == list2[i]
    if condition == False:
      return False
  return True

def test1():
  my_entry = entry.LogEntry("Now", "blank", {})
  return True

def test2():
  field = {}
  field["danny"] = "fail"
  my_entry = entry.LogEntry("Now", "blank", field)
  if my_entry.get_value(["danny"]) == "fail":
    return True
  else:
    return False

def test3():
  field = {}
  subfield = {}
  field["what time"] = subfield
  subfield["is it"] = "game time"
  my_entry = entry.LogEntry("Now", "blank", field)
  if my_entry.get_value(["what time", "is it"]) == "game time":
    return True
  else:
    return False

def runTests():
  if not test1():
    print "Test 1 failed"
  elif not test2():
    print "Test 2 failed"
  elif not test3(): 
    print "Test 3 failed"
  else:
    print "Pass"

runTests()
