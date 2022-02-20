from abstract_syntax_tree.basic_info_listener import BasicInfoListener
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from abstract_syntax_tree.JavaLexer import JavaLexer
from abstract_syntax_tree.JavaParser import JavaParser

def get_formatted_temp(temp_list):
    """
    Joins together list into String by new lines

    :param temp_list: Sequence
    :return: String
    """
    return "\n".join(temp_list)

if __name__ == '__main__':
    target_file_path = "C:\\Users\\kevin\\Desktop\\fundies 2 java\\EclipseWorkspace\\HW3\\src\\Strings.java"
    # target_file_path = "C:\\Users\\kevin\\Desktop\\Fundies2TemplateGenerator\\TourInfoServiceImpl.java"
    input_thing = FileStream(target_file_path)
    lexer = JavaLexer(input_thing)
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)

    walker = ParseTreeWalker()
    listener = BasicInfoListener()
    walker.walk(listener, parser.compilationUnit())

    class_dict = listener.class_dict

    # for c in class_dict:
    #     print(c)
    #
    ex_class = class_dict["ConsLoString"]
    #
    # for meth in ex_class.methods:
    #     print(meth)
    # print(ex_class.methods)
    # print(ex_class.fields[0].type)
    # print(ex_class.fields[1].type)
    # print(ex_class.fields[1].type is ex_class)

    print(get_formatted_temp(ex_class.get_class_template()))
