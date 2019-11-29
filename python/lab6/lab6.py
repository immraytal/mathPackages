from PIL import Image
import numpy

im = Image.open('a_image.tif')
im.show()
imarray = numpy.array(im)
print(imarray.shape)
print(im.size)
print(imarray)
