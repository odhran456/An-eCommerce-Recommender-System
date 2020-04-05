import tkinter as tk
from tkinter import font as tkfont
from recommend import top_3,name_dict,y_test
from load_usage_data import full_table


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
        for F in (StartPage, PageOne, PageTwo):
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

        self.logbtn = tk.Button(self, text="Login", command=lambda: controller.show_frame("PageOne"))
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
        return username


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
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
