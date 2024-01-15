#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Our command interpreter
    """
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User"]

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
            if obj_key in storage.all():
                print(storage.all()[obj_key])
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
            if obj_key in storage.all():
                storage.all().pop(obj_key)
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

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        """
        arg_list = arg.split()
        if arg == "":
            print("** class name missing **")
        elif arg_list[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif len(arg_list) < 3:
            print("** attribute name missing **")
        elif len(arg_list) < 4:
            print("** value missing **")
        else:
            obj_key = arg_list[0] + "." + arg_list[1]
            if obj_key in storage.all():
                setattr(
                        storage.all()[obj_key],
                        arg_list[2],
                        arg_list[3][1:-1]
                        )
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
