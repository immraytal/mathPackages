import numpy
from PIL import Image, ImageDraw
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

image = Image.open('a_image.tif')  # Открываем изображение
image.show()
imarray = numpy.array(image)
#print(imarray.shape)
#print(image.size)
#print(imarray)

draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту
pix = image.load()  # Выгружаем значения пикселей
print("pix = " , pix)
print(pix[10, 10])


#mode = int(input('mode:'))  # Считываем номер преобразования.
for i in range(width):
     for j in range(height):
       # print(type(pix[i, j][0]))
       # if type(pix[i, j][0]) == int:
       # print(pix[i, j])
        a = pix[i, j]
#       a = pix[i, j]
        b = pix[i, j]
        c = pix[i, j]
        draw.point((i, j), (a, b, c))
image.show()
imarray1 = numpy.array(image)
#print(imarray1)
# for x in range(width):
#     for y in range(height):
#        r = pix[x, y][0] #узнаём значение красного цвета пикселя
#        g = pix[x, y][1] #зелёного
#        b = pix[x, y][2] #синего
#        sr = (r + g + b)  #среднее значение
#        draw.point((x, y), (r - g, r + g , b)) #рисуем пиксель
#
# image.save("result.jpg", "JPEG") #не забываем сохранить изображение
