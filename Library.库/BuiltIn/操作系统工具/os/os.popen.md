
# os.popen



```py
import os
r = os.popen('dir')
r
<os._wrap_close object at 0x000001D30F1A0688>
for i in r:
...     print(i)
...     
 Volume in drive F is Miles
 Volume Serial Number is 0DC0-1467
 Directory of F:\Project\Intel.RMK\Intel.RMK.Tests\PyRedfishBFT
05/28/2020  04:35 PM    <DIR>          .
05/28/2020  04:35 PM    <DIR>          ..
05/21/2020  08:57 PM             1,064 .gitignore
06/01/2020  09:28 AM    <DIR>          .idea
05/22/2020  08:27 AM    <DIR>          .vscode
05/29/2020  03:28 PM    <DIR>          base_libs
05/22/2020  08:54 AM    <DIR>          configs
05/21/2020  03:29 PM               418 package_requirements.md
05/29/2020  03:04 PM    <DIR>          redfish_bft
05/29/2020  11:31 AM    <DIR>          samples
05/22/2020  10:13 AM    <DIR>          tool_redfish
05/21/2020  11:18 AM    <DIR>          venv
               2 File(s)          1,482 bytes
              10 Dir(s)  389,062,213,632 bytes free

```


