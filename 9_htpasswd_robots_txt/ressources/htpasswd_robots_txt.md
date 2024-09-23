# WP-admin password via htpasswd vulnerability report

Location:

***http://192.168.56.3/robots.txt***

***http://192.168.56.3/whatever/***

***http://192.168.56.3/admin/***


## Description

The ```robots.txt``` file serves as an initial checkpoint for search engine bots when they arrive at the website, providing them with instaructions about which URLs they are prohibited from visiting.

It is a simple text file that is uploaded to the root of the domain. It serves as the loacation that search engine bots and other spiders including AI/LLM crawlers automatically visit to check for specific rules about they _may_ or _may not_ crawl.

If we visit our file at the URL:

***http://192.168.56.3/robots.txt***

We got this result:

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

The ```User-agent```: tells who the rules are for. Here we apply directives to all crawlers and bots.

The ```Disallow```: which directories, files are forbidden. Here we tell bots not to crawl or index anything under the _"/whatever"_ and _"./hidden"_ directories.

When we go to the URL:

***http://192.168.56.3/whatever/***

There is ```htpasswd``` file that contains the line with root user credentials:
```
root:437394baff5aa33daa618be47b75cb49
```

Now when we know the credentials we can test to access to wp-amdin user profile via _"unsecured admin panel"_. The site has a security risk called an _"exposed administrative interface"_.

We decrypted the password from Md5: qwerty123@.

Login as root at

***http://192.168.56.3/admin/***

and we got the flag.

## Recommendations:

1. Use HTTPS.

2. Change admin URL, modify the WordPress config to use a less predictable URL for the admin panel.

3. Use strong passwords, 2FA

4. Restrict access to the admin panel by IP address or impliment a VPN requirement.

5. Password protection is often better than robots.txt for truly sensitive content.

