#!/usr/bin/python3

''' contains the entry point of the command interpreter'''

import cmd
import string, sys


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
