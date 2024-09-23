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

