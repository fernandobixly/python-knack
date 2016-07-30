class Record(object):  
  def __init__(self, record_data, record_fields):
    self.fields = record_fields
    self.data = record_data
    self.map_fields()
  
  def map_fields(self):
    [self.__setattr__(field, self.data[self.fields[field].key]) for field in self.fields]
    
  def attributes(self):
    attributes = {key: self.__dict__[key]for key in self.__dict__ if key !='fields' and key !='data'}
    
    return attributes
