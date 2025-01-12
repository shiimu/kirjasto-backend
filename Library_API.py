from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
from pymongo import ALL, MongoClient

app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():

    return "Allooo"

# Class for interacting with available books collection
class Available(Resource):
    def get(self):
        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['booksAvail']
        # had to make id not show, because it threw a not json serializable error.
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200

    def post(self):
        # Require these args for the POST request.
        parser = reqparse.RequestParser()
        parser.add_argument('name', required = True)
        parser.add_argument('writer', required = True)
        parser.add_argument('year', required = True)
        parser.add_argument('isbn', required = True)
        parser.add_argument('rating', required = True)
        parser.add_argument('about', required = True)
        parser.add_argument('tags', required = True)
        parser.add_argument('description', required = True)

        args = parser.parse_args()
        
# Checking if the book name already exists.        
        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['booksAvail']
        retrieved = list(collection.find({}, {'_id' : False}))
        for name in retrieved:

            if args['name'] in name['Name']:
                return {
                     'message': f"'{args['name']}' already exists."
                }, 401
        else:
            client = MongoClient('localhost', 27017)
            db = client['Laiberi']
            collection = db['booksAvail']
            new_book = collection.insert_one({
                'Name' : args['name'],
                'Writer' : args['writer'],
                'Year' : args['year'],
                'ISBN' : args['isbn'],
                'Rating' : args['rating'],
                'About' : args['about'],
                'Tags' : args['tags'],            
                'Description' : args['description']        
            
                })    
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
    
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required = True)
        parser.add_argument('writer', required = True)
        parser.add_argument('year', required = True)
        parser.add_argument('isbn', required = True)
        parser.add_argument('rating', required = True)
        parser.add_argument('about', required = True)
        parser.add_argument('tags', required = True)
        parser.add_argument('description', required = True)
        args = parser.parse_args()

        if args['name'] in list(collection['Name']):
            client = MongoClient('localhost', 27017)
            db = client['Laiberi']
            collection = db['booksAvail']
            updateBook = collection.find_one_and_replace({
                'Name' : args['name'],
                'Writer' : args['writer'],
                'Year' : args['year'],
                'ISBN' : args['isbn'],
                'Rating' : args['rating'],
                'About' : args['about'],
                'Description' : args['description']        
        })    

        retrieved = list(collection.find({}, {'_id' : False}))


        return retrieved, 200

    def delete(self):
    # Require these args for the DELETE request.

        parser = reqparse.RequestParser()
        parser.add_argument('name', required = True)
        parser.add_argument('writer', required = True)
        parser.add_argument('year', required = True)
        parser.add_argument('isbn', required = True)
        parser.add_argument('rating', required = True)
        parser.add_argument('about', required = True)
        parser.add_argument('tags', required = True)
        parser.add_argument('description', required = True)
        args = parser.parse_args()

        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['booksAvail']
        removeBook = collection.find_one_and_delete({
            'Name' : args['name'],
            'Writer' : args['writer'],
            'Year' : args['year'],
            'ISBN' : args['isbn'],
            'Rating' : args['rating'],
            'About' : args['about'],
            'Description' : args['description']        
        })    
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
        

    def push(self):
        return 401
# Class for interacting with borrowed books collection
class Borrowed(Resource):
    def get(self):
        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['booksBorrow']
        # had to make id not show, because it threw a not json serializable error.
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200

    def post(self):
    # Require these args for the POST request.

        parser = reqparse.RequestParser()
        parser.add_argument('name', required = True)
        parser.add_argument('writer', required = True)
        parser.add_argument('year', required = True)
        parser.add_argument('isbn', required = True)
        parser.add_argument('rating', required = True)
        parser.add_argument('about', required = True)
        parser.add_argument('tags', required = True)
        parser.add_argument('description', required = True)
        parser.add_argument('borrower', required = True)


        args = parser.parse_args()

        
# Checking if the book name already exists.        
        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['booksBorrow']
        retrieved = list(collection.find({}, {'_id' : False}))
        for name in retrieved:

            if args['name'] in name['Name']:
                return {
                     'message': f"'{args['name']}' already exists."
                }, 401
        else:
            client = MongoClient('localhost', 27017)
            db = client['Laiberi']
            collection = db['booksBorrow']
            new_book = collection.insert_one({
                'Name' : args['name'],
                'Writer' : args['writer'],
                'Year' : args['year'],
                'ISBN' : args['isbn'],
                'Rating' : args['rating'],
                'About' : args['about'],
                'Tags' : args['tags'],            
                'Description' : args['description'],
                'Borrower' : args['borrower']
            
                })    

        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
    
    def put(self):
# Checking if the book name already exists.        
        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['booksBorrow']
        retrieved = list(collection.find({}, {'_id' : False}))
        
        for name in retrieved:
            if args['name'] in name['Name']:
                return {
                     'message': f"'{args['name']}' already exists."
                }, 401
        else:
            client = MongoClient('localhost', 27017)
            db = client['Laiberi']
            collection = db['booksBorrow']
            new_book = collection.insert_one({
                'Name' : args['name'],
                'Writer' : args['writer'],
                'Year' : args['year'],
                'ISBN' : args['isbn'],
                'Rating' : args['rating'],
                'About' : args['about'],
                'Tags' : args['tags'],            
                'Description' : args['description']        
            
                })    

        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
    def delete(self):
       # Require these args for the DELETE request.

        parser = reqparse.RequestParser()
        parser.add_argument('name', required = True)
        parser.add_argument('writer', required = True)
        parser.add_argument('year', required = True)
        parser.add_argument('isbn', required = True)
        parser.add_argument('rating', required = True)
        parser.add_argument('about', required = True)
        parser.add_argument('tags', required = True)
        parser.add_argument('description', required = True)
        parser.add_argument('borrower', required = True)

        args = parser.parse_args()

        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['booksBorrow']
        removeBook = collection.find_one_and_delete({
            'Name' : args['name'],
            'Writer' : args['writer'],
            'Year' : args['year'],
            'ISBN' : args['isbn'],
            'Rating' : args['rating'],
            'About' : args['about'],
            'Description' : args['description'],
            'Borrower' : args['borrower']        
        })    
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
        

    def push(self):
        return 401

# Class for interacting with comments collection
class Comments(Resource):
    def get(self):
        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['comments']
        # had to make id not show, because it threw a not json serializable error.
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200

    def post(self):
        # Require these args for the POST request.
        parser = reqparse.RequestParser()
        parser.add_argument('commenter', required = True)
        parser.add_argument('message', required = True)

        args = parser.parse_args()

        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['comments']
        new_book = collection.insert_one({
            'Commenter' : args['commenter'],
            'Message' : args['message'],     
        })    
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
    
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('commenter', required = True)
        parser.add_argument('message', required = True)

        args = parser.parse_args()

        if args['name'] in list(collection['Name']):
            client = MongoClient('localhost', 27017)
            db = client['Laiberi']
            collection = db['booksAvail']
            updateBook = collection.find_one_and_replace({
                'Commenter' : args['commenter'],
                'Message' : args['message'],     
        })    

        retrieved = list(collection.find({}, {'_id' : False}))


        return retrieved, 200

    def delete(self):
    # Require these args for the DELETE request.

        parser = reqparse.RequestParser()
        parser.add_argument('commenter', required = True)
        parser.add_argument('message', required = True)
        args = parser.parse_args()

        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['booksAvail']
        removeBook = collection.find_one_and_delete({
            'Commenter' : args['commenter'],
            'Message' : args['message'],          
        })    
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
        

    def push(self):
        return 401

api.add_resource(Available, '/available')
api.add_resource(Borrowed, '/borrowed')
api.add_resource(Comments, '/comments')


# Runs on port 8080!!
if __name__ == "__main__":
    app.run( debug = True, host='127.0.0.1', port=8080 )