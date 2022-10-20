from pymongo import MongoClient
import certifi

ca = certifi.where()
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.p5ctwmd.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

movie = db.movies.find_one({'title':'가버나움'})
star = movie['star']

all_movies = list(db.movies.find({'star':star},{'_id':False}))

for m in all_movies:
    print(m['title'])
