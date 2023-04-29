# Importojme librarit e duhura
from tkinter import *
import string
import random
import pyperclip

def gjeneratori():
    # Llojet e shrkonjave,karaktereve etj..
    # Baza e gjenerimit
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    # Kur bashkohen te gjitha
    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    # Zgjedhja e llojit te pw
    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))


def copy():
    # Per butonin Copy per te marr pw
    random_password=passwordField.get()
    pyperclip.copy(random_password)

root=Tk()
# Hapim grafiken
root.title('Gjeneratori i fjalkalimit')
# Titulli
root.config(bg='grey')
# Ngjyra e BG
choice=IntVar()
# Integjeri i variables
Font=('arial',13,'bold')
# Lloji i shrkonjave

# Dizajnimi i butonave ne GUI me shrkonjat,ngjyrat dhe si te gjenerohet pw
passwordLabel=Label(root,text='Gjenerator fjalkalimin:',font=('times new roman',20,'bold'),bg='grey',fg='darkblue')
passwordLabel.grid(pady=10)

weakradioButton=Radiobutton(root,text='I dobet',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='Mesatar',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='I fort',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)

lengthLabel=Label(root,text='Gjatsia e fjalkalimit',font=Font,bg='grey',fg='darkblue')
lengthLabel.grid(pady=5)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5)

generateButton=Button(root,text='Gjenero',font=Font,command=gjeneratori)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid()

copyButton=Button(root,text='Merre fjalkalimin',font=Font,command=copy)
copyButton.grid(pady=5)

root.mainloop()
# Mbyllim grafiken
# IDRIZ MIRENA ME RESPEKT