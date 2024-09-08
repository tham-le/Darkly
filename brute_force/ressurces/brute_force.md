# Brute force attack report

A brute force breach for an **admin** password using a password.txt
and Python script.

## Overview

The attack uses a _dictionary-based_ approach, attempting various password
stored in the file named **_"password.txt"_** downloaded from _Daniel Miessler's SecLists_

The first thing that the script does is define a signal handler to handle the SIGINT signal. If the user decides to interrupt the script by pressing `CTRL+C`, the script will exit gracefully.

Next, the script defines a function called "makeBruteForce". This function reads passwords from **_"password.txt"_** and attempts each against the target system.

Finally, the scripts checks if the **name** variable is **main**.
This checks if the script is being run directly (not imported) and calls the
brute force function.

## Attack mechanism

1. **Target**: the script targets a web application at IP address 192.168.56.3.
2. **Username**: it uses a fixed username **admin**.
3. **Password Attempts**: passwords are read line by line from **_"password.txt"_**.
4. **HTTP Response**: the site always return a _200 status code_ response, regardless of whether the password is correct or not.
5. **Detection**: instead of relying on HTTP status codes, the script uses HTML
parsing to detect successful logins.
6. **HTML parsing**: BeautifulSoup is used to parse HTML  content of each response.
7. **Wrong answer**: the presence of an image named **_"WrongAnswer.gif"_** indicates an incorrect password attempt.

## Preventing brute attack

1. Impliment strong password policies and multi-factor authentication.
2. Monitor of unsuccessful login attempts
3. Impliment proper HTTP status codes for authentication failures(e.g., _401 Unauthorized_).
4. Using **CAPTCHA** challenges after several failed login attempts.