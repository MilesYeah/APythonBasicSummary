# requests.interfaces

## 主要接口
1. requests.request(method, url, **kwargs)
2. requests.head(url, **kwargs)
3. requests.get(url, params=None, **kwargs)
4. requests.post(url, data=None, json=None, **kwargs)
5. requests.put(url, data=None, **kwargs)
6. requests.patch(url, data=None, **kwargs)
7. requests.delete(url, **kwargs)

### parameters
| 参数            | 类型           | 是否必须   | 描述                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------- | -------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| method          |                |            | method for the new Request object.                                                                                                                                                                                                                                                                                                                                                                                                          |
| url             |                |            | URL for the new Request object.                                                                                                                                                                                                                                                                                                                                                                                                             |
| params          |                | (optional) | Dictionary or bytes to be sent in the query string for the Request.                                                                                                                                                                                                                                                                                                                                                                         |
| data            |                | (optional) | Dictionary or list of tuples [(key, value)] (will be form-encoded), bytes, or file-like object to send in the body of the Request.                                                                                                                                                                                                                                                                                                          |
| json            |                | (optional) | json data to send in the body of the Request.                                                                                                                                                                                                                                                                                                                                                                                               |
| headers         |                | (optional) | Dictionary of HTTP Headers to send with the Request.                                                                                                                                                                                                                                                                                                                                                                                        |
| cookies         |                | (optional) | Dict or CookieJar object to send with the Request.                                                                                                                                                                                                                                                                                                                                                                                          |
| files           |                | (optional) | Dictionary of 'name': file-like-objects (or {'name': file-tuple}) for multipart encoding upload. file-tuple can be a 2-tuple ('filename', fileobj), 3-tuple ('filename', fileobj, 'content_type') or a 4-tuple ('filename', fileobj, 'content_type', custom_headers), where 'content-type' is a string defining the content type of the given file and custom_headers a dict-like object containing additional headers to add for the file. |
| auth            |                | (optional) | Auth tuple to enable Basic/Digest/Custom HTTP Auth.                                                                                                                                                                                                                                                                                                                                                                                         |
| timeout         | float or tuple | (optional) | How many seconds to wait for the server to send data before giving up, as a float, or a (connect timeout, read timeout) tuple.                                                                                                                                                                                                                                                                                                              |
| allow_redirects | bool           | (optional) | Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to True.                                                                                                                                                                                                                                                                                                                                               |
| proxies         |                | (optional) | Dictionary mapping protocol to the URL of the proxy.                                                                                                                                                                                                                                                                                                                                                                                        |
| verify          |                | (optional) | Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to True.                                                                                                                                                                                                                                                           |
| stream          |                | (optional) | if False, the response content will be immediately downloaded.                                                                                                                                                                                                                                                                                                                                                                              |
| cert            |                | (optional) | if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.                                                                                                                                                                                                                                                                                                                                                             |




## 异常
| 异常                                         | 描述 |
| -------------------------------------------- | ---- |
| `requests.RequestException(*args, **kwargs)` |      |
| `requests.ConnectionError(*args, **kwargs)`  |      |
| `requests.HTTPError(*args, **kwargs)`        |      |
| `requests.URLRequired(*args, **kwargs)`      |      |
| `requests.TooManyRedirects(*args, **kwargs)` |      |
| `requests.ConnectTimeout(*args, **kwargs)`   |      |
| `requests.ReadTimeout(*args, **kwargs)`      |      |
| `requests.Timeout(*args, **kwargs)`          |      |



## 请求会话
1. class requests.Session
    * auth = None
    * cert = None
    * close()
    * cookies = None
    * delete(url, **kwargs)
    * get(url, **kwargs)
    * get_adapter(url)
    * get_redirect_target(resp)
    * head(url, **kwargs)
    * headers = None
    * hooks = None
    * max_redirects = None
    * merge_environment_settings(url, proxies, stream, verify, cert)
    * mount(prefix, adapter)
    * options(url, **kwargs)
    * params = None
    * patch(url, data=None, **kwargs)
    * post(url, data=None, json=None, **kwargs)
    * prepare_request(request)
    * proxies = None
    * put(url, data=None, **kwargs)
    * rebuild_auth(prepared_request, response)
    * rebuild_method(prepared_request, response)
    * rebuild_proxies(prepared_request, proxies)
    * request(method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None)
    * resolve_redirects(resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs)
    * send(request, **kwargs)
    * stream = None
    * trust_env = None
    * verify = None



## 低级类
1. class requests.Request(method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)
    * deregister_hook(event, hook)
    * prepare()
    * register_hook(event, hook)

2. class requests.Response
    * apparent_encoding
    * close()
    * content
    * cookies = None
    * elapsed = None
    * encoding = None
    * headers = None
    * history = None
    * is_permanent_redirect
    * is_redirect
    * iter_content(chunk_size=1, decode_unicode=False)
    * iter_lines(chunk_size=512, decode_unicode=None, delimiter=None)
    * json(**kwargs)
    * links
    * next
    * ok
    * raise_for_status()
    * raw = None
    * reason = None
    * request = None
    * status_code = None
    * text
    * url = None






## 更低级的类
1. class requests.PreparedRequest
    * body = None
    * deregister_hook(event, hook)
    * headers = None
    * hooks = None
    * method = None
    * path_url
    * prepare(method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)
    * prepare_auth(auth, url='')
    * prepare_body(data, files, json=None)
    * prepare_content_length(body)
    * prepare_cookies(cookies)
    * prepare_headers(headers)
    * prepare_hooks(hooks)
    * prepare_method(method)
    * prepare_url(url, params)
    * register_hook(event, hook)
    * url = None



2. class requests.adapters.BaseAdapter
    * close()
    * send(request, stream=False, timeout=None, verify=True, cert=None, proxies=None)

3. class requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=0, pool_block=False)
    * add_headers(request, **kwargs)
    * build_response(req, resp)
    * cert_verify(conn, url, verify, cert)
    * close()
    * get_connection(url, proxies=None)
    * init_poolmanager(connections, maxsize, block=False, **pool_kwargs)
    * proxy_headers(proxy)
    * proxy_manager_for(proxy, **proxy_kwargs)
    * request_url(request, proxies)
    * send(request, stream=False, timeout=None, verify=True, cert=None, proxies=None)



## 身份验证
1. class requests.auth.AuthBase
2. class requests.auth.HTTPBasicAuth(username, password)
3. class requests.auth.HTTPProxyAuth(username, password)
4. class requests.auth.HTTPDigestAuth(username, password)





## 编码
1. requests.utils.get_encodings_from_content(content)
2. requests.utils.get_encoding_from_headers(headers)
3. requests.utils.get_unicode_from_response(r)





## Cookie
1. requests.utils.add_dict_to_cookiejar(cj, cookie_dict)
2. requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
3. class requests.cookies.RequestsCookieJar(policy=None)
    * add_cookie_header(request)
    * clear(domain=None, path=None, name=None)
    * clear_expired_cookies()
    * clear_session_cookies()
    * copy()
    * extract_cookies(response, request)
    * get(name, default=None, domain=None, path=None)
    * get_dict(domain=None, path=None)
    * items()
    * iteritems()
    * iterkeys()
    * itervalues()
    * keys()
    * list_domains()
    * list_paths()
    * make_cookies(response, request)
    * multiple_domains()
    * pop(k[, d]) → v, remove specified key and return the corresponding value.
    * popitem() → (k, v), remove and return some (key, value) pair
    * set(name, value, **kwargs)
    * set_cookie_if_ok(cookie, request)
    * setdefault(k[, d]) → D.get(k,d), also set D[k]=d if k not in D
    * update(other)
    * values()
4. class requests.cookies.CookieConflictError




## 状态码查询
1. requests.codes
2. class requests.Request(method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)
    * deregister_hook(event, hook)
    * prepare()
    * register_hook(event, hook)
3. class requests.Response
    * apparent_encoding
    * close()
    * content
    * cookies = None
    * elapsed = None
    * encoding = None
    * headers = None
    * history = None
    * is_permanent_redirect
    * is_redirect
    * iter_content(chunk_size=1, decode_unicode=False)
    * iter_lines(chunk_size=512, decode_unicode=None, delimiter=None)
    * json(**kwargs)
    * links
    * next
    * ok
    * raise_for_status()
    * raw = None
    * reason = None
    * request = None
    * status_code = None
    * text
    * url = None





