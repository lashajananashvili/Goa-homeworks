#შექმენით ფუნქცია რომელიც აიღეს განუსაზღვრელი რაოდენობით არგუმენტებს და გადაეცით 7 სიტყვა და დააბრუნეთ წინადადება

def fun(*li):
    j=[]
    for i in li:
        j=j+i
    print(" ".join(j))

fun(["i","am","not","robot","i","am","human"])
