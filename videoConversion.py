import cv2
import numpy as np
INITIAL=6123128
def binaryToVideo(binary_data):
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
    
    out = cv2.VideoWriter('output.mp4',fourcc,fps,(width,height))

    for i in range(frames):
        img = np.zeros((frame_size[0], frame_size[1], 3), dtype=np.uint8)
        img[array[i] == 1] = [255, 255, 255]
        out.write(img)
    out.release()


def videoToBinary(video_path):
    binary_data = []
    cap = cv2.VideoCapture("output.mp4")
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
    binary_data = binary_data[:INITIAL]
    #print(array[:10],binary_data[:10])
    res = ''.join(str(i) for i in binary_data)
    cap.release()
    return res