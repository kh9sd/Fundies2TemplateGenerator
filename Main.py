# we need a hashmap from string name to JavaClasses
from JavaData import JavaClass, Var, Method


def is_field(ident):
    return ident[-1] != ")"  # surprisingly still works if length lower than 1


def is_constructor(method_name):  # assumes method_name is a method
    raw_name, _ = method_name.split("(")
    class_name, name = raw_name.split(".")

    return class_name == name


def process_str_to_method(s):
    raw_name, paras, _ = s.replace(")", "(").split("(")
    __, name = raw_name.split(".")

    return name, paras


def parse_input_text(location):
    def create_var(ident, j_type):
        nonlocal str_class_dict

        if j_type in str_class_dict:
            return Var(ident, str_class_dict[j_type])
        else:
            str_class_dict[j_type] = JavaClass(j_type)
            return Var(ident, str_class_dict[j_type])

    def create_method(ident, j_type):
        nonlocal str_class_dict
        name, paras = process_str_to_method(ident)

    str_class_dict = {}

    with open(location, "r") as f:
        for line in f:
            line_data = line.strip().split()

            if len(line_data) == 1:  # one element, aka new class start
                curr_class = line_data

            elif len(line_data) == 2:  # the usual, field or method
                identifier, j_class = line_data

                if is_field(identifier):
                    create_var(identifier, j_class)
                else:
                    if not is_constructor(identifier):
                        create_method(identifier, j_class)

            else:
                raise(ValueError(f"Argument {line_data}, is not proper form for reading"))
            print(line_data)


if __name__ == "__main__":
    INPUT_FILE_LOC = "inputfile.txt"

    print(f"Now reading data from {INPUT_FILE_LOC}")
    parse_input_text(INPUT_FILE_LOC)
    print("Done reading!")

    name_to_class_map = {}

    t_double = JavaClass("double", [], [])
    t_int = JavaClass("int", [], [])
    t_String = JavaClass("String", [], [])
    t_boolean = JavaClass("boolean",  [], [])

    f_sum_diff = Method("sumDiff", t_double, [])
    f_sum_motifs = Method("sumMotifs", t_int, [])
    f_desc_list = Method("descList", t_String, [t_boolean])

    f_total_diff = Method("totalDiff", t_double, [])
    f_num_motifs = Method("numMotifs", t_int, [])
    f_motif_info = Method("motifInfo", t_String, [])

    t_imotif = JavaClass("IMotif", [], [f_total_diff,
                                        f_num_motifs,
                                        f_motif_info])
    t_ilomotif = JavaClass("ILoMotif", [], [f_sum_diff,
                                            f_sum_motifs,
                                            f_desc_list])

    t_conslomotif = JavaClass("ConsLoMotif", [Var("first", t_imotif),
                                              Var("rest", t_ilomotif)]
                                           , [f_sum_diff,
                                              f_sum_motifs,
                                              f_desc_list])

    # print("\n".join(t_conslomotif.get_class_template()))


