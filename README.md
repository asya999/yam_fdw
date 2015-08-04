
Yet Another Postgres FDW for MongoDB 
====================================
based on [multicorn](http://multicorn.org)

How to use:
----------

```
Install Postgres
Install Multicorn
sudo python setup.py install

CREATE EXTENSION multicorn;
CREATE create SERVER mongodb_proxy_server FOREIGN DATA WRAPPER multicorn OPTIONS (wrapper 'yam_fdw.Yamfdw');
CREATE FOREIGN TABLE foo ( "_id" varchar OPTIONS (type 'ObjectId'), f1_f2 numeric OPTIONS (mname 'a.b'), d varchar )
   SERVER mongodb_proxy_server OPTIONS ( db 'test', collection 'foo' [, host 'hostNameOrIp', port: '27017', user 'myusername', password 'mypassword' ] );

```
