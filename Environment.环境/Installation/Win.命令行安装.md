# Win.命令行安装

* [官方文档](https://docs.python.org/3.8/using/windows.html)


To completely hide the installer UI and install Python silently, pass the `/quiet` option. 
To skip past the user interaction but still display progress and errors, pass the `/passive` option. 
The `/uninstall` option may be passed to immediately begin removing Python - no prompt will be displayed.

```bat
python-3.8.0.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
python-3.8.0.exe InstallAllUsers=0 Include_launcher=0 Include_test=0 SimpleInstall=1 SimpleInstallDescription="Just for me, no test suite."
```


Setup Help Visit docs. python.org/3.8/using/windows, html for the full list of options, including the ability to enable and disable specific features.
* "`/passive`" to display progress without requiring user interaction
* "`/quiet`" to install/uninstall without displaying any Ul
* "`/simple`" to prevent user customization
* "`/uninstall`" to remove Python (without confirmation)
* "`layout [directory]`" to pre-download all components
* "`log [filename]`" to specify log files location

