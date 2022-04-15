# mock

测试桩：模拟被测对象的返回，用于测试。通常意义的 mock 指的是 mock server ，模拟服务端返回的接口数据，用于前端开发，第三方接口联调

为什么要用 mock ？
1. 由于前后端开发进度不一致，如果前段开发速度快于后端，这时候需要一个假的接口用于模拟后端返回
2. 由于项目需要用到第三方接口，如果第三方接口未开发完成或者第三方接口没有测试环境，为了保证进度，需要模拟接口调试


如何 mock ？
1. 利用抓包工具，比如 fiddler 
2. 可以利用 web 框架模拟，Django Flask


```py
# mock_server.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>hello Flask</h1>"


if __name__ == "__main__":
    app.run("127.0.0.1", "9999")
```




```py
#mock_client.py

import requests

resp = requests.get("http://127.0.0.1:9999")
print(resp.content)
```
