import os
import cv2
path = "Images/"
images = []

for j in os.listdir(path):
    name, ext = os.path.splitext(j)
    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path + '/' + ext
        print(file_name)
        images.append(file_name)

count = len(images)
frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
print(size)

out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

for i in range(count,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("Done")