import unittest
from JavaData import JavaClass, Var, Method


class MyTestCase(unittest.TestCase):
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

    def test_get_class_template(self):
        self.assertEqual(self.t_conslomotif.get_class_template(), ['Fields:',
                                                                   'this.first ... IMotif',
                                                                   'this.rest ... ILoMotif',
                                                                   'Methods:',
                                                                   'this.sumDiff() ... double',
                                                                   'this.sumMotifs() ... int',
                                                                   'this.descList(boolean) ... String',
                                                                   'Methods for fields:',
                                                                   'this.first.totalDiff() ... double',
                                                                   'this.first.numMotifs() ... int',
                                                                   'this.first.motifInfo() ... String',
                                                                   'this.rest.sumDiff() ... double',
                                                                   'this.rest.sumMotifs() ... int',
                                                                   'this.rest.descList(boolean) ... String'])


if __name__ == '__main__':
    unittest.main()
