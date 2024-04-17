from PIL import Image, ImageChops


def pixelSearch(image1, image2):
    result = ImageChops.difference(image1, image2)

    imgtest = result.convert("L")
    threshold = 27
    finalres = imgtest.point(
        lambda x: 255 if x > threshold else 0
    )

    column = 20
    stroke = 5
    boxLenght = 1
    boxHeight = 1

    while boxLenght < 6:
        while boxHeight < 6:
            color = finalres.getpixel((column, stroke))
            if color == 255:
                for i in range(1, 6):
                    color = finalres.getpixel((column + i, stroke))
                    if color == 255:
                        boxLenght += 1
                    else:
                        boxLenght = 1
                        break

                    color = finalres.getpixel((column, stroke + i))
                    if color == 255:
                        boxHeight += 1
                    else:
                        boxHeight = 1
                        break
            if boxLenght != boxHeight:
                boxLenght = 1
                boxHeight = 1
            if stroke >= 110:
                column += 3
                stroke = 0
            stroke += 5
            if column > 200:
                column = 80
                stroke = 50
                break
    if stroke >= 110:
        column -= 3
    stroke -= 5

    return column, stroke

def imageDiff(checkimage1, checkimage2):
    utilityImage1 = ImageChops.difference(checkimage1, checkimage2)
    utilityImage2 = ImageChops.difference(checkimage1, checkimage1)

    resImage1 = utilityImage1.convert("L")
    resImage2 = utilityImage2.convert("L")

    threshold = 23
    finalImage1 = resImage1.point(
        lambda x: 255 if x > threshold else 0
    )
    finalImage2 = resImage2.point(
        lambda x: 255 if x > threshold else 0
    )

    if finalImage1.getbbox() == finalImage2.getbbox():
        return True
    else:
        return False

def finalDirFinder():
    dir1 = 'genshin script/cap'
    global finaldir
    for i in range(1, 9):
        checkimg1 = Image.open(dir1 + str(i) + '/capcheck.jpg')
        checkimg2 = Image.open('genshin script/process/check.jpg')

        if imageDiff(checkimg1, checkimg2):
            finaldir = dir1 + str(i) + '/'
            break
    return finaldir