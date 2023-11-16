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
 
https://postgres-sql-6aba726b2968.herokuapp.com/jemsa/users

https://postgres-sql-6aba726b2968.herokuapp.com/jemsa/racks

https://postgres-sql-6aba726b2968.herokuapp.com/jemsa/receivers

https://postgres-sql-6aba726b2968.herokuapp.com/warehouses

https://postgres-sql-6aba726b2968.herokuapp.com/jemsa/suppliers

https://postgres-sql-6aba726b2968.herokuapp.com/jemsa/transactions

https://postgres-sql-6aba726b2968.herokuapp.com/jemsa/incoming_transactions

https://postgres-sql-6aba726b2968.herokuapp.com/jemsa/outgoing_transactions

https://postgres-sql-6aba726b2968.herokuapp.com/jemsa/transfer_transactions

https://postgres-sql-6aba726b2968.herokuapp.com/jemsa/receivers

---
## Routes for Statistics
https://postgres-sql-6aba726b2968.herokuapp.com/jemsa/warehouse (Append ID and specific route + json body with userID for validation)

https://postgres-sql-6aba726b2968.herokuapp.com/jemsa/most (Append specific route)

https://postgres-sql-6aba726b2968.herokuapp.com/jemsa/least (same as above)

---
Json Specifics provided in excel file.
