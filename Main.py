from abstract_syntax_tree.java_file_listener import JavaFileListener
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from abstract_syntax_tree.JavaLexer import JavaLexer
from abstract_syntax_tree.JavaParser import JavaParser
from JavaData import JavaClass, Var, Method


def get_formatted_temp(temp_list):
    """
    Joins together list into String by new lines

    :param temp_list: Sequence
    :return: String
    """
    return "\n".join(temp_list)


if __name__ == "__main__":
    # target_file_path = "C:\\Users\\kevin\\Desktop\\fundies 2 java\\EclipseWorkspace\\HW3\\src\\Strings.java"
    # target_file_path = "C:\\Users\\kevin\\Desktop\\fundies 2 java\\EclipseWorkspace\\HW4\\src\\Entertainment.java"

    target_file_path = input("Where is your Java file located?\n")

    input_thing = FileStream(target_file_path)
    lexer = JavaLexer(input_thing)
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)

    walker = ParseTreeWalker()
    listener = JavaFileListener()
    walker.walk(listener, parser.compilationUnit())

    name_to_class_map = listener.class_dict
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
