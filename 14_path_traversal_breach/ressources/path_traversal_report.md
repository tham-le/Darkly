# Path traversal or "backtracking" vulnerability report

### Location ***http://192.168.56.3/index.php?page=member***

## Description

The website uses a dynamic inclusion mechanism where each page is represented by a file on the server. The **page** parameter in the URL determines which file is displayedThis approach creates a vulnerability known as **path traversal** or **directory traversal**. 


For example:

`http://192.168.56.3/index.php?page=member`
for user research page.

This URL structure allows attackers to manipulate **page** parameter to traverse the server's directory structure. By using special character sequences like **"../"**, an attacker can _move up_ the directory hierarchy and potentially access sensitive files _outside_ the intended web _root_ directory. 

Using curl, we can demonstrate the vulnerability:
```
curl 'http://192.168.56.3/index.php?page=../../../../../../../../../../etc/passwd/'
```

This request successfully retrieves the Flag on the site. This demonstrates the severity of the vulnerability, as it allows unauthorized access to system files.

To streamline our testing process and explore various path combinations, we developed a Python script to automate the routine of finding flag.

## Recommendations:

1. Avoid passing any filenames or paths in user input whenever possible.

2. Implement a whitelist of safe files that can be accessed through the dynamic inclusion mechanism.

3. Use a mapping system instead of direct file names. For example, map "member" to "var/www/html/member.php".
    - define a mapping:
    ```
    $pageMapping = [
        'member' => '/var/www/html/member.php',
        'admin' => '/var/www/html/admin.php',
        'home' => '/var/www/html/home.php',
    ]
    ```
    - In PHP code, use this mapping instead of directly accessing files:
    ```
    $requestedPage = $_GET['page'];

    if (isset($pageMapping[$requestedPage])) {
        include $pageMapping[$requestedPage];
    } else {
        // Handle invalid page request
        header('HTTP/1.1 404 Not Found');
        echo 'Page not found';
    }
    ```

4. Implement input validation and sanitization of the **page** parameter. 