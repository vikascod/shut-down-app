from tkinter import *
import os

def restart():
    os.system('shutdown /r /t 1')

def logout():
    os.system('shutdown -l')

def shutdown():
    os.system('shutdown /s /t 1')
    

st = Tk()
st.title('Shut Down App')
st.geometry('400x400')
st.config(bg='red')

button_re = Button(st, text='Restart', font=('Time New Roman', 30, 'bold'), relief=RAISED, cursor='plus', command=restart)
button_re.place(x=50, y=40, height=50, width=300)

button_lg = Button(st, text='Log-out', font=('Time New Roman', 30, 'bold'), relief=RAISED, cursor='plus', command=logout)
button_lg.place(x=50, y=140, height=50, width=300)

button_st = Button(st, text='ShutDown', font=('Time New Roman', 30, 'bold'), relief=RAISED, cursor='plus', command=shutdown)
button_st.place(x=50, y=240, height=50, width=300)




st.mainloop()