# Cookies I_am_admin vulnerability report

Location: client-side Application/Storage/Cookies

## Description:

This breach allows unauthorized access to administrative privileges through a simple string manipulation attack.

A cookie named ***"I_am_admin"*** exists on the client-side application.

***68934a3e9455fa72420237eb05902327***.

The value of this cookie is encrypted using MD5 hashing. The current decrypted value of the cookie is ```false```.

It possible to encrypt ```true``` in MD5 and set it as the value of this cookie.

***b326b5062b2f0e69046810717534cb09***

## Recommendations:

1. Move sensitive cookies like "I_am_admin" to server-side storage.

2. Replace cookie-based authentication with a more secure metod, such as token-based authentication.

3. Ensure all sensitive data is properly encrypted both at rest and in transit.