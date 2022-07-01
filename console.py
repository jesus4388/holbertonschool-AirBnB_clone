#!/usr/bin/python3

''' contains the entry point of the command interpreter'''

import cmd
import string, sys
from models.base_model import BaseModel
from models import storage

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

    def do_show(self, args):
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif (tokens[0] not in storage.class_list()):
            print("** class doesn't exist **")
        elif tokens[1] is None:
            print("** instance id missing **")
        else:
            x = tokens[0] + "." + tokens[1]
            dic = storage.all()
            try:
                print(dic[x])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, args):
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif (tokens[0] not in storage.class_list()):
            print("** class doesn't exist **")
        elif tokens[1] is None:
            print("** instance id missing **")
        else:
            x = tokens[0] + "." + tokens[1]
            dic = storage.all()
            try:
                del(dic[x])
            except Exception:
                print("** no instance found **")	


if __name__ == '__main__':
    HBNBCommand().cmdloop()
