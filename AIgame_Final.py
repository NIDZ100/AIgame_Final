import tkinter as tk
from io import StringIO
#te ir loop lai varetu atsakt speli pec beigam
r = 1
while r != 2:
    #n ir skaitlis no kura mes atnemam, to var mainit,jo koks tiek generets. Bet uzskatu ka saja gadijuma tas nav vajadzigs.
    n = 20
#buffer kas kope output un parvieto popup window
    def popup_buffer(buffer):
        if not hasattr(popup_buffer, 'popup_window'):
            popup_buffer.popup_window = tk.Toplevel()
            popup_buffer.popup_window.title('Output')
            output_label = tk.Label(popup_buffer.popup_window, text=buffer.getvalue())
            output_label.pack()
            popup_buffer.popup_window.grab_set()
            popup_buffer.popup_window.focus_force()
            popup_buffer.popup_window.wait_window()
            popup_buffer.popup_window.destroy()
            del popup_buffer.popup_window
    output_buffer = StringIO()

    #GUI izvelamies kas ak speli, es vai dators
    def button1_click():
        global k
        k = 0
        root.destroy()
    def button2_click():
        global k
        k = 1
        root.destroy()

    root = tk.Tk()
    # moot = tk.Tk()
    button1 = tk.Button(root, text="dators", command=button1_click)
    button1.pack()

    button2 = tk.Button(root, text="speletajs", command=button2_click)
    button2.pack()
    root.mainloop()
    #j - vai spele turpinas
    j = True
    #x ir izveletais skaitlis 1,2,3
    x = 0
#generejam koka pamatu
    mas = [[0 for j in range(n - 1)] for i in range(n - 1)]
    for i in range(n - 1):
        for j in range(n - 1):
            mas[i][j] = n - 1 - i - j

    # izvadam so massivu
    #   print(mas[i][j], end=" ")
    # print()
    #sagatavojam koka pamatu pirms aizpildisanas
    def copy_array(arr):
        new_arr = [[0 for j in range(len(arr[i]))] for i in range(len(arr))]
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] > 1:
                    # izvitoju derigas virsotnes ar 0
                    new_arr[i][j] = 0
                elif arr[i][j] < 1:
                    new_arr[i][j] = "n"
                    # Pievienojam min limeni
                elif (arr[i][j] == 1 and j % 2 == 1):
                    new_arr[i][j] = -1
                else:
                    new_arr[i][j] = arr[i][j]
        return new_arr
    new_mas = copy_array(mas)

#aizpildam koku
    for i in range(n - 3, -1, -1):
        for j in range(0, n - i - 2):
            if j != n - 3:  # lai nebutu out of bounds
                if (i % 2 == 0):  # parbaudam limeni
                    a = new_mas[i + 1][j]
                    if new_mas[i + 1][j + 1] != "n":  # parbaudam vai deriga virsotne
                        b = new_mas[i + 1][j + 1]
                    else:
                        b = None  # ja virsotne neder pieskiram tai vertibu None
                    if new_mas[i + 1][j + 2] != "n":
                        c = new_mas[i + 1][j + 2]
                    else:
                        c = None
                    if (b == None and c == None):
                        new_mas[i][j] = a
                    #  print(a, new_mas[i][j],"max")
                    elif (b == None and c != None):
                        new_mas[i][j] = max(a, c)
                    #  print(a,c, new_mas[i][j],"max")
                    elif (b != None and c == None):
                        new_mas[i][j] = max(a, b)
                    #   print(a,b, new_mas[i][j],"max")
                    else:
                        new_mas[i][j] = max(a, b, c)
                    #  print(a,b,c, new_mas[i][j],"max")
                if (i % 2 == 1):
                    a = new_mas[i + 1][j]
                    if new_mas[i + 1][j + 1] != "n":
                        b = new_mas[i + 1][j + 1]
                    else:
                        b = None
                    if new_mas[i + 1][j + 2] != "n":
                        c = new_mas[i + 1][j + 2]
                    else:
                        c = None
                    if (b == None and c == None):
                        new_mas[i][j] = a
                    #  print(a, new_mas[i][j],"min")
                    elif (b == None and c != None):
                        new_mas[i][j] = min(a, c)
                    #  print(a,c, new_mas[i][j],"min")
                    elif (b != None and c == None):
                        new_mas[i][j] = min(a, b)
                    # print(a,b, new_mas[i][j],"min")
                    else:
                        new_mas[i][j] = min(a, b, c)
                    # print(a,b,c, new_mas[i][j],"min")
        # Izvadam ar MinMax modificetu koku.
        '''
    print("\nLast Array:\n")
    for i in range(n - 1):
        for j in range(n - 1):
            print(new_mas[i][j], end=" ")
        print()
'''
        #index ir adrese kura nosaka tagadejo atrashanas vietu kokaa. no ta index dators izvelas labako gajienu
    index = (0, 0)
    #definejam datora gajienus,atbilstoshi max un min limeniem, kas samazina n un izmaina index atbilstosi izveletam gajienam(no 1 lidz 3)
    def gajiens():
        global n
        global index
        #!!Viss ievads spele ir implementets ir caur popup logiem.Manuprat, tiek izpildits nosacijums ka nav komandrindinju programma.
        if (new_mas[index[0]][index[1] + 2] == 1):
            n = n - 3
            index = (index[0] + 1, index[1] + 2)
            print(n,"jo tika atnemts -3", file=output_buffer)
          #  print(index)
        elif (new_mas[index[0]][index[1] + 1] == 1):
            n = n - 2
            index = (index[0] + 1, index[1] + 1)
            print(n, "jo tika atnemts -2", file=output_buffer)
            #print(index)

        elif (new_mas[index[0]][index[1]] == 1):

            n = n - 1
            index = (index[0] + 1, index[1])
            print(n, "jo tika atnemts -1", file=output_buffer)
            # print(index)
        elif (new_mas[index[0]][index[1]] == -1):

            n = n - 1
            index = (index[0] + 1, index[1])

            print(n, "jo tika atnemts -1", file=output_buffer)
            # print(index)


        elif (new_mas[index[0]][index[1] + 1] == -1):

            n = n - 2
            index = (index[0] + 1, index[1])

            print(n,"jo tika atnemts -2", file=output_buffer)
        elif (new_mas[index[0]][index[1] + 2] == -1):

            n = n - 3
            index = (index[0] + 1, index[1] + 2)
            print(n,"jo tika atnemts -3", file=output_buffer)
            # print(index)
        popup_buffer(output_buffer)
    def gajiens2():
        global n
        global index
        if (new_mas[index[0]][index[1] + 2] == -1):
            n = n - 3
            index = (index[0] + 1, index[1] + 2)
            print(n, "jo tika atnemts -3", file=output_buffer)
            # print(index)
        elif (new_mas[index[0]][index[1] + 1] == -1):
            n = n - 2
            index = (index[0] + 1, index[1] + 1)
            print(n, "jo tika atnemts -2", file=output_buffer)
            #  print(index)
        elif (new_mas[index[0]][index[1]] == -1):
            n = n - 1
            index = (index[0] + 1, index[1])
            print(n, "jo tika atnemts -1", file=output_buffer)
            #  print(index)
        elif (new_mas[index[0]][index[1]] == 1):
            n = n - 1
            index = (index[0] + 1, index[1])
            print(n, "jo tika atnemts -1", file=output_buffer)
            #  print(index)
        elif (new_mas[index[0]][index[1] + 1] == 1):
            n = n - 2
            index = (index[0] + 1, index[1])
            print(n, "jo tika atnemts -2", file=output_buffer)
            #   print(index)
        elif (new_mas[index[0]][index[1] + 2] == 1):
            n = n - 3
            index = (index[0] + 1, index[1] + 2)
            print(n, "jo tika atnemts -3", file=output_buffer)
            #   print(index)
        popup_buffer(output_buffer)
 #Parbaide vai sasniedzam koka beigas
    def check():
        global j
        global n

        if ((new_mas[index[0]][index[1]] == -1 and new_mas[index[0]][index[1] + 1] == "n" and new_mas[index[0]][
            index[1] + 2] == "n")):
            j = False

        elif (new_mas[index[0]][index[1]] == 1 and new_mas[index[0]][index[1] + 1] == "n" and new_mas[index[0]][
            index[1] + 2] == "n"):
            j = False

        elif (new_mas[index[0]][index[1]] == "n" and new_mas[index[0]][index[1] + 1] == "n" and new_mas[index[0]][
            index[1] + 2] == "n"):
            j = False
        if ((n == 1) and (j % 2 == 0) and (k == 1)):
            print("dators uzvareja", file=output_buffer)
            popup_buffer(output_buffer)
        elif ((n == 1) and (j % 2 == 1) and (k == 1)):
            print("dators zaudeja", file=output_buffer)
            popup_buffer(output_buffer)
        elif n < 1:
            print("tu zaudeji")
            popup_buffer(output_buffer)
        if ((n == 2) and (i % 2 == 0)):
            print("tu zaudeji, dators izvelas -1, file=output_buffer")
            popup_buffer(output_buffer)

    def check2():
        global j
        global n
        if ((new_mas[index[0]][index[1]] == -1 and new_mas[index[0]][index[1] + 1] == "n" and new_mas[index[0]][
            index[1] + 2] == "n")):
            j = False

        elif (new_mas[index[0]][index[1]] == 1 and new_mas[index[0]][index[1] + 1] == "n" and new_mas[index[0]][
            index[1] + 2] == "n"):
            j = False

        elif (new_mas[index[0]][index[1]] == "n" and new_mas[index[0]][index[1] + 1] == "n" and new_mas[index[0]][
            index[1] + 2] == "n"):
            j = False
        if n == 1:
            print("tu uzvareji", file=output_buffer)
            popup_buffer(output_buffer)
        elif n < 1:
            print("tu zaudeji", file=output_buffer)
            popup_buffer(output_buffer)
        if ((n == 2) and (i % 2 == 0)):
            print("tu zaudejii, dators izvelas -1 ", file=output_buffer)
            popup_buffer(output_buffer)

#Definejam speletaja gajienu
    def mansg():
        global n
        global index
#izveidojam GUI
        def set_x(value):
            global x
            x = value
            popup.destroy()

        popup = tk.Tk()
        popup.geometry("300x100+100+100")  # Set the size and position of the popup window
        popup.title("Izvelieties cik atnemt")

        btn1 = tk.Button(popup, text="1", width=10, height=2, command=lambda: set_x(1))
        btn2 = tk.Button(popup, text="2", width=10, height=2, command=lambda: set_x(2))
        btn3 = tk.Button(popup, text="3", width=10, height=2, command=lambda: set_x(3))

        btn1.pack(side="left", padx=10)
        btn2.pack(side="left", padx=10)
        btn3.pack(side="left", padx=10)

        popup.mainloop()
#x ir speletaja ievaditais skaitlis
        if x == 1:
            index = (index[0] + 1, index[1])
            n = n - 1
            print(n, "jo tika atnemts -1", file=output_buffer)

        elif x == 2:
            index = (index[0] + 1, index[1] + 1)
            n = n - 2
            print(n, "jo tika atnemts -2", file=output_buffer)

        elif x == 3:
            index = (index[0] + 1, index[1] + 2)
            n = n - 3
            print(n, "jo tika atnemts -3", file=output_buffer)
    #    print(index)
        popup_buffer(output_buffer)
#Ja dators saka speli
    if k == 0:
        while j:
            gajiens()
            check()
            if j == False:
                break
            mansg()
            check()
            if j == False:
                break
#Ja speletajs saka speli
    if k == 1:
        while j:
            mansg()
            check2()
            if j == False:
                break
            gajiens2()
            check()
            if j == False:
                break
pass













