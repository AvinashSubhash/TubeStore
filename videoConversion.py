import cv2
import numpy as np
def binaryToVideo(cache,path):
    binary_data = cache[0]
    ext = cache[1]
    filename = path.split("/")[-1].split(".")[-2]
    array = np.array(list(binary_data)).astype(np.uint8)
    res_array = array
    size = len(binary_data)
    print("Initial size :",size)
    frame_size = (128,128)
    frames = int(np.ceil(size/(frame_size[0]*frame_size[1])))
    difference = int(frames*128*128 - size)
    print("Difference: ",difference)
    additional = np.zeros(difference,)
    array = np.append(array,additional)
    array = array.reshape(frames,frame_size[0],frame_size[1])
    print("Array shape: ",array.shape)
    array = array.astype(np.uint8)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 30
    width = frame_size[0]
    height = frame_size[1]
    print(str(filename)+"-Video-"+str(difference)+"-"+str(ext)+".mp4")
    out = cv2.VideoWriter(str(filename)+"-Video-"+str(difference)+"-"+str(ext)+".mp4",fourcc,fps,(width,height))

    for i in range(frames):
        img = np.zeros((frame_size[0], frame_size[1], 3), dtype=np.uint8)
        img[array[i] == 1] = [255, 255, 255]
        out.write(img)
    out.release()
    return [difference,ext]


def videoToBinary(video_path):
    [ext,difference] = [video_path.split(".")[0].split("-")[-1],video_path.split(".")[0].split("-")[-2]]
    binary_data = []
    filename = video_path.split(".")[0]
    cap = cv2.VideoCapture(video_path)
    while True:
        ret,frame = cap.read()
        #print(ret,frame)
        if not ret:
            break
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        ret,frame = cv2.threshold(frame, 127, 1, cv2.THRESH_BINARY)
        data = frame.astype(np.uint8).tolist()
        for i in data:
            binary_data.extend(i)
    print("Length of binary data recovered: ",len(binary_data))
    binary_data = binary_data[:0-int(difference)]
    #print(array[:10],binary_data[:10])
    res = ''.join(str(i) for i in binary_data)
    cap.release()
    return [filename+"."+ext,res]