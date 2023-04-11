import tkinter as tk

# Create a new window
window = tk.Tk()

# Set the title of the window
window.title("My GUI")
def button1_click():
    log_message("n=20\n")
    global n
    global x
    n=20
    x=0
def button2_click():
    global k
    log_message("dator\n")
    k=0

def button3_click():
    global k
    log_message(" 3 clicked\n")
    k=1
button1 = tk.Button(window, text="Button 1", command=button1_click)
button2 = tk.Button(window, text="Button 2", command=button2_click)
button3 = tk.Button(window, text="Button 3", command=button3_click)
# Create a text widget to display log messages
log_widget = tk.Text(window, width=40, height=30)
log_widget.pack()

# Define a function to log a message in the text widget
def log_message(message):
    log_widget.insert(tk.END, message)

# Define functions to be called when each button is clicked


def button4_click():
    global new_mas
    mas = [[0 for j in range(n - 1)] for i in range(n - 1)]
    for i in range(n - 1):
        for j in range(n - 1):
            mas[i][j] = n - 1 - i - j

    # izvadam so massivu
    #   log_message(mas[i][j], end=" ")
    # log_message()
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
    log_message("\nNew Array:\n")
    for i in range(n-1):
        for j in range(n-1):
            log_message(new_mas[i][j], end=" ")
        log_message()
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
                    #  log_message(a, new_mas[i][j],"max")
                    elif (b == None and c != None):
                        new_mas[i][j] = max(a, c)
                    #  log_message(a,c, new_mas[i][j],"max")
                    elif (b != None and c == None):
                        new_mas[i][j] = max(a, b)
                    #   log_message(a,b, new_mas[i][j],"max")
                    else:
                        new_mas[i][j] = max(a, b, c)
                    #  log_message(a,b,c, new_mas[i][j],"max")
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
                    #  log_message(a, new_mas[i][j],"min")
                    elif (b == None and c != None):
                        new_mas[i][j] = min(a, c)
                    #  log_message(a,c, new_mas[i][j],"min")
                    elif (b != None and c == None):
                        new_mas[i][j] = min(a, b)
                    # log_message(a,b, new_mas[i][j],"min")
                    else:
                        new_mas[i][j] = min(a, b, c)
                    # log_message(a,b,c, new_mas[i][j],"min")

        # Izvadam ar MinMax modificetu koku.
    log_message("\nLast Array:\n")
    for i in range(n - 1):
        log_message("\n")
        for j in range(n - 1):
            log_message(new_mas[i][j])


    # i = int(input("Who styarts the game(0/1)"))
    # new_mas[index[0]][index[1]]
def gajiens():
        # e=new_mas[index[0]][index[1]+2]
        global n
        global i
        global index
        global new_mas
        if (new_mas[index[0]][index[1] + 2] == 1):

            n = n - 3
            index = (index[0] + 1, index[1] + 2)
            log_message(n)
            log_message( "-3\n")
            log_message(index)

        elif (new_mas[index[0]][index[1] + 1] == 1):
            n = n - 2
            index = (index[0] + 1, index[1] + 1)
            log_message(n )
            log_message("-2\n")
            log_message(index)

        elif (new_mas[index[0]][index[1]] == 1):

            n = n - 1
            index = (index[0] + 1, index[1])
            log_message(n)
            log_message("-1\n")
            log_message(index)


        elif (new_mas[index[0]][index[1]] == -1):

            n = n - 1
            index = (index[0] + 1, index[1])

            log_message(n)
            log_message("-1\n")
            log_message(index)


        elif (new_mas[index[0]][index[1] + 1] == -1):

            n = n - 2
            index = (index[0] + 1, index[1])
            log_message(index)
            log_message(n)
            log_message("-2\n")
        elif (new_mas[index[0]][index[1] + 2] == -1):

            n = n - 3
            index = (index[0] + 1, index[1] + 2)
            log_message(n)
            log_message("-3\n")
            log_message(index)

def gajiens2():
        # e=new_mas[index[0]][index[1]+2]
        global n
        global index
        global i
        if (new_mas[index[0]][index[1] + 2] == -1):
            n = n - 3
            index = (index[0] + 1, index[1] + 2)
            log_message(n)
            log_message("-3\n")
            log_message(index)
        elif (new_mas[index[0]][index[1] + 1] == -1):
            n = n - 2
            index = (index[0] + 1, index[1] + 1)
            log_message(n)
            log_message( "-2\n")
            log_message(index)
        elif (new_mas[index[0]][index[1]] == -1):
            n = n - 1
            index = (index[0] + 1, index[1])
            log_message(n,)
            log_message("-1\n")
            log_message(index)
        elif (new_mas[index[0]][index[1]] == 1):
            n = n - 1
            index = (index[0] + 1, index[1])
            log_message(n)
            log_message("-1")
            log_message(index)
        elif (new_mas[index[0]][index[1] + 1] == 1):
            n = n - 2
            index = (index[0] + 1, index[1])
            log_message(n)
            log_message("-2\n")
            log_message(index)
        elif (new_mas[index[0]][index[1] + 2] == 1):
            n = n - 3
            index = (index[0] + 1, index[1] + 2)
            log_message(n)
            log_message("-3\n")
            log_message(index)

def check():
        global i
        global j
        global n
        global index
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
            log_message("datorins uzvar")

        elif n < 1:
            log_message("tus zaudet")
        if ((n == 2) and (index[0]% 2 == 0)):
            log_message("tu zaude, dators -1")

def check2():
        global j
        global n
        global i
        global index
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
            log_message("tu uzvar")

        elif n < 1:
            log_message("tu zaudet")
        if ((n == 2) and (index[0] % 2 == 0)):
            log_message("tu zaudejii/dators -1 dara")

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
        log_message("1")

    elif x == 2:
        index = (index[0] + 1, index[1] + 1)
        n = n - 2
        log_message("2")

    else:
        index = (index[0] + 1, index[1] + 2)
        n = n - 3
        log_message("3")


index = (0, 0)

def button5_click():
    root = tk.Tk()
    log_message("-1")
    x=1

def button6_click():
    root = tk.Tk()
    log_message("-2")

    x=2
    log_message("start")
    global i
    global k
    global index
    j = True
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
def button7_click():
    root = tk.Tk()
    log_message("-3")
    x=3
    log_message("start")
    global i
    global k
    global index
    j = True
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
    root.destroy()
def button8_click():
    log_message("start")
    global i
    global k
    global index
    j=True
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
# Create 6 buttons and add them to the window

button4 = tk.Button(window, text="Button 4", command=button4_click)
button5 = tk.Button(window, text="Button 5", command=button5_click)
button6 = tk.Button(window, text="Button 6", command=button6_click)
button7 = tk.Button(window, text="Button 7", command=button7_click)
button8 = tk.Button(window, text="Button 8", command=button8_click)
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
button4.pack(side=tk.LEFT)
button5.pack(side=tk.LEFT)
button6.pack(side=tk.LEFT)
button7.pack(side=tk.LEFT)
button8.pack(side=tk.LEFT)


# Start the main event loop of the window
window.mainloop()






# Access the element using the index
# log_message(mas[index[0]][index[1]])  # output: 5














