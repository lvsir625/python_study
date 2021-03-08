
#参考：https://blog.csdn.net/a649344475/article/details/80864600
import base64
with open(r"F:\img\a\kb.jpg", mode="rb") as f1, \
        open(r"F:/img/b/kb.jpg", mode="wb") as f2:
    b6 = base64.b64encode(f1.read())
    f2.write(base64.b64decode(b6))