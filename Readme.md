# Team Name: JEMSA 
___
### Participants
Alex Y. Agosto Figueroa - alex.agosto@upr.edu 

María H. Cotto Nieves - maria.cotto@upr.edu 

Sebastián O. Espinosa Del Rosario - sebastian.espinosa@upr.edu 

Joy A. Martínez Guadalupe - joy.martinez@upr.edu 

Edwin J. Vega Reyes - edwin.vega4@upr.edu

---
### Heroku Credentials:

Host: ec2-34-202-53-101.compute-1.amazonaws.com

Database: d4b4cfrn0mrp8p

User: mzytobqvjwsson

Port: 5432

Password: b2a8350a67754fe49c4c3ab554e3b13a5d258d587826c7ecab8a4169c064699c

URI: postgres://mzytobqvjwsson:b2a8350a67754fe49c4c3ab554e3b13a5d258d587826c7ecab8a4169c064699c@ec2-34-202-53-101.compute-1.amazonaws.com:5432/d4b4cfrn0mrp8p

Heroku CLI: heroku pg:psql postgresql-vertical-44021 --app postgres-sql
___

## Routes for Entities 
Change http://127.0.0.1:5000/ (Localhost) to whatever app.py gives you if needed.
 
http://127.0.0.1:5000/jemsa/users

http://127.0.0.1:5000/jemsa/racks

http://127.0.0.1:5000/jemsa/users

http://127.0.0.1:5000/jemsa/warehouses

http://127.0.0.1:5000/jemsa/suppliers

http://127.0.0.1:5000/jemsa/transactions

http://127.0.0.1:5000/jemsa/incoming_transactions

http://127.0.0.1:5000/jemsa/outgoing_transactions

http://127.0.0.1:5000/jemsa/transfer_transactions

http://127.0.0.1:5000/jemsa/receivers

---
## Routes for Statistics
http://127.0.0.1:5000/jemsa/warehouse (Append ID and specific route + json body with userID for validation)

http://127.0.0.1:5000/jemsa/most (Append specific route)

http://127.0.0.1:5000/jemsa/least (same as above)

---
Json Specifics provided in excel file.