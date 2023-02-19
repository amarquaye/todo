"""
A simple to do app written using beeware
"""
import datetime
from functools import partial
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class ToDo(toga.App):

    def startup(self):
        
        main_box = toga.Box(style=Pack(flex=1,direction=COLUMN))

        # First box 
        box1 = toga.Box(style=Pack(flex=1,padding=10,direction=COLUMN))
        # First label to serve as title
        self.lab1 = toga.Label("To Do",style=Pack(padding=5))
        # Second label to ask for name of task
        self.lab2 = toga.Label("Name of task: ")
        # Box for lab2 and taskname
        box2 = toga.Box(style=Pack(direction=ROW,flex=1,padding=5))
        # Text input to accept name of task
        self.task_name = toga.TextInput(style=Pack(flex=1,padding=(0,0,0,10)))
        # Adding lab2 and taskname to box2
        box2.add(self.lab2,self.task_name)
        # Box for taskday and addtask
        box3 = toga.Box(style=Pack(direction=ROW,flex=1,padding=5))
        # Ask user the date he wants to perform the task
        self.task_day = toga.DatePicker()
        self.task_day.min_date = datetime.date.today()
        # Button to make another box 
        self.add_task = toga.Button('Submit',style=Pack(padding=(0,0,10,10)),on_press=partial(self.display_task))
        # Adding taskday and addtask to box3
        box3.add(self.task_day,self.add_task)

        # Adding everything to box1
        box1.add(self.lab1,box2,box3)

        # Box for adding another schedule
        box4 = toga.Box(style=Pack(padding=10))
        # Creating button for another schedule
        but1 = toga.Button('+',on_press=partial(self.another_task))
        box4.add(but1)
        # Adding everything so far to mainbox
        main_box.add(box1,box4)




        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def display_task(self, widget):
        """Function to display details of task as a popup"""
        self._main_window.info_dialog('Task',message=f"Your task {self.task_name.value.title()} is scheduled for {self.task_day.value}")

    def another_task(self,widget):
        """Fuction for creating another box"""
        
     # To be continued later.



def main():
    return ToDo()
