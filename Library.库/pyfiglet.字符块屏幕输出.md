# pyfiglet.字符块屏幕输出


## 安装
需要有Python3环境，一般RedHat8系列都自带Python3.

```sh
[root@localhost ~]# pip3 install pyfiglet
WARNING: Running pip install with root privileges is generally not a good idea. Try `pip3 install --user` instead.
Collecting pyfiglet
  Downloading https://files.pythonhosted.org/packages/33/07/fcfdd7a2872f5b348953de35acce1544dab0c1e8368dca54279b1cde5c15/pyfiglet-0.8.post1-py2.py3-none-any.whl (865kB)
    100% |████████████████████████████████| 870kB 1.3MB/s 
Installing collected packages: pyfiglet
Successfully installed pyfiglet-0.8.post1
[root@localhost ~]# 
```

```
# 未联网情况下
pip3 install pyfiglet-*.whl
# 安装包可以从 NTP System Board BFT package 下的Utilities找到
# 或者是从 https://pypi.org/project/pyfiglet/#files 下载
```


## 使用


```sh
[root@localhost ~]# pyfiglet -f pebbles "Swap NVME"
.oOOOo.                              o.     O o      'O Oo      oO o.OOoOoo 
o     o                              Oo     o O       o O O    o o  O       
O.                                   O O    O o       O o  o  O  O  o       
 `OOoo.                              O  o   o o       o O   Oo   O  ooOO    
      `O 'o     O .oOoO' .oOo.       O   o  O O      O' O        o  O       
       o  O  o  o O   o  O   o       o    O O `o    o   o        O  o       
O.    .O  o  O  O o   O  o   O       o     Oo  `o  O    o        O  O       
 `oooO'   `Oo'oO' `OoO'o oOoO'       O     `o   `o'     O        o ooOooOoO 
                         O                                                  
                         o'                                                 

[root@localhost ~]# pyfiglet -f roman "Swap NVME"
 .oooooo..o                                       
d8P'    `Y8                                       
Y88bo.      oooo oooo    ooo  .oooo.   oo.ooooo.  
 `"Y8888o.   `88. `88.  .8'  `P  )88b   888' `88b 
     `"Y88b   `88..]88..8'    .oP"888   888   888 
oo     .d8P    `888'`888'    d8(  888   888   888 
8""88888P'      `8'  `8'     `Y888""8o  888bod8P' 
                                        888       
                                       o888o      
                                                  
ooooo      ooo oooooo     oooo ooo        ooooo oooooooooooo 
`888b.     `8'  `888.     .8'  `88.       .888' `888'     `8 
 8 `88b.    8    `888.   .8'    888b     d'888   888         
 8   `88b.  8     `888. .8'     8 Y88. .P  888   888oooo8    
 8     `88b.8      `888.8'      8  `888'   888   888    "    
 8       `888       `888'       8    Y     888   888       o 
o8o        `8        `8'       o8o        o888o o888ooooood8 
                                                             
                                                             
                                                             

[root@localhost ~]# 
[root@localhost ~]# pyfiglet -f small "Swap NVME"
 ___                    _  ___   ____  __ ___ 
/ __|_ __ ____ _ _ __  | \| \ \ / /  \/  | __|
\__ \ V  V / _` | '_ \ | .` |\ V /| |\/| | _| 
|___/\_/\_/\__,_| .__/ |_|\_| \_/ |_|  |_|___|
                |_|                           

[root@localhost ~]# 
[root@localhost ~]# pyfiglet -f standard  "Swap NVME"
 ____                       _   ___     ____  __ _____ 
/ ___|_      ____ _ _ __   | \ | \ \   / /  \/  | ____|
\___ \ \ /\ / / _` | '_ \  |  \| |\ \ / /| |\/| |  _|  
 ___) \ V  V / (_| | |_) | | |\  | \ V / | |  | | |___ 
|____/ \_/\_/ \__,_| .__/  |_| \_|  \_/  |_|  |_|_____|
                   |_|                                 

[root@localhost ~]# 
[root@localhost ~]# pyfiglet -f starwars  "Swap NVME"
     _______.____    __    ____  ___      .______   
    /       |\   \  /  \  /   / /   \     |   _  \  
   |   (----` \   \/    \/   / /  ^  \    |  |_)  | 
    \   \      \            / /  /_\  \   |   ___/  
.----)   |      \    /\    / /  _____  \  |  |      
|_______/        \__/  \__/ /__/     \__\ | _|      
                                                    
.__   __. ____    ____ .___  ___.  _______ 
|  \ |  | \   \  /   / |   \/   | |   ____|
|   \|  |  \   \/   /  |  \  /  | |  |__   
|  . `  |   \      /   |  |\/|  | |   __|  
|  |\   |    \    /    |  |  |  | |  |____ 
|__| \__|     \__/     |__|  |__| |_______|
                                           

[root@localhost ~]# 
[root@localhost ~]# pyfiglet -f univers  "Swap NVME"
                                                       
 ad88888ba                                             
d8"     "8b                                            
Y8,                                                    
`Y8aaaaa,   8b      db      d8 ,adPPYYba, 8b,dPPYba,   
  `"""""8b, `8b    d88b    d8' ""     `Y8 88P'    "8a  
        `8b  `8b  d8'`8b  d8'  ,adPPPPP88 88       d8  
Y8a     a8P   `8bd8'  `8bd8'   88,    ,88 88b,   ,a8"  
 "Y88888P"      YP      YP     `"8bbdP"Y8 88`YbbdP"'   
                                          88           
                                          88           
                                                            
888b      88 8b           d8 88b           d88 88888888888  
8888b     88 `8b         d8' 888b         d888 88           
88 `8b    88  `8b       d8'  88`8b       d8'88 88           
88  `8b   88   `8b     d8'   88 `8b     d8' 88 88aaaaa      
88   `8b  88    `8b   d8'    88  `8b   d8'  88 88"""""      
88    `8b 88     `8b d8'     88   `8b d8'   88 88           
88     `8888      `888'      88    `888'    88 88           
88      `888       `8'       88     `8'     88 88888888888  
                                                            
                                                            

[root@localhost ~]# 
```



## ref
* [home](http://www.figlet.org/)
* [font examples](http://www.figlet.org/examples.html)
* []()
* []()
* []()
* []()




