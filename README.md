# kirjasto-backend

Api endpoints:

127.0.0.1:8080/

GET, POST, PUT, DELETE

POST, PUT and DELETE currently require all of the arguments listed below

available - lists all the books available for loaning.
arguments: name, writer, year, isbn, rating, about, tags, description

borrowed - lists all the books that are currently being loaned out.
arguments: name, writer, year, isbn, rating, about, tags, description, borrower

comments - lists all the comments.
arguments: commenter, message
