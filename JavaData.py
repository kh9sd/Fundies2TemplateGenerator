from OrderedSet import OrderedSet


class JavaClass:
    def __init__(self, name, fields=None, methods=None, ancestor=None):
        """
        Constructor for JavaClass

        self.name : String
        self.fields : List of Var
        self.methods : List of Method
        self.ancestor : JavaClass
        """
        self.name = name

        if fields:
            self.fields = fields
        else:
            self.fields = []

        if methods:
            self.methods = methods
        else:
            self.methods = []

        self.ancestor = ancestor

    def get_class_template(self):
        """
        Returns list of Strings, each being a line in the class template
        """
        result = ["Fields:"]
        result.extend(("this." + field) for field in self.get_fields_temps())

        result.append("Methods:")
        result.extend(("this." + method) for method in self.get_method_temps())

        result.append("Methods for fields:")
        for field in self.get_all_fields():
            result.extend(("this." + field_method) for field_method in field.get_method_list())

        return result

    def get_all_fields(self):
        """
        Returns a set of all field Vars and inherited fields from ancestors.

        Ordered by insertion
        """
        if self.ancestor is None:
            var_set = OrderedSet()
        else:
            var_set = self.ancestor.get_all_fields()

        for field in self.fields:
            var_set.add(field)

        return var_set

    def get_all_methods(self):
        """
        Returns a set of all Methods and inherited Methods from ancestors.

        Ordered by insertion
        """
        if self.ancestor is None:
            method_set = OrderedSet()
        else:
            method_set = self.ancestor.get_all_methods()

        for method in self.methods:
            method_set.add(method)

        return method_set

    def get_fields_temps(self):
        """
        Returns list of Strings, each being a single template entry for a class field
        """
        return [field.template_entry_str() for field in self.get_all_fields()]

    def get_method_temps(self):
        """
        Returns list of Strings, each being a single template entry for a class method
        """
        return [method.template_entry_str() for method in self.get_all_methods()]

    def add_field(self, field):
        """
        Setter method for adding a field

        Parameters:
            field: Var
        """
        self.fields.append(field)

    def add_method(self, method):
        """
        Setter method for adding a method

        Parameters:
            method: Method
        """
        self.methods.append(method)

    def set_ancestor(self, anc):
        """
        Setter method for setting ancestor for class

        Parameters:
            anc: JavaClass
        """
        self.ancestor = anc

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return str(self) == str(other)


class Var:
    def __init__(self, name, t):
        self.name = name  # String
        self.type = t  # JavaClass

    def template_entry_str(self):
        """
        Returns String representation of Var in template format
        """
        return self.name + " ... " + str(self.type)

    def get_method_list(self):
        """
        Returns generator of Strings, each being a representation of a method callable on this Var
        """
        return ((self.name + "." + method_temp) for method_temp in self.type.get_method_temps())

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type

    def __hash__(self):
        return hash(str(self))


class Method:
    def __init__(self, name, r_type, paras):
        self.name = name  # String
        self.return_type = r_type  # JavaClass
        self.parameters = paras  # list of JavaClass

    def template_entry_str(self):
        """
        Returns String representation of Method in template format
        """
        return str(self) + " ... " + str(self.return_type)

    def __str__(self):
        return self.name + "(" + ", ".join(str(para) for para in self.parameters) + ")"

    def __eq__(self, other):
        return self.name == other.name and \
               self.return_type == other.return_type and \
               len(self.parameters) == len(other.parameters) and \
               all(this_para == other_para for this_para, other_para in zip(self.parameters, other.parameters))

    def __hash__(self):
        return hash(str(self))
