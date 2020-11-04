# os.system

执行一条命令，命令的 stdout 直接输出到屏幕，返回命令退出的返回值。

```py
>>> a = os.system("dir")
 Volume in drive F is Miles
 Volume Serial Number is 0DC0-1467
 Directory of F:\PyDev
08/29/2020  09:49 AM    <DIR>          .
08/29/2020  09:49 AM    <DIR>          ..
08/29/2020  11:19 AM    <DIR>          .idea
08/20/2020  03:03 PM    <DIR>          .vscode
08/28/2020  02:13 PM    <DIR>          base_base
08/09/2020  10:17 AM    <DIR>          base_database
08/26/2020  09:44 AM    <DIR>          base_pandas
06/10/2020  01:55 PM    <DIR>          conf
08/28/2020  05:22 PM    <DIR>          lib_requirements
08/28/2020  05:23 PM    <DIR>          MiTACRMKThermalTest
06/24/2020  01:38 PM    <DIR>          py_mitac_sfcs
08/18/2020  05:20 PM    <DIR>          py_redfish
06/10/2020  02:46 PM                69 root
               1 File(s)             69 bytes
              12 Dir(s)  349,462,900,736 bytes free
>>> a
0
```