# Cross-Site scripting (XSS) Media vulnerability report

### Location: ***http://192.168.56.3/?page=media&src=nsa***

## Description:

This XSS vulnerability  found in a media handling system.

The application uses an `<object>` tag to display media content. When inspecting the source code of the page, we can see html:

```
 <object data="http://192.168.56.3/images/nsa_prism.jpg"></object>
```

However, this [**data**](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data) attribute can be modified directly from the client side, allowing for potential exploitation.

The `data:` scheme allows embedding small files inline in documents. However, it poses significant security risks when used improperly.

We can _modify_ the **src** parameter in the URL:

***http://192.168.56.3/?page=media&src=hello***

This results in the following HTML being rendered:

```
<object data="hello"></object>
```

_Craft_ a simple XSS payload using a `data:` URL:

```
data:text/html,<script>alert(1)</script>
```
in the URL parameter id.

But we need to _encode_ the entire `data:` text in _Base64_. We can make it in bash terminal directly with this command:

echo -n `"<script>alert(1)</script>"`|base64

It gives us:

_PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==_

_Visiting_ this URL will execute the XSS payload and we get a **Flag**!

***http://192.168.56.3/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==***

## Recommendations:

1. Implement proper input _validation_ and _sanitization_ for the `src` parameter.

2. Use [_Content Security Policy (CSP)_](https://portswigger.net/web-security/cross-site-scripting/content-security-policy) headers to restrict executable content.

3. Avoid using `data:` URLs for untrusted content.