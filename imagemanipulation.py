from PIL import Image, ImageEnhance
img = Image.open('images/testimage.jpg')
img.show()

# Technique1 - Resize

print('Image size')
print(img.size)
print('Resizing the image\n')
newsize = (300, 300)
img_resized = img.resize(newsize)

print(img_resized.size)

img_resized.save('images/resized.jpg')
img_resized.show()

# Technique2 - Brightness

print('\n\nBrightning the Image\n')
#Define enhancer
enhancer = ImageEnhance.Brightness(img)

img_light = enhancer.enhance(1.8)     #you can also reduce brightness by just adjusting factor < 1

img_light.save('images/brightened.jpg')
img_light.show()


# Technique3 - GrayScale

print('\n\nImage gray scaling:')

img1 = Image.open('images/testimage.jpg')
img1 = img.convert('L')
img1.save('images/grayscale.jpg')
img1.show()
