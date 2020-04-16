from PIL import Image
foo = Image.open('unnamed.png')
print(foo.size)
foo = foo.resize((50,50),Image.ANTIALIAS)
foo.save('image_rezied.png',quality=100)
