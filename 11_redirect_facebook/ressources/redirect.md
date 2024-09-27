# Open redirect vulnerability report

### Location ***http://192.168.56.3/index.php?page=redirect&site=facebook***

## Description

An Open Redirect Vulnerability occurs when a web application accepts a user-controlled input that directs the user to a different URL.
Attackers can exploit this breach by crafting malicious URLs that redirect users to phishing sites.

Here we see the JavaScript from our BornToSec page.

```
<a href="index.php?page=redirect&amp;site=facebook" class="icon fa-facebook"></a>
```

We can create our custom malicious destination. For example to **http://malicious.com**.

```http://192.168.56.3/index.php?page=redirect&site=malicious.com```

There is no validation URL function in JavaScript.

## Recommendations:

Code the function, for example ```isValidUrl``` that checks the extracted redirect URL is in a valid format, ensuring it begins with ```http://``` or ```https://``` and adheres to standard URL conventions.

Before redirecting, we should check if the extracted URL is valid. If it is valid, the user is redirected to the specified URL. 

Otherwise, the user is redirected to a default safe URL, such as homepage of landing page.