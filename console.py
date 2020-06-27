#!/usr/bin/python3
"""
A module cmd that contains the entry point of the command interpreter
"""
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """
    A class HBNH interpreter command
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        A command to exit of the program
        """
        return True

    def do_EOF(self, arg):
        """
        A command to exit of the program
        """
        print()
        return True

    def emptyline(self):
        """
        A method that when an empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, arg):
        """ A command that creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in "BaseModel":
            print("** class doesn't exist **")
        else:
            new_ins = BaseModel()  #Create new instance
            new_ins.save()
            print(new_ins.id)

    def do_show(self, arg):
        """ A command that show the class name and id
        """
        list = arg.split()        
        if len(list) == 0:
            print("** class name missing **")
        elif list[0] not in "BaseModel":
            print("** class doesn't exist **")
        elif len(list) == 1:
            print("** instance id missing **")
        else:
            key ="{}.{}".format(list[0], list[1])
            temp = models.storage.all()  # temp is self.__object
            if key in temp:
                print (temp[key])
            else:
                print ("** no instance found **") 
        

            #print("** instance id missing **")
        #elif 

if __name__ == '__main__':
    HBNBCommand().cmdloop()
