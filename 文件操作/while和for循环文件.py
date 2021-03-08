#for
# with open(r"t和b模式的区别.txt",mode="rb") as f1:
#     for line in f1:
#         print(line)

#while，当文件一行文件内容过长时，可以使用这种方式循环

# with open(r"t和b模式的区别.txt",mode="rb") as f2:
#     while True:
#         res = f2.read(10)  #每次度10个字节
#         if not res:
#             break
#         print(res)


#读取mp4文件
# with open(r"xinnian.mp4",mode="rb") as f3, \
#         open(r"new-xinnian.mp4",mode="wb") as f4:
#     while True:
#         res = f3.read(1024)
#         if not  res:
#             break
#         # print(res)
#         f4.write(res)
import cv2

# 获得视频的格式
videoCapture = cv2.VideoCapture(r'F:\lvsir\老男孩儿kvm\01-kvm虚拟化实战_rec.mp4')

# 获得码率及尺寸
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fNUMS = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)

# 读帧
success, frame = videoCapture.read()
while success:
    cv2.imshow('windows', frame)  # 显示
    cv2.waitKey(int(1000 / int(fps)))  # 延迟
    success, frame = videoCapture.read()  # 获取下一帧

videoCapture.release()















