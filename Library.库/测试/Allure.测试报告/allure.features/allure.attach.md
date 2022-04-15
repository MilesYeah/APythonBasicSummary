# allure.attach

报告可以显示许多不同类型的附件，这些附件可以补充测试、step 或 fixture 结果。可以通过调用如下方法添加 attachment：

## allure.attach(body, name, attachment_type, extension):
1. body
   1. 要写入文件的原始内容。
   2. 要显示的内容
2. name
   1. 包含文件名的字符串
   2. 附件名称
3. attachment_type
   1. 附件类型，是 allure.attachment_type 的其中一种。 
   2. 支持:HTML,JPG,PNG,JSON,OTHER,TEXTXML
4. extension
   1. 附件扩展名，比较少用
   2. 提供的将用作创建文件的扩展名



## allure.attachment_type提供的附件类型

allure.attachment_type

```py
class AttachmentType(Enum):

    def __init__(self, mime_type, extension):
        self.mime_type = mime_type
        self.extension = extension

    TEXT = ("text/plain", "txt")
    CSV = ("text/csv", "csv")
    TSV = ("text/tab-separated-values", "tsv")
    URI_LIST = ("text/uri-list", "uri")

    HTML = ("text/html", "html")
    XML = ("application/xml", "xml")
    JSON = ("application/json", "json")
    YAML = ("application/yaml", "yaml")
    PCAP = ("application/vnd.tcpdump.pcap", "pcap")

    PNG = ("image/png", "png")
    JPG = ("image/jpg", "jpg")
    SVG = ("image/svg-xml", "svg")
    GIF = ("image/gif", "gif")
    BMP = ("image/bmp", "bmp")
    TIFF = ("image/tiff", "tiff")

    MP4 = ("video/mp4", "mp4")
    OGG = ("video/ogg", "ogg")
    WEBM = ("video/webm", "webm")

    PDF = ("application/pdf", "pdf")
```




## allure.attach.file(source, name, attachment_type, extension):
1. source
   1. 文件路径的字符串。
2. 其他参数和上面的一致


```py
import allure
import pytest


@pytest.fixture
def attach_file_in_module_scope_fixture_with_finalizer(request):
    allure.attach('A text attacment in module scope fixture', 'blah blah blah', allure.attachment_type.TEXT)
    def finalizer_module_scope_fixture():
        allure.attach('A text attacment in module scope finalizer', 'blah blah blah blah', allure.attachment_type.TEXT)
    request.addfinalizer(finalizer_module_scope_fixture)


def test_with_attacments_in_fixture_and_finalizer(attach_file_in_module_scope_finalizer):
    pass


def test_multiple_attachments():
    allure.attach.file('./data/totally_open_source_kitten.png', attachment_type=allure.attachment_type.PNG)
    allure.attach('<head></head><body> a page </body>', 'Attach with HTML type', allure.attachment_type.HTML)
```


附件显示在它们所属的测试实体的上下文中。HTML类型的附件将呈现并显示在报告页上。
这是一种方便的方法，可以为您自己的测试结果表示提供一些定制。


