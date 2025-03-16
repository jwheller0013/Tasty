#!/usr/bin/env  python3

import sys
import json
import os

class Tasty:
    """
    Tasty class.
    :param tasks: the user tasks
    :param important_tasks: the important user tasks
    :param complete: the completed tasks
    :param unfinished: the unfinished tasks
    :param trash: the user trash
    :param version: the Tasty version
    :param save_file: the Tasty save file
    """
    # make sure to do an __init__ method
    #Hi Angelika
    #hi

    def __init__(self):
        pass

    def main(self):
        task_list = ["Hi", "Bye"]
        while True:
            command = input("Tasty> ")
            if command == "exit":
                # exit the program, how would you do this?
                exit()
            elif command == "help":
                tasty.help()
            elif command == "license":
                tasty.license()
            elif command == "clear":
                tasty.clear()
            elif command == "tasks":
                for x in task_list:
                    print(x)
                #works but maybe should be a function just could not get one to work for it
            else:
                print("Unknown command")

    def clear(self):
        if os.name == 'nt':
            os.system('cls') #windows for clear
        else:
            os.environ['TERM'] = 'xterm' #found this needed for macOS
            os.system('clear') #Mac for clear

        #works if you run in a terminal command window does not work in PyCharm



    def help(self):

        print("Tasty Help ")
        print("What do you need help with? Tasty has all the answers.")

        print("============================================================================")
        print("help                     ->        display this message")
        print("tasks                    ->        display all your tasks")
        print("trash                    ->        display the content of the trash")
        print("new <task>               ->        add a new task")
        print("remove <task>            ->        add a task to the trash")
        print("complete <task>          ->        complete a task")
        print("unfinish <task>          ->        unfinish a task")
        print("recover <task>           ->        recover a removed task")
        print("destroy <task>           ->        remove a task from the trash")
        print("advancement              ->        see the tasks advancement")
        print("exit                     ->        exit Tasty")
        print("save                     ->        save your current tasks")
        print("load                     ->        load a save file")
        print("clear                    ->        clear the screen")




    def license(self):
        """
        Display the MIT License terms for Tasty.
        """
        print("""
Copyright (c) 2024 Tasty

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        """)




if __name__ == "__main__":
    tasty = Tasty()
    tasty.main()


#Hullo there!