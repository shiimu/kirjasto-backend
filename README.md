# kirjasto-backend

Api endpoints:

127.0.0.1:8080/

<b>GET, POST, PUT, DELETE</b>

POST, PUT and DELETE currently require all of the arguments listed below

<b>available</b> - lists all the books available for loaning. <br />
arguments: name, writer, year, isbn, rating, about, tags, description

<b>borrowed</b> - lists all the books that are currently being loaned out. <br />
arguments: name, writer, year, isbn, rating, about, tags, description, borrower

<b>comments</b> - lists all the comments. <br />
arguments: commenter, message
