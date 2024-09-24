# Hidden files vulnerability report

Location ***http://192.168.56.3/.hidden/***

## Description

When we checked URL

***http://192.168.56.3/robots.txt***

we got this result:

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

Now we go to _".hidden"_ directory to URL:

***http://192.168.56.3/.hidden/***

There is Index page of /.hidden/ directory with those folders:
```
../
amcbevgondgcrloowluziypjdh/                        29-Jun-2021 18:15
bnqupesbgvhbcwqhcuynjolwkm/                        29-Jun-2021 18:15
ceicqljdddshxvnvdqzzjgddht/                        29-Jun-2021 18:15
doxelitrqvhegnhlhrkdgfizgj/                        29-Jun-2021 18:15                   
eipmnwhetmpbhiuesykfhxmyhr/                        29-Jun-2021 18:15                   
ffpbexkomzbigheuwhbhbfzzrg/                        29-Jun-2021 18:15                   
ghouhyooppsmaizbmjhtncsvfz/                        29-Jun-2021 18:15                   
hwlayeghtcotqdigxuigvjufqn/                        29-Jun-2021 18:15                   
isufpcgmngmrotmrjfjonpmkxu/                        29-Jun-2021 18:15                   
jfiombdhvlwxrkmawgoruhbarp/                        29-Jun-2021 18:15                   
kpibbgxjqnvrrcpczovjbvijmz/                        29-Jun-2021 18:15                   
ldtafmsxvvydthtgflzhadiozs/                        29-Jun-2021 18:15                   
mrucagbgcenowkjrlmmugvztuh/                        29-Jun-2021 18:15                   
ntyrhxjbtndcpjevzurlekwsxt/                        29-Jun-2021 18:15                   
oasstobmotwnezhscjjopenjxy/                        29-Jun-2021 18:15                   
ppjxigqiakcrmqfhotnncfqnqg/                        29-Jun-2021 18:15                   
qcwtnvtdfslnkvqvzhjsmsghfw/                        29-Jun-2021 18:15                   
rlnoyduccpqxkvcfiqpdikfpvx/                        29-Jun-2021 18:15                   
sdnfntbyirzllbpctnnoruyjjc/                        29-Jun-2021 18:15                   
trwjgrgmfnzarxiiwvwalyvanm/                        29-Jun-2021 18:15                   
urhkbrmupxbgdnntopklxskvom/                        29-Jun-2021 18:15                   
viphietzoechsxwqacvpsodhaq/                        29-Jun-2021 18:15
whtccjokayshttvxycsvykxcfm/                        29-Jun-2021 18:15
xuwrcwjjrmndczfcrmwmhvkjnh/                        29-Jun-2021 18:15
yjxemfsgdlkbvvtjiylhdoaqkn/                        29-Jun-2021 18:15
zzfzjvjsupgzinctxeqtzzdzll/                        29-Jun-2021 18:15
README                                             29-Jun-2021 18:15
```

We need to make _web scraping_ to extract contents of all README files found in subdirectories and save the extract data to a single output file.

**Technologies used**

- Python 3.x
- Requests library for HTTP requests
- BeautifulSoup library for HTML parsing
- lxml parser for faster XML/HTML parsing

## Recommendations:

To avoid exposing sensitive data, there are several steps you can take:

1. Configure your web server to deny access to dotfiles. For exemple, for **Nginx** you can add this to your server block:
```
location ~/\. {
    deny all;
}
```
2. Move sensitive files outside the web root directory.

3. Use HTTPS.

4. Disable directory listing. When directory listing is enabled, the web server displays a list of files and folders within a directory, exposing sensitive information. It disabled by default in the **Nginx** config file. But if we use **Apache** we need to create _.htaccess_ file containing the following line:
```
Options - Indexes
```

And change your ```/etc/apache2/apache2.conf```

```
<Directory /var/www/>
        Options FollowSymLinks
</Directory>
```
