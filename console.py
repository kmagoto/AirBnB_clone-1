#!/usr/bin/python3

# trying to build an interpreter

import cmd

class CLI(cmd.Cmd):
    prompt = "(hbnb) "
    user = input("Please enter your first name: ")
    tab = ['EOF', 'help', 'quit']
    def complete_foo(self, text, line, begidx, endidx):
        if not text:
            completions = self.tab
        else:
            completions = [f
                           for f in self.tab
                           if f.startswith(text)
                           ]
        return completions
  
    def do_EOF(self, line):
      """This should quit promter"""
      return True
    def do_quit(self, line):
      """quit the interpreter""" 
      return True 
    do_q = do_quit # shortcut for quit
    

CLI().cmdloop()
