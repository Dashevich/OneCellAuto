from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mb
import copy
import random
# names of constants - more understandable
col = 'black'
up_str = []
list_of_inf = []
down = 750
left = 50
right = 1250
up = 150
gap = 10
t = []
inf = [0] * 8
width = int((right - left) / gap)
length = int((down - up) / gap)
mas = [[0] * length for i in range(width)]
beginx = int(width / 2)
beginy = 1
mas[beginx - 1][beginy - 1] = 1
num = 0
step = 40
dist = 70
gr = 100
quantity = 0
ind = 0

def new():
    global down
    global left
    global right
    global up
    global gap
    global width
    global length
    global mas
    global beginx
    global beginy
    global inf
    down = 750
    left = 50
    right = 1250
    up = 150
    gap = 10
    width = int((right - left) / gap)
    length = int((down - up) / gap)
    inf = [0] * 8
    mas = [[0] * length for i in range(width)]
    beginx = int(width / 2)
    beginy = 1
    mas[beginx - 1][beginy - 1] = 1

def create():
    global mas
    global length
    global width
    ind = 0
    ind1 = 0
    a1 = mas[0][0]
    a2 = mas[0][0]
    a3 = mas[1][0]
    for j in range(length):
        for i in range(width):
            if length - 1 > j:
                if ind != j:
                    a1 = mas[width - 2][j]
                    a2 = mas[width - 1][j]
                    ind = j
                    ind1 = 1
                elif ind1 == 1:
                    a1 = mas[width - 1][j]
                    a2 = a3
                    ind1 = 0
                else:
                    a1 = a2
                    a2 = a3
                a3 = mas[i][j]
                mas[i - 1][j + 1] = opr(a1, a2, a3)

    return mas


def opr(a1, a2, a3):
    global inf
    a = 0
    a11 = 0
    a22 = 0
    a33 = 0
    for i in range(8):
        if a1 == a11 and a2 == a22 and a3 == a33:
            a = inf[7 - i]
        if a22 == 1 and a33 == 1:
            a11 = 1
        if a33 == 1:
            if a22 == 0:
                a22 = 1
            else:
                a22 = 0
            a33 = 0
        else:
            a33 = 1
    return a


def set(canvas):
    global gap
    for i in range(0, down - up, gap):
        canvas.create_line(left, up + i, right, up + i)
    for i in range(0, right - left, gap):
        canvas.create_line(i + left, up, i + left, down)


def paint():
    global gap
    global canvas
    for j in range(length):
        for i in range(width):
            if mas[i][j] == 1:
                canvas.create_rectangle(left + i * gap, up + j * gap, left + gap + i * gap, up + gap + j * gap, outline="black", fill="black")
            if mas[i][j] == 0:
                canvas.create_rectangle(left + i * gap, up + j * gap, left + gap + i * gap, up + gap + j * gap, outline=col, fill="white")


def rule(canvas):
    global step
    global dist
    global t
    coord = 60
    b = 20
    step = 40
    str = [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    count = 0
    for i in str:
        if i == 0:
            str[count] = 'white'
        else:
            str[count] = 'black'
        count += 1
    for i in range(8):
        # numbers - in constants
        canvas.create_rectangle(coord, b, coord + step, b+step, outline="black", fill=str[(i + 1) * 3 - 3])
        coord = coord + step
        canvas.create_rectangle(coord, b, coord + step, b + step, outline="black", fill=str[(i + 1) * 3 - 2])
        b = b + step
        canvas.create_rectangle(coord, b, coord + step, b + step, outline="black", fill='white')
        t.append('white')
        b = b - step
        coord = coord + step
        canvas.create_rectangle(coord, b, coord + step, b + step, outline="black", fill=str[(i + 1) * 3 - 1])
        coord = coord + dist


def callback(event):
    global inf
    global gr
    global step
    global dist
    global gap
    global gr
    global gap
    global up
    global mas
    global width
    global name
    step = 40
    gr = 100
    a = event.x
    b = event.y
    # just refactor it
    for i in range(8):
        if gr < a < gr + step and 60 < b < 100:
            if t[i] == 'white':
                canvas.create_rectangle(gr, 60, gr + step, 100, outline="black", fill='black')
                t[i] = 'black'
                inf[i] = 1
            else:
                canvas.create_rectangle(gr, 60, gr + step, 100, outline="black", fill='white')
                t[i] = 'white'
                inf[i] = 0
        gr = gr + step * 2 + dist
    gr = 50
    if name == 'picture':
        for i in range(width):
            if gr < a < gr + gap and up < b < up + gap:
                if mas[i][0] == 0:
                    canvas.create_rectangle(gr, up, gr + gap, up + gap, outline="black", fill='black')
                    mas[i][0] = 1
                else:
                    canvas.create_rectangle(gr, up, gr + gap, up + gap, outline="black", fill='white')
                    mas[i][0] = 0
            gr = gr + gap
    print(a, b)


def grd():
    global col
    if col == 'black':
        col = 'white'
    else:
        col = 'black'
    go()

def go():
    global mas
    mas = create()
    paint()


def choose():
    global gap
    global width
    global length
    global mas
    global beginx
    global beginy
    global combo
    gap = int(combo.get())
    width = int((right - left) / gap)
    length = int((down - up) / gap)
    mas = [[0] * length for i in range(width)]
    beginx = int(width / 2) + 1
    beginy = 1
    mas[beginx - 1][beginy - 1] = 1
    go()

def mases():
    global mas
    global inf
    global length
    global width
    global list_of_inf
    list_of_inf = []
    mas1 = copy.deepcopy(mas)
    for i in range(256):
        num = bin(i)
        num = num.split('b')[1]
        num = '0' * (8 - len(num)) + num
        count = 0
        for i in num:
            inf[count] = int(i)
            count += 1
        mas = create()
        count = 0
        for j in range(length):
            for i in range(width):
                if mas1[i][j] != mas[i][j]:
                    count += 1
                    break
        if count == 0:
            list_of_inf.append(inf.copy())
    print(list_of_inf)


def next():
    global inf
    global mas
    global num
    global list_of_inf
    global inf1
    global numrules
    global new_file
    ind = 0
    longend = numrules.__len__() - 1
    print(longend)
    inf = [0] * 8
    inf1 = [0] * 8
    bnext['state'] = 'disabled'
    num = random.randint(0, longend)
    num = numrules[num]
    new_file.write(str(num))
    print(num)
    num = bin(num)
    numi = str(num)
    numi = numi.split('b')[0] + numi.split('b')[1]
    numi = numi[::-1]
    numi += '0' * 7
    # (use list generator)
    for i in range(7):
        inf[7 - i] = int(numi[i])
    go()
    inf1 = copy.deepcopy(inf)
    mases()
    inf = copy.deepcopy(inf1)
    # print(numi)


def ans():
    global inf
    global mas
    global inf1
    global mas1
    global width
    global length
    global right
    global left
    global down
    global up
    global gap
    global t
    global bchs
    global bnext
    global bok
    global canvas
    global quantity
    global list_of_inf
    global ind
    global new_file
    t = []
    lbl1 = ' '
    width = int((right - left) / gap)
    length = int((down - up) / gap)
    ans1 = message.get()
    num = int(ans1)
    num = bin(num)
    num = num.split('b')[1]
    num = '0' * (8 - len(num)) + num
    count = 0
    for i in num:
        inf1[count] = int(i)
        count += 1
    print(list_of_inf)
    for i in list_of_inf:
        #print(i)
        count = 0
        for j in range(8):
            if str(i[j]) == str(inf1[j]):
                count += 1
        if count == 8:
            break
    if count < 8:
        print("No")
        if ind == 0:
            rule(canvas)
            bchs['state'] = 'disabled'
            inf = [0] * 8
            test.bind("<Button-1>", callback)
            bok = Button(test, text='Ок', command=noright, width=10, height=2, bg="white")
            bok.place(x=600, y=70)
            new_file.write(' - \n')
        if ind == 1:
            a = ' ' * 46
            lbl1 = Label(test, text="128" + a + "64" + a + "32" + a + "16" + a + " 8" + a + " 4" + a + "  2" + a + "   1")
            lbl1.place(x=105, y=120)
            ind = 2
    else:
        if ind == 0:
            new_file.write(' + \n')
        mb.showinfo(title="Ответ", message="Правильно")
        canvas.create_rectangle(5, 5, 1300, 149, outline="gray94", fill='gray94')
        print("Yes")
        bnext['state'] = 'normal'
        bok.destroy()
        lbl1 = Label(test, text = 1300 * " ")
        lbl1.place(x=105, y=120)
    canvas.pack(fill=BOTH, expand=1)
    #print(inf)
    #print(inf1)
    #print(mas)


def testpaint():
    global inf
    global inf1
    test.bind("<Button-1>", callback)
    bok = Button(test, text='Ок', command=noright, width=10, height=2, bg="white")

def noright():
    global inf
    global inf1
    global step
    global dist
    global quantity
    global ind
    global bok
    inf1 = copy.deepcopy(inf)
    gr = 100
    quantity = 0
    k = 0
    for i in list_of_inf:
        count = 0
        for j in range(8):
           if i[j] == inf1[j]:
                count += 1
        if k < count:
            inf = copy.deepcopy(i)
            k = count
    print("ошибка")
    print(inf1)
    print(inf)
    for i in range(8):
        if inf[i] != inf1[i]:
            #canvas.create_rectangle(gr - 40 , 20, gr + step * 2, 120, outline="black", fill='red')
            canvas.create_rectangle(gr - 45, 10, gr + step * 2 + 5, 19, outline="red", fill='red')
            canvas.create_rectangle(gr - 45, 101, gr + step * 2 + 5, 110, outline="red", fill='red')
            canvas.create_rectangle(gr - 45, 10, gr - 41, 110, outline="red", fill='red')
            canvas.create_rectangle(gr + step * 2 + 1, 10, gr + step * 2 + 5, 110, outline="red", fill='red')
            canvas.create_rectangle(gr - 41, 61, gr - 1, 110, outline="red", fill='red')
            canvas.create_rectangle(gr + 41, 61, gr + step * 2 + 5, 110, outline="red", fill='red')
        else:
            quantity += 1
            canvas.create_rectangle(gr - 45, 10, gr + step * 2 + 5, 19, outline="gray94", fill='gray94')
            canvas.create_rectangle(gr - 45, 101, gr + step * 2 + 5, 110, outline="gray94", fill='gray94')
            canvas.create_rectangle(gr - 45, 10, gr - 41, 110, outline="gray94", fill='gray94')
            canvas.create_rectangle(gr + step * 2 + 1, 10, gr + step * 2 + 5, 110, outline="gray94", fill='gray94')
            canvas.create_rectangle(gr - 41, 61, gr - 1, 110, outline="gray94", fill='gray94')
            canvas.create_rectangle(gr + 41, 61, gr + step * 2 + 5, 110, outline="gray94", fill='gray94')
        gr = gr + step * 2 + dist
    if quantity < 8:
        inf = copy.deepcopy(inf1)
        testpaint()
    else:
        bchs['state'] = 'normal'
        bok['state'] = 'disabled'
        ind = 1

def window1():
    global picture
    global canvas
    global combo
    global inf
    global mas
    global width
    global length
    global left
    global up
    global right
    global down
    global beginx
    global beginy
    global gap
    global combo
    global size
    global name
    new()
    name = 'picture'
    gap = 10
    inf = [0] * 8
    mas = [[0] * length for i in range(width)]
    picture = Toplevel(root_window)
    picture.title("Отрисовка")
    picture.geometry(size)
    picture.wm_state('zoomed')
    canvas = Canvas(picture, width=200, height=100)
    canvas.create_rectangle(left, up, right, down, outline="black", fill="white")
    canvas.pack(fill=BOTH, expand=1)
    combo = Combobox(picture)
    combo['values'] = (2, 5, 10, 20, 50, 100)
    combo.current(2)
    combo.place(x=1300, y=200)
    rule(canvas)
    gap = int(combo.get())
    bch = Button(picture, text = 'Выбрать', command=choose, width = 20, height = 3, bg="white")
    bch.place(x = 1300, y = 230)
    set(canvas)
    canvas.create_rectangle(beginx * gap + 50, up, beginx * gap + gap + 50, up + 10, outline="black", fill="black")
    picture.bind("<Button-1>", callback)
    width = int((right-left)/gap)
    length = int((down-up)/gap)
    mas = [[0] * length for i in range(width)]
    beginx = int(width/2) + 1
    beginy = 1
    mas[beginx - 1][beginy - 1] = 1
    col = 'black'
    #grid(col)
    btn = Button(picture, text = 'Отрисовать', command=go, width = 20, height = 3, bg="white")
    btn.place(x = 1300, y = 30)
    bgrid = Button(picture, text='Сетка', command=grd, width=20, height=3, bg="white")
    bgrid.place(x=1300, y=131)
    bc = Button(picture, text='Назад', command=quit_program1, width=20, height=3, bg="white")
    bc.place(x=1300, y=700)
    print(name)
    picture.mainloop()


def window2():
    global test
    global canvas
    global message
    global combo
    global size
    global bchs
    global bnext
    global inf1
    global gap
    global numrules
    global name
    global width
    global gr
    global new_file
    new()
    name = 'test'
    gap = 10
    inf1 = [0] * 8
    test = Toplevel(root_window)
    #test.wm_state('zoomed')
    test.title("Test")
    test.geometry(size)
    canvas = Canvas(test, width=200, height=100)
    canvas.create_rectangle(left, up, right, down, outline="black", fill="white")
    canvas.pack(fill=BOTH, expand=1)
    set(canvas)
    # work with file
    file = open('auto.txt', 'r')
    count = 0
    gr = 50
    for line in file:
        if count == 0:
            numrule = line.split(':')[1]
        if count == 1:
            sost = line.split(':')[1]
        count += 1
    numrule = numrule.replace(' ', '')
    numrule = numrule.replace('\n', '')
    numrule = numrule.split(',')
    numrules = []
    for i in numrule:
        if '-' in i:
            for j in range(int(i.split('-')[0]),1 + int(i.split('-')[1])):
                numrules.append(j)
        else:
            numrules.append(int(i))
    sost = int(sost.replace(' ',''))
    if sost == 0:
        sost1 = random.randint(1, width - 1) // 2
        print(sost1)
        for i in range(sost1):
            count = random.randint(1, width-1)
            print(count)
            canvas.create_rectangle(gr + count * gap, up, gr + count * gap + gap, up + gap, outline="black", fill='black')
            mas[count][0] = 1
    file.close()
    # work with file end
    new_file = open('result.txt', 'w')
    message = StringVar()
    txt = Entry(test, width=24, textvariable=message)
    txt.place(x=1300, y=30)
    combo = Combobox(test)
    combo['values'] = (2, 5, 10, 20, 50, 100)
    combo.current(2)
    combo.place(x=1300, y=390)
    gap = int(combo.get())
    canvas.create_rectangle(beginx * gap + 50, up, beginx * gap + gap + 50, up + 10, outline="black", fill="black")
    bch = Button(test, text='Выбрать', command=choose, width=20, height=3, bg="white")
    bch.place(x=1300, y=420)
    bchs = Button(test, text='Ответить', command=ans, width=20, height=2, bg="white")
    bchs.place(x=1300, y=60)
    bc = Button(test, text='Назад', command=quit_program2, width=20, height=3, bg="white")
    bc.place(x=1300, y=700)
    bnext = Button(test, text='Сгенерировать', command=next, width=20, height=3, bg="white")
    bnext.place(x=1300, y=600)
    bgrid = Button(test, text='Сетка', command=grd, width=20, height=3, bg="white")
    bgrid.place(x=1300, y=150)
    test.mainloop()

# do smth with it - one function with parametrs
def quit_program1():
    picture.destroy()

def quit_program2():
    test.destroy()

def quit_program():
    root_window.destroy()


global root_window
root_window = Tk()
#root_window.wm_state('zoomed')
root_window.title("Одноклеточные автоматы")
WidthWindow = root_window.winfo_screenwidth()
HeightWindow = root_window.winfo_screenheight()
size = str(WidthWindow) + 'x' + str(HeightWindow)
root_window.geometry(size)
btn1 = Button(root_window, text = 'Тест', command=window2, width = 20, height = 3, bg="white")
btn1.place(x = 700, y = 500)
btn = Button(root_window, text = 'Отрисовка', command=window1, width = 20, height = 3, bg="white")
btn.place(x = 700, y = 200)
bc = Button(root_window, text='Выход', command=quit_program, width=20, height=3, bg="white")
bc.place(x=1300, y=700)
root_window.mainloop()