#!/usr/bin/python3

''' contains the entry point of the command interpreter'''

import cmd
import string, sys
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    '''defining HBNBCommand'''
    def __init__(self):
        '''defining init'''
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_quit(self, arg):
       '''defining quit'''
       sys.exit(1)

    def help_quit(self):
        '''defining help quit'''
        print ("syntax: quit"),
        print ("-- terminates the application")

    def do_EOF(self, arg):
        '''defining EOF'''
        sys.exit(1)

    def help_EOF(self):
        '''defining help EOF'''
        print ("syntax: EOF"),
        print ("-- terminates the application")

    def do_create(self, arg):
        """
        create class name
        """
        if arg == "":
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            x = eval(arg)()
            x.save()
            print(x.id)

    def do_show(self, arg):
        if arg == "":
            print ("** class name missing **")
        elif arg != "BaseModel":
            print ("** class doesn't exist **")
        else:
            print (BaseModel.__class__.__name__)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
