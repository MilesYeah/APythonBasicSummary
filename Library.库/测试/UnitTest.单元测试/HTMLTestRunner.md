# HTMLTestRunner



| method                | explaination |
| --------------------- | ------------ |
| generateReport        |              |
| getReportAttributes   |              |
| run                   |              |
| sortResult            |              |
| _generate_ending      |              |
| _generate_heading     |              |
| _generate_report      |              |
| _generate_report_test |              |
| _generate_stylesheet  |              |
|                       |              |


```py
import os

import unittest
from t_unittest_simple import tUnittestSimple

from HTMLTestRunner import HTMLTestRunner

report_name = 'report name'
report_title = "report title"
report_desc = 'report description'
report_fn = f'report.html'


suit = unittest.TestSuite()
suit.addTest(tUnittestSimple("test_1"))
suit.addTest(tUnittestSimple("test_2"))

with open(report_fn, 'w') as report:
    runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=report_title,
                                           description=report_desc)
    runner.run(suit)
```


```
from HTMLTestRunner import HTMLTestRunner
dir(HTMLTestRunner)
>>> ['HTMLTestRunner', 'OutputRedirector', 'StringIO', 'Template_mixin', 'TestProgram', 'TestResult', '_TestResult', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'datetime', 'main', 'saxutils', 'stderr_redirector', 'stdout_redirector', 'sys', 'time', 'unittest']
dir(HTMLTestRunner.HTMLTestRunner)
>>> ['DEFAULT_DESCRIPTION', 'DEFAULT_TITLE', 'ENDING_TMPL', 'HEADING_ATTRIBUTE_TMPL', 'HEADING_TMPL', 'HTML_TMPL', 'REPORT_CLASS_TMPL', 'REPORT_TEST_NO_OUTPUT_TMPL', 'REPORT_TEST_OUTPUT_TMPL', 'REPORT_TEST_WITH_OUTPUT_TMPL', 'REPORT_TMPL', 'STATUS', 'STYLESHEET_TMPL', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_generate_ending', '_generate_heading', '_generate_report', '_generate_report_test', '_generate_stylesheet', 'generateReport', 'getReportAttributes', 'run', 'sortResult']
```
