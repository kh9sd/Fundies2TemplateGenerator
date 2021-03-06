from Main import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_get_trimmed_name(self):
        self.assertEqual(get_trimmed_name("ILoMotif.descList(boolean)", "ILoMotif"), "descList(boolean)")
        self.assertEqual(get_trimmed_name("ConsLoMotif.sumDiff()", "ConsLoMotif"), "sumDiff()")
        self.assertEqual(get_trimmed_name("ConsLoMotif.first", "ConsLoMotif"), "first")

    def test_str_to_method(self):
        self.assertEqual(process_method_str("descList(boolean)"),
                         ("descList", "boolean"))
        self.assertEqual(process_method_str("sumMotifs()"),
                         ("sumMotifs", ""))
        self.assertEqual(process_method_str("sumMotifs(amongus, int, sus)"),
                         ("sumMotifs", "amongus, int, sus"))

    def test_find_category(self):
        self.assertEqual(find_category("ILoMotif"), Category.CLASS)
        self.assertEqual(find_category("ILoMotif Bruh"), Category.CLASS)
        self.assertEqual(find_category("ConsLoMotif.first IMotif"), Category.FIELD)
        self.assertEqual(find_category("ConsLoMotif.ConsLoMotif(IMotif, ILoMotif)"), Category.CONSTRUCTOR)
        self.assertEqual(find_category("ConsLoMotif.ConsLoMotif()"), Category.CONSTRUCTOR)
        self.assertEqual(find_category("ConsLoMotif.sumDiff() double"), Category.METHOD)
        self.assertEqual(find_category("ConsLoMotif.sumDiff(boolean) double"), Category.METHOD)
        self.assertEqual(find_category("ConsLoMotif.sumDiff(boolean, amongus, waaa) double"), Category.METHOD)

    def test_get_formatted_template(self):
        t_double = JavaClass("double", [], [])
        t_int = JavaClass("int", [], [])
        t_String = JavaClass("String", [], [])
        t_boolean = JavaClass("boolean", [], [])

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

        self.assertEqual(get_formatted_temp(t_conslomotif.get_class_template()),
"""Fields:
this.first ... IMotif
this.rest ... ILoMotif
Methods:
this.sumDiff() ... double
this.sumMotifs() ... int
this.descList(boolean) ... String
Methods for fields:
this.first.totalDiff() ... double
this.first.numMotifs() ... int
this.first.motifInfo() ... String
this.rest.sumDiff() ... double
this.rest.sumMotifs() ... int
this.rest.descList(boolean) ... String""")

    def test_get_template_with_parse(self):
        class_dict = parse_input_file("tester_text_input1.txt")

        self.assertEqual(get_formatted_temp(class_dict["Spaceship"].get_class_template()),
"""Fields:
this.loc ... Location
this.color ... Color
this.speed ... int
Methods:
this.move(int, int) ... IGamePiece
this.draw() ... WorldImage
Methods for fields:
this.loc.moveLocation(int, int) ... Location""")




if __name__ == '__main__':
    unittest.main()
