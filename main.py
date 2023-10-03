from PIL import Image

typeimage = input("Фон ответки (D(discord),Y(youtube,белая тема),S(steam) ): ")

otvetkatype = Image.open("otvetkabased.png")

if typeimage == "d" or typeimage == "D":
    print("D")
    otvetkatype = Image.open("otvetkabased.png")
elif typeimage == "y" or typeimage == "Y":
    print("Y")
    otvetkatype = Image.open("otvetkabasey.png")
elif typeimage == "s" or typeimage == "S":
    print("S")
    otvetkatype = Image.open("otvetkabases.png")
else:
    print("Некорректный тип (выбран стандартный (D) )")
    otvetkatype = Image.open("otvetkabased.png")

otvetkabase = otvetkatype
w, h = otvetkabase.size

print ("Напишите название файла, (файл должен быть в той-же папка что и exe)")
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


otvetkaD = "temp.png"

convertq = input("Конвертировать .png в .gif? (y or n): ")
if convertq == "y" or convertq == "Y":
    otvetkaD = "temp.gif"
elif convertq == "n" or convertq == "N":
    otvetkaD = "temp.png"
else:
    print("Некорректный ответ")
back = back.save(otvetkaD)  
