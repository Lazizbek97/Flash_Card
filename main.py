from tkinter import *
from tkinter import messagebox
import json

YELLOW = "#F9F3DF"



# ---------------------------- SEARCH WEBPAGE ------------------------------- #

def search_webpage():
    
    web_page_name = website_input.get()     
    try:
        with open("user_info.json", "r") as s_file:
            data = json.load(s_file)
    except FileNotFoundError:
        messagebox.askokcancel(title = "Alert", message = "No data file found!")

        
    else:        
        if web_page_name in data.keys():
            add_pasword = messagebox.askokcancel(title = web_page_name, message = f"Email: {data[web_page_name]['Email']} \nPassword: {data[web_page_name]['Password']}")
            if add_pasword:
                pasword_input.insert(0,data[web_page_name]['Password'])
        else:
            messagebox.askokcancel(title = "Alert", message = "There is not such data")

        

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    from random import randint, choice, shuffle
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    
    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]
    
    password_list = password_letters + password_symbols + password_numbers
    
    shuffle(password_list)
    password = ''.join(password_list)
    
    
    pasword_input.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():
    
    web_page_name = website_input.get()
    email_name = email_input.get()
    password_name = pasword_input.get()
    
    new_data = {
        web_page_name: {
            "Email": email_name,
            "Password": password_name}
        }
   
    if web_page_name != "" and password_name != "":
        is_ok = messagebox.askokcancel(title = "Note!", message = f"These are the details entered:\nEmail: {email_name} \nPassword: {password_name}")
        
        if is_ok:
            try: 
                with open("user_info.json", "r") as data_file:
                    #filedagi malumotlarni dataga saqla(ol)
                    data = json.load(data_file)
                    #olingan malumotlarni yangila
                    data.update(new_data)
            except FileNotFoundError:
                with open("user_info.json", "w") as file:
                    #yangilanayotgan dataga yangi malumotni qoshib ket
                    json.dump(new_data, file, indent = 4)
            else:
                with open("user_info.json", "w") as file:
                    #yangilanayotgan dataga yangi malumotni qoshib ket
                    json.dump(data, file, indent = 4)
            finally:       
                website_input.delete(0, END)
                pasword_input.delete(0, END)
                    
                    
                
    else:
        messagebox.askokcancel(title = "Alert", message = "Please, don't leave any feilds empty!")

    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx = 50, pady = 50, bg = YELLOW)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
logo_image = PhotoImage(file = "logo.png")
canvas.create_image(100,122,image = logo_image)
canvas.grid(column = 1, row = 0)

website = Label(text ="Website:", bg = YELLOW)
website.grid(column = 0, row =1)

email = Label(text = "Email/Username:", bg = YELLOW)
email.grid(column = 0, row =2)

pasword = Label(text = "Password:", bg = YELLOW)
pasword.grid(column = 0, row =3)

website_input = Entry(width = 21, bg = YELLOW)
website_input.grid(column = 1, row = 1)
website_input.focus()

email_input = Entry(width = 36, bg = YELLOW)
email_input.grid(row = 2, column = 1, columnspan =2)
email_input.insert(0, "laziz.fayziev@mail.ru")

pasword_input = Entry(width = 21, bg = YELLOW)
pasword_input.grid(column = 1, row =3)

search_but = Button(text = "Search", width = 14, bg = "#B8DFD8", command = search_webpage)
search_but.grid(column = 2, row = 1)

generate_but = Button(text = "Generate Password", bg = "#B8DFD8", command = password_generator)
generate_but.grid(column = 2, row = 3)

add_but = Button(text = "Add", width = 36,bg = "#B8DFD8", command = save_to_file)
add_but.grid(row = 4, column = 1, columnspan =2)

window.mainloop()





























