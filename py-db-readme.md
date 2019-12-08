# pymssql连接sqlserver数据库

python3.6连接sqlserver数据库需要引入pymssql模块

pymssql官方:https://pypi.org/project/pymssql/

没有安装的话需要:

pip安装:

pip install pymssql

> 如果安装有python2/python3 两个版本，通过如下来区分pip的安装

```
python2 -m pip install XXX

python3 -m pip install XXX

```


# pip3改镜像地址

参考：
https://blog.csdn.net/u012592062/article/details/51966649

用pip安装依赖包时默认访问https://pypi.python.org/simple/，但是经常出现不稳定以及访问速度非常慢的情况，国内厂商提供的pipy镜像目前可用的有：

其中，比较常用的国内镜像包括：

1. 阿里云 http://mirrors.aliyun.com/pypi/simple/
2. 豆瓣http://pypi.douban.com/simple/
3. 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
4. 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
5. 华中科技大学http://pypi.hustunique.com/

有两种方式使用我们自己指定的镜像源，第一种是手动指定



## 手动改镜像地址

```

python3 -m pip install 包名 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

```

## 增加配置文件

- 在用户根目录下新建目录

```
mkdir .pip
```
- 在目录下新建文件 pip.conf ,并在文件中写入如下内容

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn
```

- 修改
```
yangxiying@wgr:~$ mkdir .pip3
yangxiying@wgr:~$ cd .pip3/
yangxiying@wgr:~/.pip3$ vim pip3.conf
```

