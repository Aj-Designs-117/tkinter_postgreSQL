from tkinter import *
import psycopg2 

root = Tk()
root.title("TkinterSQL")

def save_new_studens(name, age, adress):
    conn = psycopg2.connect(
        dbname = "postgres", 
        user = "postgres", 
        password = "@650076653", 
        host = "localhost",
        port = "5432"
    )
    cursor = conn.cursor()
    query = ''' INSERT INTO studens(name, age, adress) VALUES (%s, %s, %s) '''
    cursor.execute(query, (name, age, adress))
    print("datos guardados")
    conn.commit()
    conn.close()
    # Refresca la pantalla al agregar
    display_students()

def display_students():
    conn = psycopg2.connect(
        dbname = "postgres", 
        user = "postgres", 
        password = "@650076653", 
        host = "localhost",
        port = "5432"
    )
    cursor = conn.cursor()
    query = ''' SELECT * FROM studens '''
    cursor.execute(query)
    row = cursor.fetchall()

    list_box = Listbox(frame, width = 20, height = 10)
    list_box.grid(row = 10, columnspan = 4, sticky = W+E)

    for x in row:
        list_box.insert(END, x)

    conn.commit()
    conn.close()

def search(id):
    conn = psycopg2.connect(
        dbname = "postgres", 
        user = "postgres", 
        password = "@650076653", 
        host = "localhost",
        port = "5432"
    )
    cursor = conn.cursor()
    query = ''' SELECT * FROM studens WHERE id=%s '''
    cursor.execute(query, (id))
    row = cursor.fetchone()
    display_search_result(row)
    conn.commit()
    conn.close()

def display_search_result(row):

    list_box = Listbox(frame, width = 20, height = 1)
    list_box.grid(row = 9, columnspan = 4, sticky = W+E)
    list_box.insert(END, row)
       
# Canvas
canvas = Canvas(root, height = 380, width = 400)
canvas.pack()

frame = Frame()
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

label = Label(frame, text = "Agregar Estudiante")
label.grid(row = 0, column = 1)

# Name input
label = Label(frame, text = "Nombre")
label.grid(row = 1, column = 0)

entry_name = Entry(frame)
entry_name.grid(row = 1, column = 1)

# Age input
label = Label(frame, text = "Edad")
label.grid(row = 2, column = 0)

entry_age = Entry(frame)
entry_age.grid(row = 2, column = 1)

# Adress input
label = Label(frame, text = "Direccion")
label.grid(row = 3, column = 0)

entry_adress = Entry(frame)
entry_adress.grid(row = 3, column = 1)

button = Button(frame, text = "Agregar", command = lambda: save_new_studens(
    entry_name.get(), entry_age.get(), entry_adress.get() 
))
button.grid(row = 4, column = 1, sticky = W+E)

# SEARCH
label = Label(frame, text = "Buscar datos")
label.grid(row = 5, column = 1)

label = Label(frame, text = "Busca por el ID")
label.grid(row = 6, column = 0)

id_search = Entry(frame)
id_search.grid(row = 6, column = 1)

button = Button(frame, text = "Buscar", command = lambda: search(
    id_search.get()
))
button.grid(row = 6, column = 2)

display_students()

root.mainloop()