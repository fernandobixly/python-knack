from .base import Base
from .field import Field
from .record import Record
import logging
import profile
import pstats
import inflection

class KnackObject(Base):
  API_URL = "https://api.knack.com/v1/objects/object_{id}"
  ENDPOINTS = {
    'records': '/records',
    'fields': '/fields'
  }
  
  ROWS_PER_PAGE = 500
  
  def __init__(self, knack_object_id):
    self.object_id = knack_object_id
    self.url = self.API_URL.format(id=self.object_id)
    self.raw_records = []
    self.records = []
    self.fields = []
    self.get_fields()
    self.get_records()
    
  def __getattr__(self, name):
    try:
      return self.__dict__[name]
    except(KeyError):
      raise AttributeError("'{object_name}' object has no attribute '{attr_name}'"\
        .format(object_name=self.__class__.__name__, attr_name=name))
    
  def get_fields(self):
    self.raw_fields = self.make_request(self.url + self.ENDPOINTS['fields'])
    self.fields = [Field(field) for field in self.raw_fields['fields']]
    self.fields = {inflection.parameterize(field.label, "_"): field for field in self.fields}
    return self.fields
    
  def get_records(self):
    page = 1
    grouped_records = []
    while True:
      endpoint_url = "{url}{endpoint}?page={current_page}&rows_per_page={rows_per_page}".format(\
        url=self.url,\
        endpoint=self.ENDPOINTS['records'],\
        current_page=page,\
        rows_per_page=self.ROWS_PER_PAGE\
      )
      response = self.make_request(endpoint_url)
      current_records = response['records']
      
      self.raw_records.append(current_records)
      grouped_records.append([Record(r, self.fields) for r in current_records])
      
      logging.debug(response)
      if str(response['total_pages']) == str(response['current_page']):
        break
      else:
        page += 1
    
    self.records = [r for record_group in grouped_records for r in record_group]
    return self.records

