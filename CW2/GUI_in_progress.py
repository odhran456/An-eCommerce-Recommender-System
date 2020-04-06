import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
from recommend import top_3,name_dict,y_test
from load_usage_data import full_table


stored_username = "Tessa"


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label_username = tk.Label(self, text="Username")
        self.label_password = tk.Label(self, text="Password")

        self.entry_username = tk.Entry(self)
        self.entry_password = tk.Entry(self, show="*")

        self.label_username.grid(row=0, sticky=tk.E)
        self.label_password.grid(row=1, sticky=tk.E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.logbtn = tk.Button(self, text="Login", command=self.verify)
        self.logbtn.grid(columnspan=3)

        self.signbtn = tk.Button(self, text='Sign Up', command=lambda : controller.show_frame("PageTwo"))
        self.signbtn.grid(row=2, column=2, padx=20)

        self.exit_btn = tk.Button(self, text='Exit', command=self._exit)
        self.exit_btn.grid(row=0, column=3, padx=30)

        self.pack()

    def _exit(self):
        exit()

    def verify(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        print(username,password)
        if username == 'Deirbhile' and password == 'hunter2':
            self.controller.show_frame("PageOne")
        else:
            tk.messagebox.showerror("Login Failure","Incorrect username or password, please try again")


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        welcome_name = tk.Label(self, text='Welcome, ' + str(name_dict[y_test.values[0][0]]), font=controller.title_font)
        rec = tk.Label(self, text='Your recommended classes are:',font=controller.title_font)
        label_top_1 = tk.Label(self, text=top_3[0])
        label_top_2 = tk.Label(self, text=top_3[1])
        label_top_3 = tk.Label(self, text=top_3[2])
        welcome_name.pack(side="top", fill="x")
        rec.pack(side="top")
        label_top_1.pack(side="top", fill="x")
        label_top_2.pack(side="top", fill="x")
        label_top_3.pack(side="top", fill="x")

        his = tk.Label(self,text='Your Class History', font=controller.title_font)
        his.pack(side="top")
        logged_in_user_history = full_table.loc[full_table['Name'] == name_dict[y_test.values[0][0]]]['Class'].values

        for i in range(len(logged_in_user_history)):
            labelVar = tk.Label(self,text=logged_in_user_history[i])
            labelVar.pack(side="top")

        button = tk.Button(self, text="Logout",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(side="top")


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label_username_signup = tk.Label(self, text="Username")
        self.label_password_signup = tk.Label(self, text="Password")

        self.entry_username_signup = tk.Entry(self)
        self.entry_password_signup = tk.Entry(self, show="*")

        self.label_username_signup.grid(row=0, sticky=tk.E)
        self.label_password_signup.grid(row=1, sticky=tk.E)
        self.entry_username_signup.grid(row=0, column=1)
        self.entry_password_signup.grid(row=1, column=1)

        self.rgbtn = tk.Button(self, text="Register", command=self.log_details)
        self.rgbtn.grid(columnspan=3)

        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid()

    def log_details(self):
        username = self.entry_username_signup.get()
        password = self.entry_password_signup.get()
        print(username)
        global stored_username
        stored_username = username
        print(stored_username)
        if username:
            self.controller.show_frame("PageThree")
        else:
            tk.messagebox.showerror("Login Failure", "Incorrect username or password, please try again")


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        global stored_username
        lbl = tk.Label(self,text="Welcome, " + str(stored_username))
        lbl.grid(row=0,column=0)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
