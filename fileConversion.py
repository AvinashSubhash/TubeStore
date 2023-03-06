def fileNameToBinary(fileName):
    binary = ''.join(format(ord(char),'08b') for char in fileName)
    return binary
    #return [binary,binaryToFilename(binary)]

def binaryToFilename(binary):
    bytes_list = [int(binary[i:i+8], 2) for i in range(0, len(binary), 8)]
    string = ''.join([chr(byte) for byte in bytes_list])
    return string

def fileToBinary(filename):
    with open(str(filename),'rb') as f:
        contents = f.read()
        binary = ''.join(format(byte,'08b') for byte in contents)
        #binaryToFilename("result.txt",binary)   
        #print("File to binary: ",binary) 
    return binary

def binaryToFilename(filename,binary_string):
        bytes_list = [int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8)]
        binary = bytes(bytes_list)
        with open(filename,'wb') as file:
            file.write(binary)

import videoConversion as vc

vc.binaryToVideo(fileToBinary("solidity.pdf"))
print("Video to binary: ",vc.videoToBinary("binary_video.mp4"))


