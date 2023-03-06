import cv2
import numpy as np

def binaryToVideo(binary_data):
    array = np.array(list(binary_data)).astype(np.uint8)
    size = len(binary_data)
    frame_size = (128,128)
    frames = int(np.ceil(size/(frame_size[0]*frame_size[1])))
    difference = int(frames*128*128 - size)
    additional = np.zeros(difference,)
    array = np.append(array,additional)
    print(frames)
    while frames%3!=0:
        frames+=1
        array = array.append(array,np.zeros(frame_size[0]*frame_size[1]))
    print(frames)
    array = array.reshape(frames,frame_size[0],frame_size[1])*255
    print(array.shape)
    array = array.astype(np.uint8)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 30
    width = frame_size[0]
    height = frame_size[1]
    
    out = cv2.VideoWriter('output.mp4',fourcc,fps,(width,height))

    for i in range(0,frames,3):
        image = cv2.merge((array[i,:,:],array[i+1,:,:],array[i+2,:,:]))
        out.write(image)
    out.release()


def videoToBinary(video_path):
    binary_data = bytearray()
    cap = cv2.VideoCapture("output.mp4")
    while True:
        ret,frame = cap.read()
        #print(ret,frame)
        if not ret:
            break
        print((frame[:,:,0]/255).astype(int))
        #binary_data.extend([frame[0,0,0],[frame[0,0,1],[frame[0,0,2]])
    cap.release()
    return binary_data