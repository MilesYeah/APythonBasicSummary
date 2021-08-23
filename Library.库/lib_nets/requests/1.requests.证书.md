

## SSL 证书验证

Requests 可以为 HTTPS 请求验证 SSL 证书，就像 web 浏览器一样。SSL 验证默认是开启的，如果证书验证失败，Requests 会抛出 SSLError:
```py
>>> requests.get('https://requestb.in')
requests.exceptions.SSLError: hostname 'requestb.in' doesn't match either of '*.herokuapp.com', 'herokuapp.com'
```

在该域名上我没有设置 SSL，所以失败了。但 Github 设置了 SSL:
```py
>>> requests.get('https://github.com', verify=True)
<Response [200]>
```

你可以为 verify 传入 CA_BUNDLE 文件的路径，或者包含可信任 CA 证书文件的文件夹路径：
```py
>>> requests.get('https://github.com', verify='/path/to/certfile')
```

或者将其保持在会话中：
```py
s = requests.Session()
s.verify = '/path/to/certfile'
```

注解: 如果 verify 设为文件夹路径，文件夹必须通过 OpenSSL 提供的 c_rehash 工具处理。

你还可以通过 REQUESTS_CA_BUNDLE 环境变量定义可信任 CA 列表。


## 不使用证书

如果你将 verify 设置为 False，Requests 也能忽略对 SSL 证书的验证。
```py
>>> requests.get('https://kennethreitz.org', verify=False)
<Response [200]>
```

默认情况下， verify 是设置为 True 的。选项 verify 仅应用于主机证书。

对于私有证书，你也可以传递一个 CA_BUNDLE 文件的路径给 verify。你也可以设置 # REQUEST_CA_BUNDLE 环境变量。




## 客户端证书
你也可以指定一个本地证书用作客户端证书，可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组：
```py
>>> requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))
<Response [200]>
```

或者保持在会话中：
```py
s = requests.Session()
s.cert = '/path/client.cert'
```

如果你指定了一个错误路径或一个无效的证书:
```py
>>> requests.get('https://kennethreitz.org', cert='/wrong_path/client.pem')
SSLError: [Errno 336265225] _ssl.c:347: error:140B0009:SSL routines:SSL_CTX_use_PrivateKey_file:PEM lib
```

本地证书的私有 key 必须是解密状态。目前，Requests 不支持使用加密的 key。



## CA 证书
Requests 默认附带了一套它信任的根证书，来自于 Mozilla trust store。然而它们在每次 Requests 更新时才会更新。这意味着如果你固定使用某一版本的 Requests，你的证书有可能已经 太旧了。

从 Requests 2.4.0 版之后，如果系统中装了 certifi 包，Requests 会试图使用它里边的 证书。这样用户就可以在不修改代码的情况下更新他们的可信任证书。

为了安全起见，我们建议你经常更新 certifi！

