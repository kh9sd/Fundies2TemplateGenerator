# we need a hashmap from string name to JavaClasses
from JavaData import JavaClass, Var, Method
from enum import Enum


class Category(Enum):
    CLASS = 0
    FIELD = 1
    CONSTRUCTOR = 2
    METHOD = 3


def get_trimmed_name(name, class_name):
    """
    Gets trimmed name like "IMotif.first" and class name "IMotif"
    and returns "first"

    :param name: String
    :param class_name: String
    :return: String
    """
    return name[len(class_name) + 1:]


def process_method_str(s):
    """
    Gets input like bruh(Boolean, IMotif)
    and outputs "bruh", "Boolean, IMotif"

    :param s: String
    :return: 2-tuple of String, String
    """
    name, paras, _ = s.replace(")", "(").split("(")

    return name, paras


def find_category(input_str):
    """
    Gets raw line from input file and determines whether it is
    a class, field, constructor, or method

    :param input_str: String
    :return: enumeration of Category
    """
    par_splits = input_str.split("(")
    if len(par_splits) == 1:  # either class name or field
        if "." not in input_str:
            return Category.CLASS
        else:
            return Category.FIELD

    elif len(par_splits) == 2:  # method, have to ignore constructors
        name, _ = par_splits
        class_name, method_name = name.split(".")

        if class_name == method_name:
            return Category.CONSTRUCTOR
        return Category.METHOD

    raise(ValueError("Line '{input_str}' is not a valid input"))


def parse_input_file(location):
    """
    Reads text file and produces finished dict containing
    all JavaClasses with inner structures

    :param location: String
    :return: dict(String, JavaClass)
    """
    def get_from_dict_always(j_type):
        """
        Returns JavaClass object corresponding to string in str_class_dict

        SIDE EFFECT: If not in dict, adds to dict keyed by class name

        :param j_type:
        :return: JavaClass
        """
        nonlocal str_class_dict

        if j_type not in str_class_dict:
            str_class_dict[j_type] = JavaClass(j_type)

        return str_class_dict[j_type]

    def create_var(ident, j_type):
        """
        creates Var object holding name and type JavaClass

        :param ident: String
        :param j_type: String
        :return: Var
        """
        return Var(ident, get_from_dict_always(j_type))

    def create_para_list(paras):
        """
        creates list of JavaClass from inputted String

        :param paras: String, formatted like "boolean, IMotif, int"
        :return: list of JavaClass
        """
        return [get_from_dict_always(para.strip()) for para in paras.split(",")]

    def create_method(ident, j_type):
        """
        Creates method with name, return type as JavaClass, and list of parameters as
        list of JavaClass

        :param ident: String
        :param j_type: String
        :return: Method
        """
        name, paras = process_method_str(ident)
        return Method(name, get_from_dict_always(j_type), create_para_list(paras))

    str_class_dict = {}

    with open(location, "r") as f:
        for line in f:
            line = line.strip()
            cat = find_category(line)

            if cat == Category.CLASS:
                cur_class_name, *rest = line.split()
                cur_class = get_from_dict_always(cur_class_name)

                if rest:
                    cur_class.set_ancestor(get_from_dict_always(rest[0]))

                print("On new class:", cur_class_name)

            elif cat == Category.FIELD:
                identifier, j_class = line.split()
                identifier = get_trimmed_name(identifier, cur_class_name)

                cur_class.add_field(create_var(identifier, j_class))

            elif cat == Category.METHOD:
                identifier, j_class = line.rsplit(sep=None, maxsplit=1)
                identifier = get_trimmed_name(identifier, cur_class_name)

                cur_class.add_method(create_method(identifier, j_class))

            elif cat == Category.CONSTRUCTOR:
                pass

    return str_class_dict


def get_formatted_temp(temp_list):
    """
    Joins together list into String by new lines

    :param temp_list: Sequence
    :return: String
    """
    return "\n".join(temp_list)


if __name__ == "__main__":
    INPUT_FILE_LOC = "inputfile.txt"

    print(f"Now reading data from {INPUT_FILE_LOC}")
    name_to_class_map = parse_input_file(INPUT_FILE_LOC)
    print("Done reading, all detected classes (including builtins) are:")

    for c_name in name_to_class_map:
        print(c_name)

    while True:
        choice = input("\nEnter 'c' to get a template for a class, "
                       "enter 'p' to get a template for a method parameter\n").lower()

        if choice == "c":
            target_class = input("\nWhat class would you like a template for?\n").strip()

            if target_class in name_to_class_map:
                print(get_formatted_temp(name_to_class_map[target_class].get_class_template()))
            else:
                print("Invalid class name, returning to start\n")

        elif choice == "p":
            input_class = input("\nWhat class is your variable?\n").strip()

            if input_class in name_to_class_map:
                var_class = name_to_class_map[input_class]
                var_name = input("\nWhat is the name of your variable?\n")

                new_var = Var(var_name, var_class)
                print(get_formatted_temp(new_var.get_method_list()))
            else:
                print("Invalid class name, returning to start\n")

        else:
            print("\nInvalid option, try again")
