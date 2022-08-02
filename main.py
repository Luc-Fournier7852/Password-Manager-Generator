from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


nr_letters= random.randint(8,10)
nr_symbols = random.randint(2,4)
nr_numbers = random.randint(2,4)

password = ['']
char = 0
sym = 0
num = 0
rand = 0


def generate_password():
    final_pass = ['']
    for n in range(0,nr_letters):
        n = random.randint(0,len(letters)-1)
        char = letters[n]
        password.append(char)

    for n in range(0,nr_symbols):
        n = random.randint(0,len(symbols)-1)
        sym = symbols[n]
        password.append(sym)

    for n in range(0,nr_numbers):
        n = random.randint(0,len(numbers)-1)
        num = numbers[n]
        password.append(num)


    for n in range(0,len(password)):
        n = random.randint(0,len(password)-1)
        rand = password.pop(n)
        final_pass.append(rand)

    final_pass = ''.join(str(x) for x in final_pass)
    password_input.delete(0,END)
    password_input.insert(0,final_pass)
    pyperclip.copy(final_pass)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website=website_input.get()
    email =email_input.get()
    password=password_input.get()
    if len(password) ==0 or len(email)==0 or len(website)==0:
        messagebox.askretrycancel(title="Oops",message="One or more entry fields are missing\nPlease retry")
        return
    is_ok = messagebox.askokcancel(title="Confirm", message=f"These are the details entered\nEmail: {email}\nPassword: {password}\nWould you like to proceed?")
    if is_ok:
        with open("save_data.txt",mode="a") as file:
            file.write(f"{website}||{email}||{password}\n")
        website_input.delete(0,END)
        password_input.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200,highlightthickness=0)
bg_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=bg_img)
canvas.grid(row=0,column=1)


#LABELS
website_label = Label(text= "Website:", font= ("SF Pro",11))
website_label.grid(row=1,column=0)

email_label=Label(text="Emial/Username:",font= ("SF Pro",11))
email_label.grid(row=2,column=0)

password_label=Label(text="Password:",font= ("SF Pro",11))
password_label.grid(row=3,column=0)

#Entries
website_input=Entry(width= 50)
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus()

email_input=Entry(width= 50)
email_input.grid(row=2,column=1,columnspan=2)
#email_input.insert(0,"lucon@live.ca")

password_input=Entry(width= 32)
password_input.grid(row=3,column=1)


#Buttons
generate=Button(text="Generate Password",command=generate_password)
generate.grid(row=3,column=2)

add=Button(text="Add",width=43,command=add_password)
add.grid(row=4,column=1,columnspan=2)




window.mainloop()