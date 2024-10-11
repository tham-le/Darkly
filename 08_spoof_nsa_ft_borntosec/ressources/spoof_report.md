# Client-side spoofing vulnerability report

### Location: 
***http://192.168.56.3/index.php***

***http://192.168.56.3/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f***

## Description:

When inspecting root page we can press on `©BornToSec` link in the footer part and we will be redirected on this URL:

***http://192.168.56.3/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f***

Exploring _source_ page we got this _result_:
```
<a href="https://www.youtube.com/watch?v=Bznxx12Ptl0">
    <img src="images/albatroz.jpg"
    onload="coucou()"> event
</a>
```
We can read the paragraph with Lorem Ipsum text and the _requirements_:

```
<!--
You must come from : "https://www.nsa.gov/".
-->
...
<!--
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```

We can also get this result using a curl command line in our terminal:

`curl http://192.168.56.3/index.php\?page\=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`

Based on the information provided, here is how we can _construct_ a curl command that meets the requirements:

`curl -A "ft_bornToSec" -e "https://www.nsa.gov/" "http://192.168.56.3/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"`

1. **User-Agent spoofing** (`-A "ft_bornToSec"`): sets a custom User-Agent/browser header to _"ft_bornToSec"_ as requested, to mimic a specific browser.

2. **Referer Header spoofing** (`-e "https://www.nsa.gov/"`): sets Referer header to _"https://www.nsa.gov/"_, making it appear as though the request comes from the NSA website.


This is a form client-side spoofing.

Inspecting the result we can find a **Flag**.

## Recommendations:

1. **Server-side validation**: implement strict validation of all input parameters on the server-side, regardless of what the client sends.

2. Implement HTTPS and SSH for web communications.

3. Use multi-factor authentication.

4. Implement solutions for detecting DNS spoofing, IP spoofing or ARP spoofing: Wireshark, Snort, Nmap