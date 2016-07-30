Simple Knack Wrapper
---

This is a simple wrapper made for (https://www.knack.com)[https://www.knack.com]. 
It supports paginated queries and provides enough functionality to browse an object's data
from python.

It has only been tested with root access keys but maybe it works with page access keys as well.
Let me know!

A sample use case is a simple backup script that pulls in all the records from a list of
object ids and outputs them to separate csv files per object id:


'''
import knack
import csv
import logging
import console

logging.basicConfig(level=logging.INFO)

application_id = 'your-application-id'
rest_api_key = 'your-rest-api-key'
objects_to_backup = [] # enter the object ids you want to download

knack.Base.setup(application_id, rest_api_key)

if __name__ == '__main__':
  for id in objects_to_backup:
    filename = 'object_{object_id}.csv'.format(object_id=id)
    
    with open(filename, 'w', encoding='utf-8') as csvfile:
      knack_object = knack.KnackObject(id)
      fieldnames = knack_object.fields.keys()
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
      
      for record in knack_object.records:
        writer.writerow(record.attributes())
        
    logging.info('Done writing {filename}'.format(filename=filename))
    console.quicklook(filename)
    
  logging.info('Script finished successfully.')
'''

Feel free to use/modify/comment.

- Jose
