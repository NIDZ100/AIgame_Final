import tkinter as tk
r=1
while r!=2:
    n=20
    '''
    def button3_click():
        global n
        print("Buttked")
        n=19
    
    
    def button4_click():
        global n
        print("Bur")
        n=20
        moot.destroy()
    
    def button5_click():
        global n
        print("Burra")
        n = 21
     '''
    def button1_click():
        global k
        print("Button 1 clicked")
        k=0
        root.destroy()
    def button2_click():
        global k
        print("Button 2 clicked")
        k=1
        root.destroy()

    root = tk.Tk()
    #moot = tk.Tk()
    button1 = tk.Button(root, text="dators", command=button1_click)
    button1.pack()

    button2 = tk.Button(root, text="es", command=button2_click)
    button2.pack()
    '''
    button3 = tk.Button(moot, text="19", command=button3_click)
    button3.pack()
    
    button4 = tk.Button(moot, text="20", command=button4_click)
    button4.pack()
    
    button5 = tk.Button(moot, text="21", command=button5_click)
    button5.pack()
    
    moot.mainloop()
    '''
    root.mainloop()
    j = True
    x = 0

    mas = [[0 for j in range(n - 1)] for i in range(n - 1)]
    for i in range(n - 1):
        for j in range(n - 1):
            mas[i][j] = n - 1 - i - j


    # izvadam so massivu
    #   print(mas[i][j], end=" ")
    # print()
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

    """
    print("\nNew Array:\n")
    for i in range(n-1):
        for j in range(n-1):
            print(new_mas[i][j], end=" ")
        print()
     """

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
    print("\nLast Array:\n")
    for i in range(n - 1):
        for j in range(n - 1):
            print(new_mas[i][j], end=" ")
        print()

    # i = int(input("Who styarts the game(0/1)"))

    index = (0, 0)


    # new_mas[index[0]][index[1]]
    def gajiens():
        # e=new_mas[index[0]][index[1]+2]
        global n
        global index
        if (new_mas[index[0]][index[1] + 2] == 1):

            n = n - 3
            index = (index[0] + 1, index[1] + 2)
            print(n, "-3")
            print(index)

        elif (new_mas[index[0]][index[1] + 1] == 1):
            n = n - 2
            index = (index[0] + 1, index[1] + 1)
            print(n, "-2")
            print(index)

        elif (new_mas[index[0]][index[1]] == 1):

            n = n - 1
            index = (index[0] + 1, index[1])
            print(n, "-1")
            print(index)


        elif (new_mas[index[0]][index[1]] == -1):

            n = n - 1
            index = (index[0] + 1, index[1])

            print(n, "-1")
            print(index)


        elif (new_mas[index[0]][index[1] + 1] == -1):

            n = n - 2
            index = (index[0] + 1, index[1])
            print(index)
            print(n, "-2")
        elif (new_mas[index[0]][index[1] + 2] == -1):

            n = n - 3
            index = (index[0] + 1, index[1] + 2)
            print(n, "-3")
            print(index)


    def gajiens2():
        # e=new_mas[index[0]][index[1]+2]
        global n
        global index
        if (new_mas[index[0]][index[1] + 2] == -1):
            n = n - 3
            index = (index[0] + 1, index[1] + 2)
            print(n, "-3")
            print(index)
        elif (new_mas[index[0]][index[1] + 1] == -1):
            n = n - 2
            index = (index[0] + 1, index[1] + 1)
            print(n, "-2")
            print(index)
        elif (new_mas[index[0]][index[1]] == -1):
            n = n - 1
            index = (index[0] + 1, index[1])
            print(n, "-1")
            print(index)
        elif (new_mas[index[0]][index[1]] == 1):
            n = n - 1
            index = (index[0] + 1, index[1])
            print(n, "-1")
            print(index)
        elif (new_mas[index[0]][index[1] + 1] == 1):
            n = n - 2
            index = (index[0] + 1, index[1])
            print(n, "-2")
            print(index)
        elif (new_mas[index[0]][index[1] + 2] == 1):
            n = n - 3
            index = (index[0] + 1, index[1] + 2)
            print(n, "-3")
            print(index)


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
        if ((n == 1)and(j%2==0)and(k==1)):
            print("datorins uzv")
        elif ((n == 1)and(j%2==1)and(k==1)):
            print("datorins zaud")
        elif n < 1:
            print("tus zaudet")
        if ((n == 2) and (i % 2 == 0)):
            print("tu zaude, dators -1")


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
            print("tu uzvar")

        elif n < 1:
            print("tu zaudet")
        if ((n == 2) and (i % 2 == 0)):
            print("tu zaudejii/dators -1 dara")


    def mansg():
        global n
        global index

        # Create a function to set the value of x
        def set_x(value):
            global x
            x = value
            popup.destroy()  # Close the popup window

        # Create a popup window with three buttons
        popup = tk.Tk()
        popup.geometry("300x100+100+100")  # Set the size and position of the popup window
        popup.title("Choose sticks")

        btn1 = tk.Button(popup, text="1", width=10, height=2, command=lambda: set_x(1))
        btn2 = tk.Button(popup, text="2", width=10, height=2, command=lambda: set_x(2))
        btn3 = tk.Button(popup, text="3", width=10, height=2, command=lambda: set_x(3))

        btn1.pack(side="left", padx=10)
        btn2.pack(side="left", padx=10)
        btn3.pack(side="left", padx=10)

        popup.mainloop()  # Start the popup window

        # Process the value of x and update index and n
        if x == 1:
            index = (index[0] + 1, index[1])
            n = n - 1
            print(n, "-1")

        elif x == 2:
            index = (index[0] + 1, index[1] + 1)
            n = n - 2
            print(n, "-2")

        else:
            index = (index[0] + 1, index[1] + 2)
            n = n - 3
            print(n, "-3")
        print(index)


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

    # Access the element using the index
    # print(mas[index[0]][index[1]])  # output: 5
input("spied!")













