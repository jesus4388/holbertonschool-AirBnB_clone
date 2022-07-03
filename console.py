#!/usr/bin/python3
''' contains the entry point of the command interpreter'''

import cmd
import string, sys
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """""defining HBNBCommand"""

    if sys.stdin and sys.stdin.isatty():
        prompt = "(hbnb) "

    else:
        prompt = "(hbnb) \n"

    def do_quit(self, arg):
       '''Quit command to exit the program'''
       return True

    def help_quit(self):
        '''defining help quit'''
        print ("syntax: quit"),
        print ("-- terminates the application")

    def do_EOF(self, arg):
        '''EOF command to exit the program'''
        return True

    def help_EOF(self):
        '''defining help EOF'''
        print ("syntax: EOF"),
        print ("-- terminates the application")

    def emptyline(self):
        ''' Pass on empty line'''
        return
        

    def do_create(self, arg):
        """
        create class name
        """
        if not arg:
            print("** class name missing **")
            return
        elif arg != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            x = eval(arg)()
            x.save()
            print(x.id)

    def do_show(self, args):
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
            return
        elif (tokens[0] not in storage.class_list()):
            print("** class doesn't exist **")
            return
        elif len(tokens) < 2:
            print("** instance id missing **")
            return
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
            return
        elif (tokens[0] not in storage.class_list()):
            print("** class doesn't exist **")
            return
        elif len(tokens) < 2:
            print("** instance id missing **")
            return
        else:
            x = tokens[0] + "." + tokens[1]
            dic = storage.all()
            try:
                del(dic[x])
            except Exception:
                print("** no instance found **")

    def do_all(self, args):
        '# display all'
        tokens = args.split()
        objects = storage.all()
        listin = []

        if len(tokens) > 0:
            if tokens[0] not in storage.class_list():
                print("** class doesn't exist **")
                return
            for key, value in objects.items():
                if tokens[0] == value.__class__.__name__:
                    listin.append(str(value))
            print(listin)
        else:
            for key, value in objects.items():
                listin.append(str(value))
            print(listin)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
