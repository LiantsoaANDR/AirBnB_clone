#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Our command interpreter
    """
    prompt = "(hbnb) "
    class_list = {"BaseModel"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)"""
        if arg == "":
            print("** class name missing **")
        elif arg not in self.class_list:
            print("** class doesn't exist **")
        else:
            obj = eval(arg)()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id
        """
        arg_list = arg.split()
        if arg == "":
            print("** class name missing **")
        elif arg_list[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            obj_key = arg_list[0] + "." + arg_list[1]
            for key, value in storage.all().items():
                if key == obj_key:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        arg_list = arg.split()
        if arg == "":
            print("** class name missing **")
        elif arg_list[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            obj_key = arg_list[0] + "." + arg_list[1]
            for key, value in storage.all().items():
                if key == obj_key:
                    storage.all().pop(key)
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name
        """
        obj_rep = []
        if arg == "":
            for obj in storage.all().values():
                obj_rep.append(str(obj))
            print(obj_rep)
        elif arg in self.class_list:
            for obj in storage.all().values():
                if obj.__class__.__name__ == arg:
                    obj_rep.append(str(obj))
            print(obj_rep)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
