from PIL import Image

bitstring="0000000111110111110000000011111010101010101011111001000101111100100101000100100010100010111110100010010001011011110011010001001111101001001111101111100000000101010101010000000111111100110110100111111100000101110111011110101011001001110101011111101111101111000011001011011110000011010100011111101110100111100101101111110001110010101110100000000010111001101001010110000010111010110101111001011100111100011000000010110011000111011111110100110111011001010000000100011101010100110011111011111101001110110101000101010111010000011100100010100100101101001010010001010110011101010011001111101000110001100100110000000100100100000010110"

outimg= Image.new("RGB",(25,25),"black")
pixels_out = outimg.load()

count=-1
for i in range(0,25):
    for j in range (0,25):
        count+=1
        if bitstring[count]=="1":
            pixels_out[(j,i)]=(255,255,255)

 
outimg=outimg.resize((100,100))
outimg.save("qrout.png","png")
