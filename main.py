from PIL import Image

otvetkabase = Image.open("otvetkabase2.png")
w, h = otvetkabase.size

print ("Напишите название файла, файл должен быть в той-же папка что и exe!")
filename = input(": ")

filename2 = Image.open(filename)

w2, h2 = filename2.size

back = Image.new("RGB", (w2, (h2 + h)), (255, 255, 255))

if h2 > h:
    back = back.resize((w2, (h2 + h)))

h3 = (h2 + h)

wb, hb = back.size

otvetkabase = otvetkabase.resize((w2,h))


back.paste(filename2,(0, h3 - h2))
back.paste(otvetkabase)

otvetkabase = otvetkabase.convert('RGBA')
back = back.convert('RGBA')

back = back.save("temp.png","PNG")

input()