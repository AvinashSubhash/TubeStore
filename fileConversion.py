
def binaryToFile(cache):
    filename = cache[0]
    binary_string = cache[1]
    byte_array = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = int(binary_string[i:i+8], 2)
        byte_array.append(byte)
    LATTE = byte_array
    #print(byte_array)
    with open(filename,'wb') as file:
        file.write(byte_array)

def fileToBinary(filename):
    ext = filename.split(".")[-1]
    with open(str(filename),'rb') as f:
        contents = f.read()
        binary = ''.join(format(byte,'08b') for byte in contents)
        #binaryToFile("final_output.pdf",binary)   
        
        
    return [binary,ext]


