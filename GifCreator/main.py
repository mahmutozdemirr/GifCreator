from PIL import Image, ImageDraw, ImageFont

fnt = ImageFont.truetype("arial", 50)
def create_image_with_text(wh, text):
    widht, height = wh
    img = Image.new("RGB", (500, 500),"yellow")
    draw = ImageDraw.Draw(img)
    draw.text((widht, height),text, font = fnt, fill="blue")
    return img

frames =[]
x, y = 0, 0
for i in range(100):
    new_frame = create_image_with_text((x-100, y), "FENERBAHÇE")
    frames.append(new_frame)
    x += 5
    y += 5

frames[0].save("moving_text.gif", format="GIF",
               append_images=frames[1:], save_all=True, duration=35, loop=0)
