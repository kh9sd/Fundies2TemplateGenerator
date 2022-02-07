# we need a hashmap from string name to JavaClasses
from JavaData import JavaClass, Var, Method
from enum import Enum


class Category(Enum):
    CLASS = 0
    FIELD = 1
    CONSTRUCTOR = 2
    METHOD = 3


def get_trimmed_name(name, class_name):
    return name[len(class_name) + 1:]


def process_str_to_method(s):
    """
    [desc]

    :param s: String
    :return: 2-tuple of String, String
    """
    name, paras, _ = s.replace(")", "(").split("(")

    return name, paras


def find_category(input_str):
    match len(input_str.split("(")):
        case 1:  # either class name or field
            name = input_str
            match len(name.split()):
                case 1:
                    return Category.CLASS
                case 2:
                    return Category.FIELD

        case 2:  # method, have to ignore constructors
            name, _ = input_str.split("(")
            class_name, method_name = name.split(".")

            if class_name == method_name:
                return Category.CONSTRUCTOR
            return Category.METHOD

    raise(ValueError("Line '{input_str}' is not a valid input"))


def parse_input_file(location):
    def add_if_not_in_dict(j_type):
        """
        [desc]

        :param j_type:
        :return: JavaClass
        """
        nonlocal str_class_dict

        if j_type not in str_class_dict:
            str_class_dict[j_type] = JavaClass(j_type)

        return str_class_dict[j_type]

    def create_var(ident, j_type):
        """
        [desc]

        :param ident: String
        :param j_type: String
        :return: Var
        """
        return Var(ident, add_if_not_in_dict(j_type))

    def create_para_list(paras):
        """
        [desc]

        :param paras: String, formatted like "boolean, IMotif, int"
        :return: list of JavaClass
        """
        return [add_if_not_in_dict(para.strip()) for para in paras.split(",")]

    def create_method(ident, j_type):
        """
        [desc]

        :param ident: String
        :param j_type: String
        :return: Method
        """
        name, paras = process_str_to_method(ident)
        return Method(name, add_if_not_in_dict(j_type), create_para_list(paras))

    str_class_dict = {}

    with open(location, "r") as f:
        for line in f:
            match find_category(line):
                case Category.CLASS:
                    cur_class_name = line.strip()
                    cur_class = add_if_not_in_dict(cur_class_name)

                    print("On new class:", cur_class_name)

                case Category.FIELD:
                    identifier, j_class = line.split()
                    identifier = get_trimmed_name(identifier, cur_class_name)

                    cur_class.add_field(create_var(identifier, j_class))

                case Category.METHOD:
                    identifier, j_class = line.rsplit(sep=None, maxsplit=1)
                    identifier = get_trimmed_name(identifier, cur_class_name)

                    cur_class.add_method(create_method(identifier, j_class))
                case Category.CONSTRUCTOR:
                    pass

    return str_class_dict


def get_formatted_temp(temp_list):
    return "\n".join(temp_list)


if __name__ == "__main__":
    INPUT_FILE_LOC = "inputfile.txt"

    print(f"Now reading data from {INPUT_FILE_LOC}")
    name_to_class_map = parse_input_file(INPUT_FILE_LOC)
    print("Done reading!")

    # print(name_to_class_map)
    # print(get_formatted_template(name_to_class_map["ILoMotif"]))
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
            para_class = input("\nWhat class is your variable?\n").strip()

            if para_class in name_to_class_map:
                var_name = input("\nWhat is the name of your variable?\n")
                print(get_formatted_temp(name_to_class_map[para_class].custom_var_temp(var_name)))
            else:
                print("Invalid class name, returning to start\n")

        else:
            print("\nInvalid option, try again")


    # print(get_formatted_template(name_to_class_map["ConsLoMotif"]))
