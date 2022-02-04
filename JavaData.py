class JavaClass:
    def __init__(self, name, fields, methods):
        self.name = name  # string
        self.fields = fields  # Vars
        self.methods = methods  # Methods

    def get_class_template(self):
        result = ["Fields: "]
        result.extend(("this." + field.template_entry()) for field in self.fields)

        result.append("Methods: ")
        result.extend(("this." + method) for method in self.get_method_temps())

        result.append("Methods for fields: ")

        for field in self.fields:
            result.extend(("this." + field_method) for field_method in field.get_method_list())

        return result

    def get_method_temps(self):
        return (method.template_entry() for method in self.methods)

    def __str__(self):
        return self.name


class Var:
    def __init__(self, name, type):
        self.name = name  # String
        self.type = type  # JavaClass

    def template_entry(self):
        return self.name + " ... " + str(self.type)

    def get_method_list(self):
        return ((self.name + "." + method_temp_line) for method_temp_line in self.type.get_method_temps())

    def __str__(self):
        return self.name


class Method:
    def __init__(self, name, r_type, paras):
        self.name = name  # String
        self.return_type = r_type  # JavaClass
        self.parameters = paras  # JavaClasses

    def template_entry(self):
        return str(self) + " ... " + str(self.return_type)

    def __str__(self):
        return self.name + "(" + ", ".join(str(para) for para in self.parameters) + ")"
