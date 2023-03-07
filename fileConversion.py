INITIAL_DATA = 0
def binaryToFile(filename,binary_string):
    byte_array = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = int(binary_string[i:i+8], 2)
        byte_array.append(byte)
    LATTE = byte_array
    #print(byte_array)
    with open(filename,'wb') as file:
        file.write(byte_array)

def fileToBinary(filename):
    with open(str(filename),'rb') as f:
        contents = f.read()
        binary = ''.join(format(byte,'08b') for byte in contents)
        INITIAL_DATA = binary
        #binaryToFile("final_output.pdf",binary)   
        
    return binary

import videoConversion as vc
vc.binaryToVideo(fileToBinary("Codechef-problems.zip"))
#print("Video to binary: ",vc.videoToBinary("binary_video.mp4"))
binary = vc.videoToBinary("Codechef-problems.mp4")
#_ = binaryToFile("out.zip",binary)

