from PIL import Image, ImageDraw, ImageFont

# loop through all the entries
for i in range(1, 1000):
    img = Image.new('RGB', (1280, 720), color = (255, 0, 0))
    fnt = ImageFont.truetype('beb.otf', 250)
    title = "DAY #{}".format(i)
    d = ImageDraw.Draw(img)
    d.text((50,300), title, font=fnt, fill=(255, 255, 255))
    img.save(title+'.png')

print("Done !")
