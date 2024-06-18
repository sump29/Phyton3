from PIL import Image, ImageDraw


img = Image.new('RGB', (300, 300), color='white')
draw = ImageDraw.Draw(img)


draw.rectangle((50, 50, 250, 250), fill='green')
draw.rectangle((100, 100, 200, 200), fill='red')
draw.polygon([(150, 150), (250, 250), (100, 250)], fill='blue')
draw.ellipse((150, 150, 250, 250), fill='none', outline='black')


img.save('my_image.png')