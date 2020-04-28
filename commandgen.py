#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image
from PIL import GifImagePlugin
import numpy as np 
import os, os.path
import io

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

MODE = 3
DEBUG = 0
file1 = open("output.txt", "w", encoding="utf-8").close()
myFile = open("output.txt", "w", encoding="utf-8")
#/tellraw @a ["",{"text":"\u2588","color":"#fffffff"}, etc
if MODE == 0: 
    
    x = 'soultest.png'
    im = Image.open(x).convert("RGBA")
    pix = np.asarray(im)
    print(im)
    imHeight = len(pix) 
    imWidth = len(pix[0])
       
    if DEBUG == 1:
        print(im.size)
        print(imWidth)
        print(imHeight)

    s = '/tellraw @a [\"\",'
    for i in range(0, imHeight):
        for j in range(0, imWidth):
            r = pix[i,j][0]
            g = pix[i,j][1]
            b = pix[i,j][2]
            a = pix[i,j][3]
            hex = rgb2hex(r, g, b)
            if DEBUG == 1:
                print("Pixel value: (%d, %d)\n" %(i, j))
                print('RGBA for i = %d, j = %d: (%d, %d, %d, %d), hex = %s' %(i, j, r, g, b, a, hex))

            
            s += '{\"text\":\"'
            if a <= 255/2:
                block = "▒"
            else:
                block = "█" 
            s += block
            s += '\",\"color\":\"'   
            s += hex
            if i == (imHeight - 1) and j == (imWidth - 1):
                s += '\"}]'
            else:   
                s += '\"},'
        if i < imHeight - 1:
            s += '{\"text\":\"\\n\"},'
    print(s)
    myFile.write(s)
    im.save(x)
elif MODE == 1:

    imf = Image.open('soultest2.gif')
    if DEBUG == 1:
        print(imf.is_animated)
        print(imf.n_frames)

    for frame in range(0, imf.n_frames):
        imf.seek(frame)
        imf.save('temp__1.png')

        im = Image.open('temp__1.png').convert("RGBA")
        
        pix = np.asarray(im)

        imHeight = len(pix) 
        imWidth = len(pix[0])
       
        if DEBUG == 1:
            print(im.size)
            print(imWidth)
            print(imHeight)

        s = '/tellraw @a [\"\",'
        for i in range(0, imHeight):
            for j in range(0, imWidth):

                r = pix[i,j][0]
                g = pix[i,j][1]
                b = pix[i,j][2]
                a = pix[i,j][3]
                if DEBUG == 1:
                    print("Pixel value: (%d, %d)\n" %(i, j))
                    print('RGBA for i = %d, j = %d: (%d, %d, %d, %d), hex = %s' % (i, j, r, g, b, a, hex))

                hex = rgb2hex(r, g, b)
                s += '{\"text\":\"'
                if a <= 255/2:
                    block = "▒"
                else:
                    block = "█" 
                s += block
                s += '\",\"color\":\"'   
                s += hex
                if i == (imHeight - 1) and j == (imWidth - 1):
                    s += '\"}]'
                else:   
                    s += '\"},'
            if i < imHeight - 1:
                s += '{\"text\":\"\\n\"},'
        print(s)
        myFile.write(s)
        myFile.write("\n\n")
        os.remove('temp__1.png')

# ANIMATION WITH ALPHA: (ex: filename0000.png, filename0001.png, filename0003.png)
elif MODE == 2:

    gifName = "souls-animation"
    #imf = Image.open("Soul-Animation%04d",frame)
    if DEBUG == 1:
        path = 'frames'
        num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
        print(num_files)
    for frame in range(0, num_files):

        frameName = "frames/%s%04d.png" % (gifName, frame)
        im = Image.open(frameName).convert("RGBA")
        
        pix = np.asarray(im)

        imHeight = len(pix) 
        imWidth = len(pix[0])
       
        if DEBUG == 1:
            print(im.size)
            print(imWidth)
            print(imHeight)

        s = '/tellraw @a [\"\",'
        for i in range(0, imHeight):
            for j in range(0, imWidth):

                r = pix[i,j][0]
                g = pix[i,j][1]
                b = pix[i,j][2]
                a = pix[i,j][3]
                if DEBUG == 1:
                    print("Pixel value: (%d, %d)\n" %(i, j))
                    print('RGBA for i = %d, j = %d: (%d, %d, %d, %d), hex = %s' % (i, j, r, g, b, a, hex))

                hex = rgb2hex(r, g, b)
                s += '{\"text\":\"'
                if a <= 255/2:
                    block = "▒"
                else:
                    block = "█" 
                s += block
                s += '\",\"color\":\"'   
                s += hex
                if i == (imHeight - 1) and j == (imWidth - 1):
                    s += '\"}]'
                else:   
                    s += '\"},'
            if i < imHeight - 1:
                s += '{\"text\":\"\\n\"},'
        print(s)
        myFile.write(s)
        myFile.write("\n\n")

elif MODE == 3: #sicko mode - compress gif to height of 20
    gifName = "test_gif_sicko.gif"
    imf = Image.open(gifName)
    if DEBUG == 1:
        print(imf.is_animated)
        print(imf.n_frames)

    for frame in range(0, imf.n_frames):
        imf.seek(frame)

        imf.save('temp__1.png')

        im = Image.open('temp__1.png').convert("RGBA")
        im.thumbnail((35, 20), Image.ANTIALIAS)
        #print(im.size)

        pix = np.asarray(im)

        imHeight = len(pix) 
        imWidth = len(pix[0])
       
        if DEBUG == 1:
            print(im.size)
            print(imWidth)
            print(imHeight)

        s = '/tellraw @a [\"\",'
        for i in range(0, imHeight):
            for j in range(0, imWidth):

                r = pix[i,j][0]
                g = pix[i,j][1]
                b = pix[i,j][2]
                a = pix[i,j][3]
                if DEBUG == 1:
                    print("Pixel value: (%d, %d)\n" %(i, j))
                    print('RGBA for i = %d, j = %d: (%d, %d, %d, %d), hex = %s' % (i, j, r, g, b, a, hex))

                hex = rgb2hex(r, g, b)
                s += '{\"text\":\"'
                if a <= 255/2:
                    block = "▒"
                else:
                    block = "█" 
                s += block
                s += '\",\"color\":\"'   
                s += hex
                if i == (imHeight - 1) and j == (imWidth - 1):
                    s += '\"}]'
                else:   
                    s += '\"},'
            if i < imHeight - 1:
                s += '{\"text\":\"\\n\"},'
        #print(s)
        myFile.write(s)
        myFile.write("\n\n")
        os.remove('temp__1.png')
