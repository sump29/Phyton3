import PIL


def draw_name(name, size, color):
    image = PIL.Image.new('RGB', size, 'white')
    draw = PIL.ImageDraw.Draw(image)


    for letter in name:
        letter_image = PIL.Image.new('RGB', (size[0] // len(name), size[1]), 'white')
        letter_draw = PIL.ImageDraw.Draw(letter_image)


        if letter == 'К':
            letter_draw.polygon([(0, 0), (size[0] // len(name), 0), (size[0] // len(name), size[1])], fill=color)
        elif letter == 'и':
            letter_draw.polygon([(0, 0), (size[0] // len(name), 0), (size[0] // len(name), size[1])], fill=color)
        elif letter == 'р':
            letter_draw.polygon([(0, 0), (size[0] // len(name), 0), (size[0] // len(name), size[1])], fill=color)
            letter_draw.polygon(
                [(0, size[1] // 2), (size[0] // len(name), size[1] // 2), (size[0] // len(name), size[1])], fill=color)
        elif letter == 'л':
            letter_draw.polygon([(0, 0), (size[0] // len(name), 0), (size[0] // len(name), size[1])], fill=color)


    final_image = PIL.Image.new('RGB', size, 'white')
    final_image.paste(image, (0, 0))

    return final_image



name = 'Кирилл'
size = (500, 100)
color = 'black'

final_image = draw_name(name, size, color)
final_image.save('name.png')