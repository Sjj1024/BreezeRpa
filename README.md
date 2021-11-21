# BreezeRpa
使用自动注入基础框架搭建Rpa流程

里面有一个小Demo，用于生成soul的匹配度的，哈哈哈
![](https://github.com/Sjj1024/BreezeRpa/blob/main/Picture/951636101615.jpg?raw=true)

先安装依赖吧:
https://pypi.tuna.tsinghua.edu.cn/simple/ 清华
http://pypi.doubanio.com/simple/ 豆瓣
http://mirrors.aliyun.com/pypi/simple/ 阿里
https://pypi.mirrors.ustc.edu.cn/simple/ 中国科学技术大学
http://mirrors.163.com/pypi/simple/ 网易

```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

忽略错误安装依赖方式:
```
cat requirement_s.txt | xargs -n 1 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/
```