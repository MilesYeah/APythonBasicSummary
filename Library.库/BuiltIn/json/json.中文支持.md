

# json序列化时，默认遇到中文会转换成unicode，如果想要保留中文怎么办？

在序列化是将json.dumps中的默认参数ensure_ascii改为False就可以保留中文了
`json.dumps(obj,ensure_ascii=False)`
