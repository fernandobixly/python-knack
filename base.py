import json
import requests
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Logger initialized.")

  
"""Knack API requests and responses wrapper/proxy.
Objective: have a simple way of sharing and using access tokens
and serializing/deserializing data to/from the API.
"""
class Base(object):
  application_id = None
  rest_api_key = None
  
  _session = None

  def make_request(klass, url, data=None):
    logging.debug("GET {url} - data: {data}".format(url=str(url), data=str(data)))
    response = klass._session.get(url)
    try:
      return response.json()
    except:
      logging.info(response)
      raise
    
  @classmethod
  def setup(klass, application_id, rest_api_key):
    klass.rest_api_key = rest_api_key
    klass.application_id = application_id
    klass.headers = {
      'X-Knack-Application-Id': klass.application_id,
      'X-Knack-REST-API-Key': klass.rest_api_key
    }
    klass._session = requests.Session()
    klass._session.headers.update(klass.headers)
    
