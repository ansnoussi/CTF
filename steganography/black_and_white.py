#!/usr/bin/env python

#if an image is made of black and white pixels, convert it to bitstring
from PIL import Image

img = Image.open('baconian.bmp').convert('RGB')
pixels_orig = img.load()

(w,h)=img.size

s=[]
for j in range(0,w):
    for i in range(0,h):    
      (r,g,b) = pixels_orig[j,i]
      s.append(str(r&1))

print ''.join(s)
