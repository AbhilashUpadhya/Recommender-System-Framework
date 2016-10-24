import time
import datetime

#movie id | movie title | release date | video release date | IMDb URL 
def import_events(client,file):
  f = open(file, 'r')
  count = 0
  print "Importing data..."
  for line in f:
    data = line.rstrip('\r\n').split('|') 
    genres = data[10].rstrip('\r\n').split('^')
    client.create_event(
      event="$set",
      entity_type="item",
      entity_id=data[0],
      properties={
        'genres' : genres,
	'title' : data[1],
	'release' : data[3],
	'url': data[4]
      }
    )
#    print "\nTitle: " + str(title) +"\n" + "Year: "+ str(year)+"\n"+"URL: "+ str(url)+ "\n"+ "Genre: "					
    count += 1
  print str(count)
client = predictionio.EventClient(
 
  url='http://localhost:7070',
  threads=500,
  qsize=4000)
import_events(client,'items.txt')
