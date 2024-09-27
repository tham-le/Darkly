# Cross-Site scripting (XSS) feedback vulnerability report

### Location: ***http://192.168.56.3/index.php?page=feedback***

## Description:

This vulnerability allows attackers to inject malicious scripts into the page, potentially compromising user sessions and stealing sensitive information.

The **Name** and **Message** fields are vulnerable to XSS attacks. No apparent server-side validation or sanitization of user inputs.

```
<textarea name="mtxtMessage" cols="50" rows="3" maxlength="50"></textarea>
```

We can submit this script in the both fields:
```
<script>
    alert("XSS")
</script>
```

There is no validation to filter user input.

An attacker could steal session cookies or tokens. Sensitive information could be accessed and exfiltrated.

## Recommendations:

1. The simplest way to eliminate XSS breaches is to pass all external data through a filter to remove dangerous keywords, for example, the ```<script>``` tag, JavaScript commands, CSS styles, and other dangerous HTML elements.
In some cases, a filter could even eliminate all special characters.

2. All variables in a web application needs to be protected.

3. For JSON, verify that the ```Content-Type``` header is ```application/json``` and not simple ```text/html``` to prevent XSS.