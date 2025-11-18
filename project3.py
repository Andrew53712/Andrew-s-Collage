# CPS121 Project 3
# Written: 11/17/25 Andrew Woods woodsandrew09@gmail.com
# 
# A collage featuring a few of my personal favorite sports leagues, teams and their respective logos. 
# Functions include rotation, mirroring, color change and inversion, and others. 
#
# Change each occurrence of "_" in the list below to be "Y" or "N" to indicate
# whether or not the given transformation is implemented in your program.
#
#   Can be done using just getPixels()
#   _ Altering colors of the image
#   _ Grayscale
#   _ Making darker or lighter
#   _ Sepia-toned
#   _ Posterized
#   Need nested loops
#   _ Mirrorizing
#   _ Edge detection
#   _ Chromakey (change background)
#   _ Blurring
#   Need nested loops and alter size or shape
#   _ Rotation
#   _ Cropping
#   _ Shifting
#   Other transformations
#   _ <description of transformation>
#   _ <description of transformation>
#   _ <description of transformation>
# ============================================================================

import GCPictureTools as pgt
import pygame as pg
import os, sys
import traceback

# ============================================================================
# ================ Start making changes after this comment ===================
# ============================================================================

# ---- SUPPORTING FUNCTIONS SHOULD GO HERE ----

def colorchange1(pic):
    
    width = pic.getWidth()
    height = pic.getHeight()
    new = pgt.Picture(width, height)
    
    for i in range(width):
        for j in range(height):
            color = pic.getColor(i, j)
            r = color.r
            g = color.g
            b = color.b
            
            # check if the pixel is gray, white, or black
            if r < 30 and g < 30 and b < 30:  # black
                new_r, new_g, new_b = r, g, b
            elif r > 225 and g > 225 and b > 225:  # white
                new_r, new_g, new_b = r, g, b
            elif abs(r - g) < 20 and abs(r - b) < 20 and abs(g - b) < 20:  # gray
                new_r, new_g, new_b = r, g, b
            # recolor red pixels
            elif r > g and r > b:
                new_r, new_g, new_b = 255, 215, 0  # gold
            # recolor blue pixels
            elif b > r and b > g:
                new_r, new_g, new_b = 128, 0, 128  # purple
            # all other colors stay the same
            else:
                new_r, new_g, new_b = r, g, b
            
            # put the pixel in the mirrored spot
            new.setColor(width - 1 - i, j, (new_r, new_g, new_b))
    
    return new


def flipimageVert(pic):
    """
    Flip pic vertically.
    """
    width, height = pic.getWidth(), pic.getHeight()
    new = pgt.Picture(width, height)

    for x in range(width):
        for y in range(height):

            color = pic.getColor(x, y)

            # place pixel upside down in transformed
            new.setColor(x, height - 1 - y, color)

    return new


def flipimageHorizontal(pic):
    """
    Flip pic horizontally.
    """
    width, height = pic.getWidth(), pic.getHeight()
    new = pgt.Picture(width, height)

    for x in range(width):
        for y in range(height):
            color = pic.getColor(x, y)
            new.setColor(width - 1 - x , y, color)

    return new


def colorinvert(pic):
    """
    invert colors.
    """
    width, height = pic.getWidth(), pic.getHeight()
    new = pgt.Picture(width, height)

    for x in range(width):
        for y in range(height):
            color = pic.getColor(x, y)
            r, g, b = color.r, color.g, color.b

            # invert colors
            r, g, b = 255 - r, 255 - g, 255 - b

            new.setColor(x , y, (r, g, b))

    return new

def cropit(pic, newWidth, newHeight):
    """crop the image and make it smaller
    """
    width, height = pic.getWidth(), pic.getHeight()
    new = pgt.Picture(newWidth, newHeight)

    x = int(width/2 - newWidth/2)
    y = int(height/2 - newHeight/2)
    for col in range(x, x+newWidth):
        for row in range(y, y+newHeight):
            color = pic.getColor(col, row)
            new.setColor(col - x, row - y, color)


    return new

def mirrorhorizontal(pic):
    """
    Mirror the image at the horizontal axis.
    """
    width, height = pic.getWidth(), pic.getHeight()
    new = pgt.Picture(pic)

    for x in range(width):
        for y in range(height // 2):

            color = pic.getColor(x, y)

            # place pixel upside down in transformed
            new.setColor(x, height - 1 - y, color)

    return new



def createCollage():
    """Create a collage.
 
    Returns
    -------
    Picture
        the collage.
    """
    # create "canvas" on which to make a collage.  You may exchange the
    # width and height values if you prefer a landscape orientation.
    collage = pgt.Picture(700, 950)

    # ---- YOUR CODE TO BUILD THE COLLAGE GOES HERE ----
    # Notice that this is **inside** the createCollage() function.  Because
    # createCollage() should be a "one-and-only-one-thing" function, you
    # should use supporting functions to do transformations, etc.  These
    # supporting functions should be defined below, after the code for this
    # function.
    pic1 = pgt.Picture('image1.png')
    pic2 = pgt.Picture('image2.png')
    pic3 = pgt.Picture('image3.jpg')
    pic4 = pgt.Picture('image4.png')
    
    pic5 = flipimageVert(pic1)
    pic5  = colorchange1(pic5)
    pic6 = colorinvert(pic4)
    pic6 = flipimageHorizontal(pic6)
    pic7 = cropit(pic2, pic2.getWidth() - 10, pic2.getHeight() - 10)
    pic7 = colorinvert(pic7)
    pic8 = mirrorhorizontal(pic3)
    pic9 = cropit(pic2, pic2.getWidth() - 20, pic2.getHeight() - 20)
    pic9 = flipimageHorizontal(pic9) and colorchange1(pic9)
    pic10 = colorinvert(pic3)
    pic11 = flipimageHorizontal(pic4)
    pic11 = cropit(pic11, pic11.getWidth() - 30, pic11.getHeight() - 30)

    pic1.copyInto(collage, 430, 0)
    pic3.copyInto(collage, 465, 480)
    pic2.copyInto(collage, 460, 760)
    pic4.copyInto(collage, 470, 220)
    pic5.copyInto(collage, 0, 0)
    pic6.copyInto(collage, 25, 220)
    pic7.copyInto(collage, 0, 780)
    pic8.copyInto(collage, 10, 480)
    pic9.copyInto(collage, 230, 180)
    pic10.copyInto(collage, 235, 400)
    pic11.copyInto(collage, 270, 675)
    return collage

def createWebPage(imageFile, webPageFile):
    """Create web page that contains the collage.
    Parameter: imageFile - the image file name 
    Parameter: webPageFile - the finename of the output web page 
    Returns
    -------
    nothing
    """

    htmlFile = open(webPageFile, "wt")

    # ---- YOUR CODE TO BUILD THE Webpage with the COLLAGE GOES HERE ----
    htmlFile.write("<!DOCTYPE html>\n")
    htmlFile.write("<html>\n")
    htmlFile.write(f"<img src=\"{imageFile}\"/>")
    htmlFile.write("</html>\n")
    print("output file:", htmlFile.name)
    htmlFile.close()    





# ============================================================================
# ============== Do NOT make any changes below this comment ==================
# ============================================================================

if __name__ == '__main__':

    # first command line argument, if any, is name of image file for output
    # second command line argument, if any, is name of the output html file name
    collageFile = None
    htmlFileName = "webpage.html"  #Default name

    if len(sys.argv) > 1:
        collageFile = sys.argv[1]
    if len(sys.argv) > 2:
        htmlFile = sys.argv[2]    

    # temporarily set media path to project directory
    scriptDir = os.path.dirname(os.path.realpath(sys.argv[0]))

    # create the collage
    
    collage = createCollage()
    #collage.display()

    try:
        # either show collage on screen or write it to file
        if collageFile is None:
            collage.display()
            input('Press Enter to quit...')
        else:
            print(f'Saving collage to {collageFile}')
            collage.save(collageFile)
            createWebPage(collageFile, htmlFileName)
    except:
        print('Could not show or save picture')

