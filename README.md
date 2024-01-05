# MangaAIRepairerBackend   

本程序需要搭配前台脚本使用。[脚本地址](https://greasyfork.org/zh-CN/scripts/483769-%E6%BC%AB%E7%94%BB%E7%BD%91%E7%AB%99%E7%94%BB%E8%B4%A8ai%E4%BF%AE%E5%A4%8D)   
漫画网站的画质AI高清修复，基于Real-ESRGAN实现。暂时只支持漫画柜   
下载解压后运行安装bat脚本。


## 以下供开发者阅读：项目如何运行  
### 先决条件
python 版本大于3.11，小于3.13  
pipx    
poetry   


克隆本仓库后首先在项目根目录下运行：
```
python -m venv venv
.\venv\scripts\activate
poetry install
```