from abstract_syntax_tree.JavaParserListener import JavaParserListener
from abstract_syntax_tree.JavaParser import JavaParser
from JavaData import JavaClass, Var, Method


# ★ Point 3
class JavaFileListener(JavaParserListener):
    # ★ Point 4
    def __init__(self):
        self.cur_class_name = None
        self.cur_class = None
        self.class_dict = {}


    def get_or_add_dict(self, j_type):
        if j_type not in self.class_dict:
            self.class_dict[j_type] = JavaClass(j_type)

        return self.class_dict[j_type]

    def create_var(self, ident, j_type):
        """
        creates Var object holding name and type JavaClass

        :param ident: String
        :param j_type: String
        :return: Var
        """
        return Var(ident, self.get_or_add_dict(j_type))

    def create_method(self, ident, j_type, paras_list):
        """
        Creates method with name, return type as JavaClass, and list of parameters as
        list of JavaClass

        :param ident: String
        :param j_type: String
        :return: Method
        """
        return Method(ident, self.get_or_add_dict(j_type), paras_list)

    # #★ Point 5
    # # Enter a parse tree produced by JavaParser#packageDeclaration.
    # def enterPackageDeclaration(self, ctx:JavaParser.PackageDeclarationContext):
    #     self.ast_info['packageName'] = ctx.qualifiedName().getText()
    #
    # # Enter a parse tree produced by JavaParser#importDeclaration.
    # def enterImportDeclaration(self, ctx:JavaParser.ImportDeclarationContext):
    #     import_class = ctx.qualifiedName().getText()
    #     self.ast_info['imports'].append(import_class)

    def enterInterfaceDeclaration(self, ctx:JavaParser.InterfaceDeclarationContext):
        self.cur_class_name = ctx.getChild(1).getText()
        self.cur_class = self.get_or_add_dict(self.cur_class_name)

        # size = ctx.getChildCount()
        #
        # for i in range(size - 1):  # last element is just gibberish for rest of class
        #     cur_token = ctx.getChild(i)
        #
        #     if cur_token.getText() == "class":
        #         self.cur_class_name = ctx.getChild(i + 1).getText()
        #         self.cur_class = self.get_or_add_dict(self.cur_class_name)
        #     elif cur_token.getText() == "extends":
        #         self.cur_class.set_ancestor(self.get_or_add_dict(ctx.getChild(i + 1).getText()))

    def enterInterfaceMethodDeclaration(self, ctx:JavaParser.InterfaceMethodDeclarationContext):
        # print(ctx.getChildCount())
        # print(ctx.getChild(0).getText())
        # for thing in ctx.getChildren():
        #     print(thing.getChildCount())
        #     print(thing.getText())
        #     for nested_thing in thing.getChildren():
        #         print(nested_thing.getText())
        for method in ctx.getChildren(): # have to actually iterate on the ctx to get the indiv. methods
            self.enterMethodDeclaration(method)

    # Enter a parse tree produced by JavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        method_return_type = ctx.getChild(0).getText()
        method_name = ctx.getChild(1).getText()
        para_list = self.parse_method_params_block(ctx.getChild(2))

        self.cur_class.add_method(self.create_method(method_name, method_return_type, para_list))

    # Enter a parse tree produced by JavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
        size = ctx.getChildCount()

        for i in range(size-1):  # last element is just gibberish for rest of class
            cur_token = ctx.getChild(i)

            if cur_token.getText() == "class":
                self.cur_class_name = ctx.getChild(i+1).getText()
                self.cur_class = self.get_or_add_dict(self.cur_class_name)
            elif cur_token.getText() == "extends":
                self.cur_class.set_ancestor(self.get_or_add_dict(ctx.getChild(i+1).getText()))

            # print(ctx.getChild(i).getText())

        # print("cur in ", ctx.getChild(1).getText())

        # child_count = int(ctx.getChildCount())
        # if child_count == 7:
        #     # class Foo extends Bar implements Hoge
        #     # c1 = ctx.getChild(0)  # ---> class
        #     c2 = ctx.getChild(1).getText()  # ---> class name
        #     # c3 = ctx.getChild(2)  # ---> extends
        #     c4 = ctx.getChild(3).getChild(0).getText()  # ---> extends class name
        #     # c5 = ctx.getChild(4)  # ---> implements
        #     # c7 = ctx.getChild(6)  # ---> method body
        #     self.ast_info['className'] = c2
        #     self.ast_info['implements'] = self.parse_implements_block(ctx.getChild(5))
        #     self.ast_info['extends'] = c4
        # elif child_count == 5:
        #     # class Foo extends Bar
        #     # or
        #     # class Foo implements Hoge
        #     # c1 = ctx.getChild(0)  # ---> class
        #     c2 = ctx.getChild(1).getText()  # ---> class name
        #     c3 = ctx.getChild(2).getText()  # ---> extends or implements
        #
        #     # c5 = ctx.getChild(4)  # ---> method body
        #     self.ast_info['className'] = c2
        #     if c3 == 'implements':
        #         self.ast_info['implements'] = self.parse_implements_block(ctx.getChild(3))
        #     elif c3 == 'extends':
        #         c4 = ctx.getChild(3).getChild(0).getText()  # ---> extends class name or implements class name
        #         self.ast_info['extends'] = c4
        # elif child_count == 3:
        #     # class Foo
        #     # c1 = ctx.getChild(0)  # ---> class
        #     c2 = ctx.getChild(1).getText()  # ---> class name
        #     # c3 = ctx.getChild(2)  # ---> method body
        #     self.ast_info['className'] = c2

    # Enter a parse tree produced by JavaParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:JavaParser.FieldDeclarationContext):
        field_type = ctx.getChild(0).getText()
        field_name = ctx.getChild(1).getText()

        self.cur_class.add_field(self.create_var(field_name, field_type))

    def parse_method_params_block(self, ctx):
        params_exist_check = int(ctx.getChildCount())
        result = []
        # () ---> 2
        # (Foo foo) ---> 3
        # (Foo foo, Bar bar) ---> 3
        # (Foo foo, Bar bar, int count) ---> 3
        if params_exist_check == 3:
            params_child_count = int(ctx.getChild(1).getChildCount())
            if params_child_count == 1:
                param_type = ctx.getChild(1).getChild(0).getChild(0).getText()
                param_name = ctx.getChild(1).getChild(0).getChild(1).getText()

                # param_var = self.create_var(param_name, param_type)

                result.append(self.get_or_add_dict(param_type))
            elif params_child_count > 1:
                for i in range(params_child_count):
                    if i % 2 == 0:
                        param_type = ctx.getChild(1).getChild(i).getChild(0).getText()
                        param_name = ctx.getChild(1).getChild(i).getChild(1).getText()

                        # param_var = self.create_var(param_name, param_type)

                        result.append(self.get_or_add_dict(param_type))
        return result

