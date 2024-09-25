# Recover page vulnerability report

### Location: ***http://192.168.56.3/index.php?page=recover***

## Description:

A significant vulnerability was discovered in the password recovery functionality of ***Signin*** page. Specifically, when user initiates the _"I forgot my password"_ process and is redirected to the recovery page.

The recovery page contains a hidden form input with the _hardcoded_ webmaster's email address (***"webmaster@borntosec.com"***). The mail address could be accessed by any user visiting the recovery page. This exposes the webmaster's contact information, potentially leading to targeted _phishing_ attempts or other forms of attack.

## Recommendations:

1. Remove hardcoded sensitive information from the client-side code. **_Store_ sensitive information securely on the _server-side_ and _retrieve_ it dynamically when needed**.

2. Impliment server-side validation. Develop robust server-side validation for all form submissions. **_Sanitize_ and _validate_ all user inputs before processing**.