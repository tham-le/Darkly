# Brute force attack report

### Location: ***http://192.168.56.3/index.php?page=signin***

## Description:

A brute force breach for an **admin** password using a password.txt
and Python script.


The attack uses a _dictionary-based_ approach, attempting various password
stored in the file named ***"password.txt"*** downloaded from _Daniel Miessler's SecLists_

The first thing that the script does is define a signal handler to handle the SIGINT signal. If the user decides to interrupt the script by pressing `CTRL+C`, the script will exit gracefully.

Next, the script defines a function called "makeBruteForce". This function reads passwords from ***"password.txt"*** and attempts each against the target system.

Finally, the scripts checks if the **name** variable is **main**.
This checks if the script is being run directly (not imported) and calls the
brute force function.

Run the script using the Python interpreter:
```
python3 get_password.py
```

## Attack mechanism:

1. **Target**: the script targets a web application at IP address _192.168.56.3_.

2. **Username**: it uses a fixed username ***"admin"***.

3. **Password Attempts**: passwords are read line by line from ***"password.txt"***.

4. **HTTP Response**: the site always return a _200 status code_ response, regardless of whether the password is correct or not.

5. **Detection**: instead of relying on HTTP status codes, the script uses HTML
parsing to detect successful logins.

6. **HTML parsing**: BeautifulSoup is used to parse HTML  content of each response.

7. **Wrong answer**: the presence of an image named ***"WrongAnswer.gif"*** indicates an incorrect password attempt.

8. **Get a password**: ***shadow*** 

## Recommendations:

1. Impliment _strong_ password policies and ***multi-factor authentication***.

2. Monitor of unsuccessful login attempts.

3. Impliment proper HTTP status codes for authentication failures(e.g., _401 Unauthorized_).

4. Using ***CAPTCHA*** challenges after several failed login attempts.