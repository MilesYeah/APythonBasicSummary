# Django filter

## 什么是过滤器
* 写在模板中，属于Django模板语言
* 可以修改模板中的变量，从而显示不同内容

## 如何使用过滤器
* \{\{ value \| filter \}\}
* 例子: \{\{ list_nums \| length \}\}
* 过滤器可以叠加\{\{ value \| filter1 \| filter2 \| ... \}\}

