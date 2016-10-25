import time
import datetime

def import_events(client, file):
  f = open(file, 'r')
  count = 0
  print "Importing data..."
  ts = time.time()
  st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
  print 'Start Time : '+st
  for line in f:
    data = line.rstrip('\r\n').split('|') 
    client.create_event(
        event="rate",
        entity_type="user",
        entity_id=data[0],
        target_entity_type="item",
        target_entity_id=data[1],
        properties= { "rating" : float(data[2]) }
      )
    count += 1
    print str(count)
  ts = time.time()
  st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
  print 'End Time : '+st
client = predictionio.EventClient(
  
  url='http://localhost:7070',
  threads=1000,
  qsize=4000)
import_events(client, 'userstomovie.txt')
