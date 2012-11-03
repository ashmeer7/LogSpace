class LogEntry(object):
  #fields is defined by each of the extending classes and useful for them
  def __init__(self, date, entry_type, fields):
    self.date = date
    self.entry_type = entry_type
    self.fields = fields 
  
  #field_depth is a list to traverse down 
  def get_value(self, field_items):
    current_item = self.fields
    for field_item in field_items:
      current_item = current_item[field_item]
    return current_item
