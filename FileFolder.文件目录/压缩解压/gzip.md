# gzip



为了以文本形式读取压缩文件，可以这样做：
```py
# gzip compression
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()
```

类似的，为了写入压缩数据，可以这样做：
```py
# gzip compression
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)
```
如上，所有的I/O操作都使用文本模式并执行Unicode的编码/解码。 类似的，如果你想操作二进制数据，使用 rb 或者 wb 文件模式即可。




## ref
* [读写压缩文件](https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p07_read_write_compressed_datafiles.html)
* []()
* []()
* []()
* []()
* []()
* []()
* []()

