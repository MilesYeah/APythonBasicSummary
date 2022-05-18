# css selector :   **元素名[限制条件]**


| 定位器 Locator | 方法                           | By.               | 描述                      | 特点 |
| -------------- | ------------------------------ | ----------------- | ------------------------- | ---- |
| `css selector` | `find_element_by_css_selector` | `By.CSS_SELECTOR` | 定位 CSS 选择器匹配的元素 |      |
|                |                                |                   |                           |      |
|                |                                |                   |                           |      |



### 基础的CSS选择器
| 选择器               | 名字              | 例子       | 例子描述                                                   |
| -------------------- | ----------------- | ---------- | ---------------------------------------------------------- |
| 基础选择器           |                   |            |
| .class               | class选择器       | .intro     | 选择 class="intro" 的所有元素。                            |
| #id                  | id选择器          | #firstname | 选择 id="firstname" 的所有元素。                           |
| *                    | 通配符            |            | 选择所有元素。                                             |
| element              | 标签选择器        | p          | 选择所有 `<p>` 元素。                                        |
| 多层选择器           |                   |            |
| element,element      | 分组选择器        | div,p      | 同时选择所有 `<div>` 元素和所有 `<p>` 元素。                   |
| element element      | 后端选择器        | div p      | 选择 `<div>` 元素内部的所有 `<p>` 元素（包括子元素、孙子元素） |
| element>element      | 子元素选择器      | div>p      | 选择 `<div>` 元素下的 `<p>` 子元素。                           |
| element+element      | 相邻选择器        | div+p      | 选择 `<div>` 元素之后的所有兄弟 `<p>` 元素。                   |
| 属性选择器           |                   |            |
| `[attribute]`        | `[target]`        |            | 选择带有 target 属性所有元素。                             |
| `[attribute=value]`  | `[target=_blank]` |            | 选择 target="_blank" 的所有元素。                          |
| `[attribute~=value]` | `[title~=flower]` |            | 选择 title 属性包含单词 "flower" 的所有元素。              |
| `[attribute|=value]` | `[lang|=en]`      |            | 选择 lang 属性值以 "en" 开头的所有元素。                   |

### 伪类选择器
| 选择器               | 例子                  | 例子描述                                         |
| -------------------- | --------------------- | ------------------------------------------------ |
| :first-child         | p:first-child         | 选择属于父元素的第一个子元素的每个 `<p>` 元素。    |
| :nth-child(n)        | p:nth-child(2)        | 选择属于其父元素的第二个子元素的每个 `<p>` 元素。  |
| :nth-last-child(n)   | p:nth-last-child(2)   | 同上，从最后一个子元素开始计数。                 |
| :nth-of-type(n)      | p:nth-of-type(2)      | 选择属于其父元素第二个 `<p>` 元素的每个 `<p>` 元素。 |
| :nth-last-of-type(n) | p:nth-last-of-type(2) | 同上，但是从最后一个子元素开始计数。             |
| :last-child          | p:last-child          | 选择属于其父元素最后一个子元素每个 `<p>` 元素。    |





针对元素属性：   属性=属性值


| 选择器                 | 例子                    | 例子描述                                               |
| ---------------------- | ----------------------- | ------------------------------------------------------ |
| `.class`               | `.intro`                | 选择 class="intro" 的所有元素。                        |
| `.class1.class2`       | `.name1.name2`          | 选择 class 属性中同时有 name1 和 name2 的所有元素。    |
| `.class1 .class2`      | `.name1 .name2`         | 选择作为类名 name1 元素后代的所有类名 name2 元素。     |
| `#id`                  | `#firstname`            | 选择 id="firstname" 的元素。                           |
| `*`                    | `*`                     | 选择所有元素。                                         |
| `element`              | `p`                     | 选择所有 `<p>` 元素。                                  |
| `element.class`        | `p.intro`               | 选择 class="intro" 的所有 `<p>` 元素。                 |
| `element,element`      | `div, p`                | 选择所有 `<div>` 元素和所有 `<p>` 元素。               |
| `element element`      | `div p`                 | 选择 `<div>` 元素内的所有 `<p>` 元素。                 |
| `element>element`      | `div > p`               | 选择父元素是 `<div>` 的所有 `<p>` 元素。               |
| `element+element`      | `div + p`               | 选择紧跟 `<div>` 元素的首个 `<p>` 元素。               |
| `element1~element2`    | `p ~ ul`                | 选择前面有 `<p>` 元素的每个 `<ul>` 元素。              |
| `[attribute]`          | `[target]`              | 选择带有 target 属性的所有元素。                       |
| `[attribute=value]`    | `[target=_blank]`       | 选择带有 target="_blank" 属性的所有元素。              |
| `[attribute~=value]`   | `[title~=flower]`       | 选择 title 属性包含单词 "flower" 的所有元素。          |
| `[attribute|=value]`   | `[lang|=en]`            | 选择 lang 属性值以 "en" 开头的所有元素。               |
| `[attribute^=value]`   | `a[href^="https"]`      | 选择其 src 属性值以 "https" 开头的每个 `<a>` 元素。    |
| `[attribute$=value]`   | `a[href$=".pdf"]`       | 选择其 src 属性以 ".pdf" 结尾的所有 `<a>` 元素。       |
| `[attribute*=value]`   | `a[href*="w3schools"]`  | 选择其 href 属性值中包含 "abc" 子串的每个 `<a>` 元素。 |
| `:active`              | `a:active`              | 选择活动链接。                                         |
| `::after`              | `p::after`              | 在每个 `<p>` 的内容之后插入内容。                      |
| `::before`             | `p::before`             | 在每个 `<p>` 的内容之前插入内容。                      |
| `:checked`             | `input:checked`         | 选择每个被选中的 `<input>` 元素。                      |
| `:default`             | `input:default`         | 选择默认的 `<input>` 元素。                            |
| `:disabled`            | `input:disabled`        | 选择每个被禁用的 `<input>` 元素。                      |
| `:empty`               | `p:empty`               | 选择没有子元素的每个 `<p>` 元素（包括文本节点）。      |
| `:enabled`             | `input:enabled`         | 选择每个启用的 `<input>` 元素。                        |
| `:first-child`         | `p:first-child`         | 选择属于父元素的第一个子元素的每个 `<p>` 元素。        |
| `::first-letter`       | `p::first-letter`       | 选择每个 `<p>` 元素的首字母。                          |
| `::first-line`         | `p::first-line`         | 选择每个 `<p>` 元素的首行。                            |
| `:first-of-type`       | `p:first-of-type`       | 选择属于其父元素的首个 `<p>` 元素的每个 `<p>` 元素。   |
| `:focus`               | `input:focus`           | 选择获得焦点的 input 元素。                            |
| `:fullscreen`          | `:fullscreen`           | 选择处于全屏模式的元素。                               |
| `:hover`               | `a:hover`               | 选择鼠标指针位于其上的链接。                           |
| `:in-range`            | `input:in-range`        | 选择其值在指定范围内的 input 元素。                    |
| `:indeterminate`       | `input:indeterminate`   | 选择处于不确定状态的 input 元素。                      |
| `:invalid`             | `input:invalid`         | 选择具有无效值的所有 input 元素。                      |
| `:lang(language)`      | `p:lang(it)`            | 选择 lang 属性等于 "it"（意大利）的每个 `<p>` 元素。   |
| `:last-child`          | `p:last-child`          | 选择属于其父元素最后一个子元素每个 `<p>` 元素。        |
| `:last-of-type`        | `p:last-of-type`        | 选择属于其父元素的最后 `<p>` 元素的每个 `<p>` 元素。   |
| `:link`                | `a:link`                | 选择所有未访问过的链接。                               |
| `:not(selector)`       | `:not(p)`               | 选择非 `<p>` 元素的每个元素。                          |
| `:nth-child(n)`        | `p:nth-child(2)`        | 选择属于其父元素的第二个子元素的每个 `<p>` 元素。      |
| `:nth-last-child(n)`   | `p:nth-last-child(2)`   | 同上，从最后一个子元素开始计数。                       |
| `:nth-of-type(n)`      | `p:nth-of-type(2)`      | 选择属于其父元素第二个 `<p>` 元素的每个 `<p>` 元素。   |
| `:nth-last-of-type(n)` | `p:nth-last-of-type(2)` | 同上，但是从最后一个子元素开始计数。                   |
| `:only-of-type`        | `p:only-of-type`        | 选择属于其父元素唯一的 `<p>` 元素的每个 `<p>` 元素。   |
| `:only-child`          | `p:only-child`          | 选择属于其父元素的唯一子元素的每个 `<p>` 元素。        |
| `:optional`            | `input:optional`        | 选择不带 "required" 属性的 input 元素。                |
| `:out-of-range`        | `input:out-of-range`    | 选择值超出指定范围的 input 元素。                      |
| `::placeholder`        | `input::placeholder`    | 选择已规定 "placeholder" 属性的 input 元素。           |
| `:read-only`           | `input:read-only`       | 选择已规定 "readonly" 属性的 input 元素。              |
| `:read-write`          | `input:read-write`      | 选择未规定 "readonly" 属性的 input 元素。              |
| `:required`            | `input:required`        | 选择已规定 "required" 属性的 input 元素。              |
| `:root`                | `:root`                 | 选择文档的根元素。                                     |
| `::selection`          | `::selection`           | 选择用户已选取的元素部分。                             |
| `:target`              | `#news:target`          | 选择当前活动的 #news 元素。                            |
| `:valid`               | `input:valid`           | 选择带有有效值的所有 input 元素。                      |
| `:visited`             | `a:visited`             | 选择所有已访问的链接。                                 |




## cssSelector
`元素名[限制条件]`
`限制条件：属性='属性值''multi-chosen']`
`a[data-city='全国']`


## 通过元素的id属性值来进行定位：
`#id属性值`


## 多个限制条件：
`a[data-id='749'][class='hot-city-name']`


### 子元素 和 后代元素

#### `元素1 > 元素2`
如果 元素2 是 元素1 的 直接子元素， CSS Selector 选择子元素的语法是这样的

中间用一个大于号 （我们可以理解为箭头号）

注意，最终选择的元素是 元素2， 并且要求这个 元素2 是 元素1 的直接子元素


#### `元素1 > 元素2 > 元素3 > 元素4`

也支持更多层级的选择， 比如

就是选择 元素1 里面的子元素 元素2 里面的子元素 元素3 里面的子元素 元素4 ， 最终选择的元素是 元素4


#### `元素1   元素2`

如果 元素2 是 元素1 的 后代元素， CSS Selector 选择后代元素的语法是这样的

中间是一个或者多个空格隔开

最终选择的元素是 元素2 ， 并且要求这个 元素2 是 元素1 的后代元素。

#### `元素1   元素2   元素3  元素4`

也支持更多层级的选择， 比如

最终选择的元素是 元素4






### 根据属性选择




### 组选择

如果我们要 同时选择所有class 为 plant 和 class 为 animal 的元素。怎么办？

这种情况，css选择器可以 使用 逗号 ，称之为 组选择 ，像这样
```
.plant , .animal
```
再比如，我们要同时选择所有tag名为div的元素 和 id为BYHY的元素，就可以像这样写
```
div,#BYHY
```

对应的selenium代码如下
```py
elements = wd.find_elements_by_css_selector('div,#BYHY')
for element in elements:
    print(element.text)
```



### 按次序选择子节点
```html
<body>  
       <div id='t1'>
           <h3> 唐诗 </h3>
           <span>李白</span>
           <p>静夜思</p>
           <span>杜甫</span>
           <p>春夜喜雨</p>              
       </div>      
        
       <div id='t2'>
           <h3> 宋词 </h3>
           <span>苏轼</span>
           <p>赤壁怀古</p>
           <p>明月几时有</p>
           <p>江城子·乙卯正月二十日夜记梦</p>
           <p>蝶恋花·春景</p>
           <span>辛弃疾</span>
           <p>京口北固亭怀古</p>
           <p>青玉案·元夕</p>
           <p>西江月·夜行黄沙道中</p>
       </div>             

</body>
```

#### 父元素的第n个子节点
我们可以指定选择的元素 是父元素的第几个子节点

使用 nth-child

比如，

我们要选择 唐诗 和宋词 的第一个 作者，

也就是说 选择的是 第2个子元素，并且是span类型

所以这样可以这样写 span:nth-child(2) ，


如果你不加节点类型限制，直接这样写 :nth-child(2)

就是选择所有位置为第2个的所有元素，不管是什么类型

#### 父元素的倒数第n个子节点

也可以反过来， 选择的是父元素的 倒数第几个子节点 ，使用 nth-last-child

比如：
```
p:nth-last-child(1)
```
就是选择第倒数第1个子元素，并且是p元素



#### 父元素的第几个某类型的子节点

我们可以指定选择的元素 是父元素的第几个 某类型的 子节点

使用 nth-of-type

比如，

我们要选择 唐诗 和宋词 的第一个 作者，

可以像上面那样思考：选择的是 第2个子元素，并且是span类型

所以这样可以这样写 span:nth-child(2) ，


还可以这样思考，选择的是 第1个span类型 的子元素

所以也可以这样写 span:nth-of-type(1)


#### 父元素的倒数第几个某类型的子节点

当然也可以反过来， 选择父元素的 倒数第几个某类型 的子节点

使用 nth-last-of-type

像这样

p:nth-last-of-type(2)



#### 奇数节点和偶数节点

如果要选择的是父元素的 偶数节点，使用 nth-child(even)

比如

p:nth-child(even)
如果要选择的是父元素的 奇数节点，使用 nth-child(odd)

p:nth-child(odd)

如果要选择的是父元素的 某类型偶数节点，使用 nth-of-type(even)

如果要选择的是父元素的 某类型奇数节点，使用 nth-of-type(odd)



### 兄弟节点选择


#### 相邻兄弟节点选择

上面的例子里面，我们要选择 唐诗 和宋词 的第一个 作者

还有一种思考方法，就是选择 h3 后面紧跟着的兄弟节点 span。

这就是一种 相邻兄弟 关系，可以这样写 h3 + span

表示元素 紧跟关系的 是 加号


#### 后续所有兄弟节点选择

如果要选择是 选择 h3 后面所有的兄弟节点 span，可以这样写 h3 ~ span






## ref
* [css表达式-下篇](http://www.byhy.net/tut/auto/selenium/css_2/)
* [CSS 选择器参考手册](https://www.w3school.com.cn/cssref/css_selectors.asp)
* []()
* []()
* []()
* []()
* []()
* []()
