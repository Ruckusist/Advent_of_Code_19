import math, time, copy, os
import threading
from timeit import default_timer as timer


class Int_Code_Comp(object):
    """FINISHED AND WORKING... just run main()"""
    def __init__(self, config=None, manual_input=True):
        # print("Initializing Int Code Computer Ver. day.13")
        self.config = config
        self.manual_input = manual_input
        self.pointer = 0
        self.input = 0
        self.ram = 0
        self.simple = [104,424242,99]
        self.day2 = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,9,19,23,2,23,10,27,1,6,27,31,1,31,6,35,2,35,10,39,1,39,5,43,2,6,43,47,2,47,10,51,1,51,6,55,1,55,6,59,1,9,59,63,1,63,9,67,1,67,6,71,2,71,13,75,1,75,5,79,1,79,9,83,2,6,83,87,1,87,5,91,2,6,91,95,1,95,9,99,2,6,99,103,1,5,103,107,1,6,107,111,1,111,10,115,2,115,13,119,1,119,6,123,1,123,2,127,1,127,5,0,99,2,14,0,0]
        self.test = [[104,1125899906842624,99], [1102,34915192,34915192,7,4,7,99,0], [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]]
        self.TEST = [3,225,1,225,6,6,1100,1,238,225,104,0,101,14,135,224,101,-69,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,102,90,169,224,1001,224,-4590,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1102,90,45,224,1001,224,-4050,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,1001,144,32,224,101,-72,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,36,93,225,1101,88,52,225,1002,102,38,224,101,-3534,224,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1102,15,57,225,1102,55,49,225,1102,11,33,225,1101,56,40,225,1,131,105,224,101,-103,224,224,4,224,102,8,223,223,1001,224,2,224,1,224,223,223,1102,51,39,225,1101,45,90,225,2,173,139,224,101,-495,224,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1101,68,86,224,1001,224,-154,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,344,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,359,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,374,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,389,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,404,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,419,101,1,223,223,1007,677,226,224,1002,223,2,223,1006,224,434,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,449,101,1,223,223,8,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,479,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,677,677,224,102,2,223,223,1006,224,509,101,1,223,223,1008,677,677,224,102,2,223,223,1005,224,524,1001,223,1,223,107,226,226,224,1002,223,2,223,1005,224,539,101,1,223,223,7,226,226,224,102,2,223,223,1005,224,554,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,569,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,584,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,108,226,226,224,1002,223,2,223,1005,224,614,101,1,223,223,1008,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,644,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,659,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226]
        self.BOOST = [1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,0,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1101,0,38,1019,1102,1,37,1008,1101,252,0,1023,1102,24,1,1004,1102,35,1,1017,1101,0,28,1011,1101,0,36,1003,1102,30,1,1013,1101,0,0,1020,1102,1,1,1021,1102,897,1,1028,1101,20,0,1000,1101,0,22,1005,1102,29,1,1007,1101,0,34,1009,1102,1,259,1022,1101,310,0,1025,1102,892,1,1029,1101,21,0,1014,1102,1,315,1024,1101,0,33,1002,1102,31,1,1015,1102,190,1,1027,1102,1,39,1001,1101,26,0,1010,1101,27,0,1016,1102,1,23,1018,1101,0,32,1012,1101,0,25,1006,1102,1,197,1026,109,34,2106,0,-7,1001,64,1,64,1106,0,199,4,187,1002,64,2,64,109,-22,2108,34,-3,63,1005,63,221,4,205,1001,64,1,64,1106,0,221,1002,64,2,64,109,-10,1208,-1,42,63,1005,63,237,1106,0,243,4,227,1001,64,1,64,1002,64,2,64,109,20,2105,1,1,1001,64,1,64,1105,1,261,4,249,1002,64,2,64,109,1,21108,40,40,-6,1005,1017,283,4,267,1001,64,1,64,1105,1,283,1002,64,2,64,109,7,1205,-9,301,4,289,1001,64,1,64,1105,1,301,1002,64,2,64,109,-1,2105,1,-5,4,307,1106,0,319,1001,64,1,64,1002,64,2,64,109,-8,1206,0,331,1105,1,337,4,325,1001,64,1,64,1002,64,2,64,109,-6,21108,41,38,0,1005,1015,353,1105,1,359,4,343,1001,64,1,64,1002,64,2,64,109,11,1206,-6,377,4,365,1001,64,1,64,1106,0,377,1002,64,2,64,109,1,21101,42,0,-8,1008,1019,42,63,1005,63,399,4,383,1105,1,403,1001,64,1,64,1002,64,2,64,109,-29,1202,6,1,63,1008,63,24,63,1005,63,425,4,409,1106,0,429,1001,64,1,64,1002,64,2,64,109,14,1201,-3,0,63,1008,63,34,63,1005,63,451,4,435,1105,1,455,1001,64,1,64,1002,64,2,64,109,10,21101,43,0,-9,1008,1013,41,63,1005,63,475,1106,0,481,4,461,1001,64,1,64,1002,64,2,64,109,-17,2101,0,0,63,1008,63,21,63,1005,63,501,1106,0,507,4,487,1001,64,1,64,1002,64,2,64,109,-5,2107,21,5,63,1005,63,525,4,513,1105,1,529,1001,64,1,64,1002,64,2,64,109,13,1202,-7,1,63,1008,63,26,63,1005,63,553,1001,64,1,64,1106,0,555,4,535,1002,64,2,64,109,5,21107,44,45,-8,1005,1010,573,4,561,1105,1,577,1001,64,1,64,1002,64,2,64,109,-6,21102,45,1,7,1008,1019,45,63,1005,63,603,4,583,1001,64,1,64,1105,1,603,1002,64,2,64,109,-15,1207,10,28,63,1005,63,623,1001,64,1,64,1106,0,625,4,609,1002,64,2,64,109,8,2108,37,-4,63,1005,63,645,1001,64,1,64,1105,1,647,4,631,1002,64,2,64,109,6,21102,46,1,1,1008,1012,44,63,1005,63,671,1001,64,1,64,1106,0,673,4,653,1002,64,2,64,109,4,1207,-6,35,63,1005,63,695,4,679,1001,64,1,64,1106,0,695,1002,64,2,64,109,1,2107,38,-8,63,1005,63,715,1001,64,1,64,1105,1,717,4,701,1002,64,2,64,109,-23,1208,10,36,63,1005,63,739,4,723,1001,64,1,64,1105,1,739,1002,64,2,64,109,4,2102,1,7,63,1008,63,24,63,1005,63,765,4,745,1001,64,1,64,1105,1,765,1002,64,2,64,109,13,2102,1,-4,63,1008,63,22,63,1005,63,789,1001,64,1,64,1105,1,791,4,771,1002,64,2,64,109,-8,1201,5,0,63,1008,63,32,63,1005,63,811,1106,0,817,4,797,1001,64,1,64,1002,64,2,64,109,11,1205,7,829,1105,1,835,4,823,1001,64,1,64,1002,64,2,64,109,-1,2101,0,-6,63,1008,63,25,63,1005,63,857,4,841,1106,0,861,1001,64,1,64,1002,64,2,64,109,8,21107,47,46,-9,1005,1011,877,1106,0,883,4,867,1001,64,1,64,1002,64,2,64,109,9,2106,0,-1,4,889,1106,0,901,1001,64,1,64,4,64,99,21101,0,27,1,21102,915,1,0,1105,1,922,21201,1,59500,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,0,942,0,1105,1,922,21201,1,0,-1,21201,-2,-3,1,21101,0,957,0,1105,1,922,22201,1,-1,-2,1105,1,968,21201,-2,0,-2,109,-3,2105,1,0]
        self.paint = [3,8,1005,8,299,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,28,1006,0,85,1,106,14,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,58,1,1109,15,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,84,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,105,1006,0,48,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,130,1006,0,46,1,1001,17,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,160,2,109,20,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,185,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,207,1006,0,89,2,1002,6,10,1,1007,0,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,241,2,4,14,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,267,1,1107,8,10,1,109,16,10,2,1107,4,10,101,1,9,9,1007,9,1003,10,1005,10,15,99,109,621,104,0,104,1,21101,0,387239486208,1,21102,316,1,0,1106,0,420,21101,0,936994976664,1,21102,327,1,0,1105,1,420,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,1,29192457307,1,21102,1,374,0,1106,0,420,21101,0,3450965211,1,21101,0,385,0,1106,0,420,3,10,104,0,104,0,3,10,104,0,104,0,21102,1,837901103972,1,21101,408,0,0,1106,0,420,21102,867965752164,1,1,21101,0,419,0,1105,1,420,99,109,2,22102,1,-1,1,21102,40,1,2,21102,451,1,3,21102,1,441,0,1106,0,484,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,446,447,462,4,0,1001,446,1,446,108,4,446,10,1006,10,478,1102,0,1,446,109,-2,2105,1,0,0,109,4,1201,-1,0,483,1207,-3,0,10,1006,10,501,21101,0,0,-3,22101,0,-3,1,22102,1,-2,2,21101,1,0,3,21101,520,0,0,1106,0,525,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,548,2207,-4,-2,10,1006,10,548,21201,-4,0,-4,1105,1,616,22101,0,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,0,567,0,1106,0,525,22101,0,1,-4,21101,1,0,-1,2207,-4,-2,10,1006,10,586,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,608,21202,-1,1,1,21102,608,1,0,106,0,483,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]
        self.arcade = [2,380,379,385,1008,2617,649812,381,1005,381,12,99,109,2618,1101,0,0,383,1102,1,0,382,21001,382,0,1,21002,383,1,2,21102,37,1,0,1106,0,578,4,382,4,383,204,1,1001,382,1,382,1007,382,43,381,1005,381,22,1001,383,1,383,1007,383,23,381,1005,381,18,1006,385,69,99,104,-1,104,0,4,386,3,384,1007,384,0,381,1005,381,94,107,0,384,381,1005,381,108,1105,1,161,107,1,392,381,1006,381,161,1101,-1,0,384,1105,1,119,1007,392,41,381,1006,381,161,1101,0,1,384,21001,392,0,1,21101,0,21,2,21102,0,1,3,21102,1,138,0,1106,0,549,1,392,384,392,21001,392,0,1,21102,21,1,2,21102,1,3,3,21102,161,1,0,1105,1,549,1101,0,0,384,20001,388,390,1,20101,0,389,2,21102,1,180,0,1106,0,578,1206,1,213,1208,1,2,381,1006,381,205,20001,388,390,1,20101,0,389,2,21102,205,1,0,1105,1,393,1002,390,-1,390,1102,1,1,384,21002,388,1,1,20001,389,391,2,21101,228,0,0,1105,1,578,1206,1,261,1208,1,2,381,1006,381,253,20102,1,388,1,20001,389,391,2,21102,1,253,0,1105,1,393,1002,391,-1,391,1101,0,1,384,1005,384,161,20001,388,390,1,20001,389,391,2,21101,0,279,0,1106,0,578,1206,1,316,1208,1,2,381,1006,381,304,20001,388,390,1,20001,389,391,2,21101,304,0,0,1106,0,393,1002,390,-1,390,1002,391,-1,391,1101,0,1,384,1005,384,161,20102,1,388,1,21002,389,1,2,21102,0,1,3,21101,0,338,0,1105,1,549,1,388,390,388,1,389,391,389,21002,388,1,1,20102,1,389,2,21102,4,1,3,21101,0,365,0,1106,0,549,1007,389,22,381,1005,381,75,104,-1,104,0,104,0,99,0,1,0,0,0,0,0,0,361,19,18,1,1,21,109,3,21201,-2,0,1,22101,0,-1,2,21101,0,0,3,21101,0,414,0,1106,0,549,21201,-2,0,1,22102,1,-1,2,21102,429,1,0,1105,1,601,2102,1,1,435,1,386,0,386,104,-1,104,0,4,386,1001,387,-1,387,1005,387,451,99,109,-3,2106,0,0,109,8,22202,-7,-6,-3,22201,-3,-5,-3,21202,-4,64,-2,2207,-3,-2,381,1005,381,492,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,481,21202,-4,8,-2,2207,-3,-2,381,1005,381,518,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,507,2207,-3,-4,381,1005,381,540,21202,-4,-1,-1,22201,-3,-1,-3,2207,-3,-4,381,1006,381,529,21202,-3,1,-7,109,-8,2105,1,0,109,4,1202,-2,43,566,201,-3,566,566,101,639,566,566,1202,-1,1,0,204,-3,204,-2,204,-1,109,-4,2106,0,0,109,3,1202,-1,43,593,201,-2,593,593,101,639,593,593,21002,0,1,-2,109,-3,2106,0,0,109,3,22102,23,-2,1,22201,1,-1,1,21101,0,499,2,21101,0,275,3,21101,0,989,4,21101,630,0,0,1105,1,456,21201,1,1628,-2,109,-3,2105,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,2,2,2,0,2,2,2,2,2,2,0,2,2,0,2,2,2,2,2,0,2,0,2,2,0,0,0,0,2,2,2,2,2,0,0,0,2,2,0,1,1,0,0,0,0,0,0,2,0,2,0,2,2,0,2,0,0,2,0,2,2,2,0,2,2,2,2,0,2,0,2,2,2,2,2,0,2,0,2,2,2,0,1,1,0,2,0,2,0,0,2,2,0,2,0,2,2,2,2,2,0,2,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,2,0,2,2,2,2,2,0,1,1,0,2,2,2,2,2,0,2,2,2,2,2,0,2,2,2,2,2,2,0,0,0,0,2,2,0,0,0,2,2,2,0,0,0,0,2,0,0,2,0,0,1,1,0,2,2,2,2,0,0,2,2,2,2,2,2,2,0,0,0,0,2,0,2,2,2,2,0,0,2,0,0,2,0,0,2,2,2,2,0,0,2,2,0,1,1,0,2,2,2,0,2,2,0,0,2,2,0,2,2,2,0,0,2,0,2,2,0,2,0,2,2,2,2,2,2,0,2,2,2,2,2,2,0,2,2,0,1,1,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,0,0,0,2,2,2,2,0,2,2,2,2,0,2,2,2,2,2,2,0,1,1,0,0,0,0,2,0,2,2,0,2,2,2,0,0,0,2,0,0,2,0,2,0,2,2,2,0,2,0,2,2,2,2,2,2,0,2,2,0,2,0,0,1,1,0,2,2,2,2,2,0,2,0,0,2,0,2,2,0,2,0,2,2,2,0,2,2,2,0,2,0,0,2,0,2,2,0,2,0,2,0,2,2,2,0,1,1,0,2,2,2,0,0,2,2,2,2,0,2,0,0,0,2,0,0,2,2,2,0,0,2,0,2,0,2,2,2,2,0,2,0,2,0,2,0,0,2,0,1,1,0,2,2,2,2,2,0,0,2,2,0,0,0,2,0,2,0,2,0,0,2,0,0,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2,2,0,1,1,0,2,2,2,0,2,0,0,2,0,0,2,0,2,2,0,0,2,0,2,2,0,2,2,2,2,2,0,2,0,0,2,2,2,0,2,0,2,0,2,0,1,1,0,2,2,2,2,2,2,0,2,0,0,2,2,2,0,2,2,0,2,0,0,2,0,0,0,0,2,2,0,0,2,0,0,2,0,0,0,0,2,2,0,1,1,0,2,2,2,2,2,2,0,2,0,0,0,0,0,2,0,0,0,2,2,2,2,0,2,0,2,0,0,0,0,2,0,0,2,2,2,0,0,0,2,0,1,1,0,0,2,0,0,2,0,2,0,2,2,2,0,2,0,2,0,2,2,2,0,0,2,2,0,2,0,0,0,2,2,2,0,0,0,2,2,2,2,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,50,83,69,55,5,36,88,27,48,45,55,26,23,56,75,93,20,97,93,90,50,24,84,49,93,23,74,88,42,37,31,74,42,93,56,81,50,48,64,26,80,53,72,51,63,25,30,74,85,93,5,1,78,10,85,22,20,18,92,98,97,29,52,22,67,48,79,50,19,64,11,1,29,71,44,32,19,30,36,73,78,28,13,42,33,74,56,38,1,55,94,9,53,16,26,24,75,3,17,67,18,19,7,56,61,22,71,85,2,24,80,20,6,33,12,67,38,81,41,59,81,38,17,7,61,10,77,36,96,85,10,71,76,68,90,62,93,16,83,61,59,42,83,81,10,94,35,38,66,27,61,26,61,61,65,1,42,65,83,30,23,96,39,87,30,38,47,97,48,77,38,23,23,26,36,58,77,33,44,23,21,49,72,7,46,73,43,86,8,71,92,43,16,1,72,40,55,10,74,5,84,24,92,24,10,47,7,49,9,23,6,80,18,78,88,50,31,56,45,35,74,62,68,74,45,78,5,20,75,83,72,13,59,66,76,63,49,97,54,9,16,32,39,7,45,16,32,57,71,18,80,90,54,8,27,53,5,10,2,74,79,34,2,76,21,80,75,62,88,46,32,26,5,1,60,14,73,60,7,69,93,36,4,63,94,89,2,55,30,5,7,28,71,72,45,44,3,98,43,42,28,63,69,52,61,67,79,80,55,1,39,1,58,6,82,64,81,11,16,41,50,23,31,94,98,75,96,94,40,98,97,20,88,94,64,17,61,60,63,26,76,87,73,80,30,15,61,90,61,16,41,86,52,67,90,58,85,33,29,59,92,45,10,82,22,65,62,43,14,92,47,17,25,15,55,55,25,70,52,63,86,73,86,34,43,7,2,94,93,13,73,28,88,23,12,82,16,79,56,36,32,52,62,82,81,57,39,88,70,25,50,14,80,52,56,11,81,14,15,83,36,84,76,74,21,19,56,1,29,44,68,87,42,68,92,54,13,76,48,48,66,89,49,64,32,59,53,30,57,20,94,72,42,2,77,7,56,54,27,17,67,67,56,94,8,58,28,81,9,72,64,20,95,92,7,61,7,46,44,2,81,17,78,7,32,64,40,17,47,62,57,19,61,36,88,10,71,6,88,39,43,48,2,50,30,20,39,75,9,46,78,17,56,88,96,20,50,7,14,12,67,7,23,77,94,58,44,96,65,48,44,60,52,65,88,39,45,13,63,37,16,2,26,41,95,73,45,37,29,35,82,30,14,90,18,29,33,92,23,63,51,79,17,86,76,83,85,20,43,48,51,28,94,50,77,74,90,5,33,52,47,14,76,70,3,59,28,95,78,82,1,6,59,97,38,68,60,68,95,31,98,8,32,71,70,25,47,76,75,13,35,60,19,45,7,49,34,61,93,21,79,81,52,17,82,28,69,35,72,10,12,55,25,45,9,67,60,67,27,97,26,13,30,4,6,64,34,36,88,19,90,50,35,32,6,38,15,18,88,10,42,68,71,31,29,45,90,50,85,13,69,80,91,4,21,81,18,21,38,44,42,49,54,47,61,43,17,54,89,47,13,27,6,67,96,54,80,54,85,32,1,39,18,28,98,55,30,2,90,43,9,48,43,54,42,21,3,50,49,2,47,23,51,2,66,88,80,24,66,31,28,68,15,93,34,55,69,86,92,16,13,69,26,78,20,84,16,87,1,51,91,65,89,70,31,28,48,28,81,54,40,81,77,25,64,98,41,46,30,50,9,33,58,24,31,62,41,92,4,40,12,53,32,50,62,78,80,36,90,36,47,9,34,13,91,36,74,82,60,31,74,77,33,16,79,10,68,56,52,43,71,76,31,65,14,68,49,73,36,55,76,48,37,3,33,85,8,42,92,44,66,22,84,54,98,50,8,21,70,63,89,53,21,20,72,9,46,38,27,20,76,66,57,15,73,23,34,36,38,46,53,76,86,45,75,50,27,25,81,80,68,95,73,12,89,58,15,30,79,63,35,62,53,15,27,64,89,21,58,65,80,16,92,64,29,89,16,71,23,68,46,30,17,41,67,4,16,84,25,9,78,46,18,85,3,26,32,12,45,49,79,11,4,65,82,17,21,29,60,1,20,16,93,72,7,17,88,67,75,3,24,73,73,71,54,35,95,57,80,16,7,44,8,58,83,68,87,21,41,90,7,85,32,22,41,23,47,30,56,94,27,50,65,62,36,74,51,39,21,36,44,47,96,15,59,72,97,84,25,649812]
        self.thrusters = [3,8,1001,8,10,8,105,1,0,0,21,46,55,72,85,110,191,272,353,434,99999,3,9,1002,9,5,9,1001,9,2,9,102,3,9,9,101,2,9,9,102,4,9,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,101,2,9,9,1002,9,2,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,1002,9,3,9,101,3,9,9,1002,9,5,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99]
        self.repair_program = [99]
        self.t1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        self.t2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
        self.t3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        self.t4 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
        self.t5 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

    def load_program_to_ram(self, program, noun=None, verb=None):
        self.ram = [0 for x in range(56000)]  # might need 34463338 ram
        self.pointer = 0
        for i, e in enumerate(program):
            self.ram[i] = e
        # print("Finished Loading Program to RAM")
        # print(f"Initial Program len is {len(program)}, RAM in use: 56k")
        if noun: self.ram[1] = noun
        if verb: self.ram[2] = verb

    def process(self, verbose=True):
        op_code = int(str(self.ram[self.pointer])[-2:])
        if verbose: print(f"P: {self.pointer} | OP: {self.ram[self.pointer]}")
        if op_code == 99: return False
        if op_code ==  1: return self.op_one(verbose)
        if op_code ==  2: return self.op_two(verbose)
        if op_code ==  3: return self.op_three(verbose)
        if op_code ==  4: return self.op_four(verbose)
        if op_code ==  5: return self.op_five(verbose)
        if op_code ==  6: return self.op_six(verbose)
        if op_code ==  7: return self.op_seven(verbose)
        if op_code ==  8: return self.op_eight(verbose)
        if op_code ==  9: return self.op_nine(verbose)
        else:
            print(f"BAD OP CODE>>>  CMON!! ==> {op_code}")

    def op_one(self,verbose=True):
        operation = str(self.ram[self.pointer])
        if len(operation) < 5:
            operation = "0"*(5-len(operation)) + operation
        
        var_1_mode = int(operation[2])
        var_2_mode = int(operation[1])
        var_3_mode = int(operation[0])
        
        input_one = int(self.ram[self.pointer+1])
        input_two = int(self.ram[self.pointer+2])
        output    = int(self.ram[self.pointer+3])

        if var_1_mode   == 0: one = int(self.ram[input_one])
        elif var_1_mode == 1: one = int(input_one)
        elif var_1_mode == 2: one = int(self.ram[input_one + self.ram[-1]])

        if var_2_mode   == 0: two = int(self.ram[input_two])
        elif var_2_mode == 1: two = int(input_two)
        elif var_2_mode == 2: two = int(self.ram[input_two + self.ram[-1]])

        if var_3_mode   == 0: three = int(output)
        elif var_3_mode == 2: three = int(output + self.ram[-1])
        # three = output

        if verbose: print(f"Got opcode 1 | {operation} | Addition")
        if verbose: print(f"\tFULL LINE: {operation}, {input_one}, {input_two}, {output}" )
        if verbose: print(f"\tin_1_mode = {var_1_mode}")
        if verbose: print(f"\tin_2_mode = {var_2_mode}")
        if verbose: print(f"\t{one} + {two} = {one+two} ==> 0x{three}")
        self.ram[three] = one + two  # THE ACTION
        if verbose: print(f"\t0x{three} ==> {self.ram[three]}")
        self.pointer += 4
        return True
    
    def op_two(self,verbose=True):
        operation = str(self.ram[self.pointer])
        if len(operation) < 5:
            operation = "0"*(5-len(operation)) + operation
        op_code = int(operation[-2:])
        var_1_mode = int(operation[2])
        var_2_mode = int(operation[1])
        var_3_mode = int(operation[0])
        input_one = int(self.ram[self.pointer+1])
        input_two = int(self.ram[self.pointer+2])
        output    = int(self.ram[self.pointer+3])

        if var_1_mode   == 0: one = int(self.ram[input_one])
        elif var_1_mode == 1: one = int(input_one)
        elif var_1_mode == 2: one = int(self.ram[input_one + self.ram[-1]])

        if var_2_mode   == 0: two = int(self.ram[input_two])
        elif var_2_mode == 1: two = int(input_two)
        elif var_2_mode == 2: two = int(self.ram[input_two + self.ram[-1]])

        if var_3_mode   == 0: three = int(output)
        elif var_3_mode == 2: three = int(output + self.ram[-1])

        if verbose: print(f"Got opcode 2 | {operation} | Addition")
        if verbose: print(f"\tFULL LINE: {operation}, {input_one}, {input_two}, {output}" )
        if verbose: print(f"\tin_1_mode = {var_1_mode}")
        if verbose: print(f"\tin_2_mode = {var_2_mode}")
        if verbose: print(f"\t{one} * {two} = {one*two} ==> 0x{three}")
        self.ram[three] = one * two  # THE ACTION
        if verbose: print(f"\t0x{three} ==> {self.ram[three]}")
        self.pointer += 4
        return True

    def op_three(self, verbose=True):
        operation = str(self.ram[self.pointer])
        if len(operation) < 5:
            operation = "0"*(5-len(operation)) + operation
        var_1_mode = int(operation[2])
        input_one = int(self.ram[self.pointer+1])
        if var_1_mode == 0: one = input_one
        if var_1_mode == 2: one = input_one + self.ram[-1]
        if self.manual_input:
            x = input("PLEASE INPUT A VARIABLE(1): ") or 1
        else:
            x = self.report()
            # print(f"Accepting Input of {x}")  # this is good.
        if verbose: print(f"\tAddr 0x{one} = {x}")
        self.ram[one] = int(x)
        self.input    = int(x)
        self.pointer += 2
        return True

    def op_four(self, verbose=True):
        operation = str(self.ram[self.pointer])
        if len(operation) < 5: operation = "0"*(5-len(operation)) + operation
        var_1_mode = int(operation[2])
        input_one = int(self.ram[self.pointer+1])
        if var_1_mode == 0: 
            one = input_one
            if verbose: print(f"\tValue @ Addr 0x{one} = {self.ram[one]}")
            self.pointer += 2
            return self.ram[one]
        if var_1_mode == 1: 
            one = input_one
            if verbose: print(f"\tValue @ Addr 0x{self.pointer+1} = {one}")
            self.pointer += 2
            return one
        if var_1_mode == 2: 
            one = input_one + self.ram[-1]
            if verbose: print(f"\tValue @ Addr 0x{one} = {self.ram[one]}")
            self.pointer += 2
            return self.ram[one]
        
    def op_five(self, verbose=True):
        """
        Opcode 5 is jump-if-true: if the first parameter is non-zero, 
        it sets the instruction pointer to the value from the second parameter. 
        Otherwise, it does nothing.
        """
        operation = str(self.ram[self.pointer])
        if len(operation) < 5:
            operation = "0"*(5-len(operation)) + operation
        op_code = int(operation[-2:])
        var_1_mode = int(operation[2])
        var_2_mode = int(operation[1])
        input_one = self.ram[self.pointer+1]
        input_two = self.ram[self.pointer+2]

        if var_1_mode == 0:   one = int(self.ram[input_one])
        elif var_1_mode == 1: one = int(input_one)
        elif var_1_mode == 2: one = int(self.ram[input_one + self.ram[-1]])

        if var_2_mode == 0:   two = int(self.ram[input_two])
        elif var_2_mode == 1: two = int(input_two)
        elif var_2_mode == 2: two = int(self.ram[input_two + self.ram[-1]])

        if verbose: print(f"\tGot opcode 5 | {operation} | Jump-If-True")
        if verbose: print(f"\tFULL LINE: {operation}, {input_one}, {input_two}" )
        if verbose: print(f"\tin_1_mode = {var_1_mode}")
        if verbose: print(f"\tin_2_mode = {var_2_mode}")
        if verbose: print(f"\tDoes {one} == 0 ?? {one == 0} | if True pointer = {self.pointer + 3} else {two}")
        if one == 0: self.pointer += 3
        else:        self.pointer  = two
        if verbose: print(f"\tNew pointer Position: {self.pointer}")
        return True

    def op_six(self, verbose=True):
        """
        Opcode 6 is jump-if-false: if the first parameter is zero, 
        it sets the instruction pointer to the value from the second parameter. 
        Otherwise, it does nothing.
        """
        operation = str(self.ram[self.pointer])
        if len(operation) < 5:
            operation = "0"*(5-len(operation)) + operation
        op_code = int(operation[-2:])
        var_1_mode = int(operation[2])
        var_2_mode = int(operation[1])
        input_one = self.ram[self.pointer+1]
        input_two = self.ram[self.pointer+2]

        if var_1_mode == 0:   one = int(self.ram[input_one])
        elif var_1_mode == 1: one = int(input_one)
        elif var_1_mode == 2: one = int(self.ram[input_one + self.ram[-1]])

        if var_2_mode == 0:   two = int(self.ram[input_two])
        elif var_2_mode == 1: two = int(input_two)
        elif var_2_mode == 2: two = int(self.ram[input_two + self.ram[-1]])

        if verbose: print(f"\tGot opcode 6 | {operation} | Jump-If-False")
        if verbose: print(f"\tFULL LINE: {operation}, {input_one}, {input_two}" )
        if verbose: print(f"\tin_1_mode = {var_1_mode}")
        if verbose: print(f"\tin_2_mode = {var_2_mode}")
        if verbose: print(f"\tDoes {one} == 0 ?? {one == 0} | if True pointer = {two} else {self.pointer + 3}")
        if one == 0: self.pointer = two
        else:        self.pointer += 3
        if verbose: print(f"\tNew pointer Position: {self.pointer}")
        return True

    def op_seven(self, verbose=True):
        operation = str(self.ram[self.pointer])
        if len(operation) < 5:
            operation = "0"*(5-len(operation)) + operation
        op_code    = int(operation[-2:])
        var_1_mode = int(operation[2])
        var_2_mode = int(operation[1])
        var_3_mode = int(operation[0])
        input_one  = self.ram[self.pointer+1]
        input_two  = self.ram[self.pointer+2]
        output     = self.ram[self.pointer+3]

        if var_1_mode == 0:   one = int(self.ram[input_one])
        elif var_1_mode == 1: one = int(input_one)
        elif var_1_mode == 2: one = int(self.ram[input_one + self.ram[-1]])

        if var_2_mode == 0:   two = int(self.ram[input_two])
        elif var_2_mode == 1: two = int(input_two)
        elif var_2_mode == 2: two = int(self.ram[input_two + self.ram[-1]])

        if var_3_mode   == 0: three = int(output)
        elif var_3_mode == 2: three = int(output + self.ram[-1])

        if verbose: print(f"\tGot opcode 5 | {operation} | Jump-If-True")
        if verbose: print(f"\tFULL LINE: {operation}, {input_one}, {input_two}" )
        if verbose: print(f"\tin_1_mode = {var_1_mode}")
        if verbose: print(f"\tin_2_mode = {var_2_mode}")
        if verbose: print(f"\tis {one} < {two} ?? {one < two} | if True 1 --> 0x{three}")
        self.ram[three] = 1 if one < two else 0
        if verbose: print(f"\t0x{three} ==> {self.ram[three]}")
        self.pointer += 4
        return True

    def op_eight(self, verbose=True):
        operation = str(self.ram[self.pointer])
        if len(operation) < 5:
            operation = "0"*(5-len(operation)) + operation
        op_code = int(operation[-2:])
        var_1_mode = int(operation[2])
        var_2_mode = int(operation[1])
        var_3_mode = int(operation[0])
        input_one = self.ram[self.pointer+1]
        input_two = self.ram[self.pointer+2]
        output = self.ram[self.pointer+3]

        if var_1_mode == 0:   one = int(self.ram[input_one])
        elif var_1_mode == 1: one = int(input_one)
        elif var_1_mode == 2: one = int(self.ram[input_one + self.ram[-1]])

        if var_2_mode == 0:   two = int(self.ram[input_two])
        elif var_2_mode == 1: two = int(input_two)
        elif var_2_mode == 2: two = int(self.ram[input_two + self.ram[-1]])

        if var_3_mode   == 0: three = int(output)
        elif var_3_mode == 2: three = int(output + self.ram[-1])

        if verbose: print(f"\tGot opcode 5 | {operation} | Jump-If-True")
        if verbose: print(f"\tFULL LINE: {operation}, {input_one}, {input_two}" )
        if verbose: print(f"\tin_1_mode = {var_1_mode}")
        if verbose: print(f"\tin_2_mode = {var_2_mode}")
        if verbose: print(f"\tDoes {one} == {two} ?? {one == two} | if True 1 --> 0x{three}")
        self.ram[three] = 1 if one == two else 0
        if verbose: print(f"\t0x{three} ==> {self.ram[three]}")
        self.pointer += 4
        return True

    def op_nine(self, verbose=True):
        """
        adjusts the relative base by the value of its only parameter. The relative base increases (or decreases, if the value is negative) by the value of the parameter.
        """
        operation = str(self.ram[self.pointer])
        if verbose: print(f"Got opcode 9 | {operation} | Relative Base")
        if len(operation) < 5:
            operation = "0"*(5-len(operation)) + operation
        input_one = self.ram[self.pointer+1]
        var_1_mode = int(operation[2])
        if var_1_mode == 0:
            one = int(self.ram[input_one])
        elif var_1_mode == 1:
            one = int(input_one)
        elif var_1_mode == 2:
            one = int(self.ram[input_one + self.ram[-1]])

        if verbose: print(f"R-Pointer = {self.ram[-1]} + {one} == {self.ram[-1] + one}")
        self.ram[-1] += one
        self.pointer += 2
        return True

    def report(self, printer=False): return 1

    def get_action(self, num_actions=2):
        action = []
        while len(action) < num_actions:
            output = self.process(False)
            if type(output) is bool:
                if output == False: return False
            if type(output) is int:
                action.append(output)
        return action


class Arcade(Int_Code_Comp):
    """FINISHED AND WORKING... just run arcade()"""
    def __init__(self, verbose=False):
        super().__init__(manual_input=False)
        self.load_program_to_ram(self.arcade)
        self.score = 0
        self.game = [[0 for y in range(23)] for x in range(43)]
        self.highscore = 0
        self.played = 0
        self.counter = 0
        self.verbose = verbose
        if verbose:
            p = input("Do you want to play a game?? (y/n) >") or 0
            if 'y' not in str(p):
                self.play = 0
            else:
                self.play = 1

    def count(self):
        counter = 0
        for i in self.game:
            for x in i:
                if x == 2: counter += 1
        return counter

    def run(self):
        gameover = False
        setup = False
        win = False
        while True:
            # draw inital state to play game.
            while not setup:
                act = self.get_action(3)
                if act[0] == -1:
                    self.score = act[2]
                    # self.refresh()
                    setup = True
                    print(f"Finished Seting up screen | score: {self.score}")
                    break
                self.game[act[0]][act[1]] = act[2]
            if self.count() == 0:
                if not win:
                    print('*'*42)
                    print("YOU WON MAN!!")
                    print('*'*42)
                    win = True
            if gameover:
                if not win:
                    print('*'*42)
                    print("GAME OVER MAN!!")
                    print('*'*42)
                
                
                if self.score > self.highscore: 
                    self.highscore = self.score
                
                print(f"Score: {self.score}")
                retry = input("PLAY AGAIN?? (y/n) >") or ''
                
                if not 'y' in retry:
                    retry1 = input("Let Santa Play?? (y/n) >") or ''
                    if not 'y' in retry1:
                        exit("Thanks for playing Santa'z Intcode Blocks")
                    else:
                        self.play = 0
                
                self.game = [[0 for y in range(23)] for x in range(43)]
                setup = False
                gameover = False
                self.counter = 0
                self.played += 1
                self.load_program_to_ram(self.arcade)
                self.pointer = 0
            else:
                output = self.process(False)
                if output == True: continue
                if output == False: gameover = True; continue
                if type(output) is int:
                    y = self.process(False)
                    peice = self.process(False)
                    if output == -1: self.score = peice
                    else: self.game[output][y] = peice
            self.counter += 1

    def report(self):
        direction = self.update(self.verbose)
        if self.play:
            x = input("a for left, d for right, s no move. (s)> ") or 's'
            if   'a' in x: return -1
            elif 'd' in x: return 1
            elif 's' in x: return 0
            else: return 0
        return direction

    def update(self, verbose=True):
        #if self.verbose: 
        #    os.system('clear')
        floped = []
        ball = [0,0]
        paddle = [0,0]
        for i in range(len(self.game[0])):
            msg = ""
            for x in range(len(self.game)):
                if   self.game[x][i] == 0: msg += ' '
                elif self.game[x][i] == 1: msg += '%'
                elif self.game[x][i] == 2: msg += '#'
                elif self.game[x][i] == 3: 
                    msg += '^'
                    paddle = [x, i]
                elif self.game[x][i] == 4: 
                    msg += '0'
                    ball = [x, i]
            floped.append(msg)
        for i in floped:
            msg = ""
            for x in i: msg += x
            if verbose: print(msg)
        try:
            if verbose: guide1 = [' ' for x in range(43)]
            if verbose: guide1[paddle[0]] = '|'
            if verbose: guide1[ball[0]] = '+'
            if verbose: print(''.join([x for x in guide1]))
            pass
        except:
            if verbose: print()
            pass
        if self.verbose:
            print(f"Score: {self.score}  |  Moves: {self.counter}")
            print(f"Blocks Remaining: {self.count()}")
            print(f"High Score: {self.highscore}")
            print(f"Games Played: {self.played}")
            print(f"Paddle Position: {paddle[0], paddle[1]}")
            print(f"Ball Position: {ball[0], ball[1]}")
            # print(f"Difference = {paddle[0] - ball[0]}")
        suggested = paddle[0] - ball[0]
        if verbose: time.sleep(.05)
        if suggested == 0: return  0
        elif suggested > 0: return -1
        elif suggested < 0: return 1


class Robot(Int_Code_Comp):
    def __init__(self, manual_input=False, program=None):
        super().__init__(None, manual_input)
        if program is None:
            self.load_program_to_ram(self.paint)
        else:
            self.load_program_to_ram(program)
        self.boardsize = 100
        self.position = [0,0]
        self.all_positions = []
        self.direction = 0
        self.counter = 0
        self.draw = False
        self.verbose = False
        self.msg_actions = []
        self.gameboard = []
        self.new_board()

    def new_board(self):
        self.gameboard = [[0 for x in range(self.boardsize)] for x in range(self.boardsize)]
        self.position = [int(self.boardsize/2), int(self.boardsize/2)-25]
        self.gameboard[self.position[0]][self.position[1]] = 1

    def update(self, action=None):
        os.system('clear')
        print("%"*len(self.gameboard[0]))
        for i, e in enumerate(reversed(self.gameboard)):
            if not sum(e) == 0:
                msg = ''
                for y, x in enumerate(e):
                    if i == self.position[0] and y == self.position[1]: 
                        if   self.direction == 0: msg += '^'
                        elif self.direction == 1: msg += '>'
                        elif self.direction == 2: msg += 'V'
                        elif self.direction == 3: msg += '<'
                        else: msg += '!'
                    else: msg += '.' if x == 0 else '#'
                print(msg)
        print("%"*len(self.gameboard[0]))
    
    def report(self): return int(self.gameboard[self.position[0]][self.position[1]])

    def unique_actions(self): return int(len(set(tuple(x) for x in self.all_positions))-1)

    def take_action(self, action): return True

    def run(self, num_actions=2, draw=False):
        start = timer()
        while True:
            action = self.get_action(num_actions)
            if action == False: break
            self.take_action(action)
            self.counter += 1
            if draw:
                self.update(action)
                time.sleep(.05)
        return timer() - start

    def start(self): return self.run()


class ThrusterAmplifiers(Int_Code_Comp):
    """FINISHED AND WORKING... just run thrusters()"""
    def __init__(self, phase_setting):
        super().__init__(manual_input=False)
        self.load_program_to_ram(self.thrusters)
        self.phase_setting = phase_setting
        self.input = 0
        self.inputter = True

    def report(self):
        if self.inputter:
            self.inputter = False
            return self.phase_setting
        return self.input

    def run_until_wait(self, _input):
        self.input = _input
        while True:
            output = self.process(False)
            if type(output) is bool:
                if output == False: return False
            
            if type(output) is int: return output

    def run(self):
        result = 0
        while True:
            output = self.get_action(1)
            if type(output) is bool:
                if output == False: break
            if type(output) is int:
                result = output
        self.output = result
        return result


class Painter(Robot):
    def __init__(self, manual_input=False):
        super().__init__(manual_input)
        # if True:
        #      self.gameboard[self.position[0]][self.position[1]] = 1

    def update(self, action=None):
        # os.system('clear')
        print("%"*len(self.gameboard[0]))
        for i, e in enumerate(reversed(self.gameboard)):
            if not sum(e) == 0:
                msg = ''
                for y, x in enumerate(e):
                    if i == self.position[0] and y == self.position[1]: 
                        if   self.direction == 0: msg += '^'
                        elif self.direction == 1: msg += '>'
                        elif self.direction == 2: msg += 'V'
                        elif self.direction == 3: msg += '<'
                        else: msg += '!'
                    else: msg += '.' if x == 0 else '#'
                print(msg)
        print("%"*len(self.gameboard[0]))

        direction = lambda x: "Turn Left" if x == 0 else "Turn Right"
        color = lambda x: "Paint Black" if x == 0 else "Paint White"
        print(f"Current Position = ({self.position[0]}, {self.position[1]})")
        print(f"Position List: {str(self.all_positions[-5:])}")
        # unique_actions = len(set(tuple(x) for x in self.all_positions))
        print(f"Number of actions: {len(self.all_positions)-1}, unique actions: {self.unique_actions()}")
        if action:
            msg_action = f"Action #{self.counter} : {direction(action[1])}, {color(action[0])}"
            self.msg_actions.append(msg_action)
            for act in reversed(self.msg_actions[-10:]):
                print(act)

    def take_action(self, action):
        # Paint the Square ==> Then Move. Paint->Move
        self.gameboard[self.position[0]][self.position[1]] = action[0]

        # do move.
        if action[1] == 0:  # turn left or minus one
            if self.direction == 0: # if is up then go left
                self.direction = 3  # left
            else: self.direction -= 1
        if action[1] == 1:  # turn right or plus one
            if self.direction == 3:
                self.direction = 0
            else: self.direction += 1

        # move in the direction of the turn
        if   self.direction == 0: self.position[0] += 1
        elif self.direction == 1: self.position[1] += 1
        elif self.direction == 2: self.position[0] -= 1
        elif self.direction == 3: self.position[1] -= 1
        else:
            exit(f"Direction is out of bounds: {self.direction}")

        # add this new tile to the list of tiles visited.
        self.all_positions.append(copy.copy(self.position))

    def start(self):
        runtime = self.run(2)
        print("Results:")
        self.update()
        print(f"Total Actions: {len(self.all_positions)}")
        print(f"Total Runtime: {runtime/60:.2f} mins")
        print(f"Total Unique Moves: {self.unique_actions()}")


class Repair(Robot):
    def __init__(self, manual_input=False):
        program = [3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,1002,1034,1,1039,1001,1036,0,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,1001,1034,0,1039,102,1,1036,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1105,1,124,1001,1034,-1,1039,1008,1036,0,1041,101,0,1035,1040,102,1,1038,1043,1001,1037,0,1042,1106,0,124,1001,1034,1,1039,1008,1036,0,1041,1001,1035,0,1040,102,1,1038,1043,1001,1037,0,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,9,1032,1006,1032,165,1008,1040,5,1032,1006,1032,165,1101,0,2,1044,1105,1,224,2,1041,1043,1032,1006,1032,179,1102,1,1,1044,1106,0,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,40,1044,1106,0,224,1101,0,0,1044,1106,0,224,1006,1044,247,102,1,1039,1034,101,0,1040,1035,101,0,1041,1036,1001,1043,0,1038,1001,1042,0,1037,4,1044,1106,0,0,26,29,83,66,1,36,14,44,33,12,3,15,20,56,9,35,51,55,6,20,13,71,15,23,94,38,45,15,47,30,89,39,11,55,5,9,47,29,41,36,78,12,4,65,48,66,36,94,76,30,63,41,32,1,73,1,35,65,87,46,18,90,11,44,30,73,87,8,38,46,17,78,51,34,19,53,37,26,20,24,46,64,17,6,26,41,10,62,14,88,23,94,13,55,5,45,10,39,83,99,32,34,72,30,58,33,71,47,21,38,97,38,46,41,18,39,37,8,86,55,35,4,92,19,21,53,61,6,55,69,16,85,62,26,63,17,80,33,10,53,91,2,37,94,37,93,7,97,18,55,54,36,17,62,89,12,92,32,69,4,46,47,19,89,25,12,51,91,9,1,71,35,56,39,98,48,7,49,24,95,15,45,2,1,93,82,19,7,11,70,30,64,28,27,58,4,39,30,94,72,33,43,90,98,26,32,70,1,81,25,35,47,17,31,92,15,73,13,27,72,65,30,67,2,22,89,77,30,47,12,58,26,79,22,37,74,41,3,42,30,39,67,24,18,62,98,19,59,95,25,6,67,42,35,85,51,48,7,63,17,67,53,45,13,25,43,1,54,4,65,55,20,73,32,70,1,33,39,93,88,19,35,56,21,13,53,73,31,21,44,73,31,13,69,30,42,26,51,25,90,16,49,9,93,50,28,60,24,18,61,23,11,98,19,45,77,12,61,31,3,66,56,4,77,24,59,87,31,38,65,67,7,9,23,71,9,59,35,55,83,22,12,94,17,67,87,96,63,8,29,32,34,15,55,39,60,41,74,39,81,47,51,25,26,57,28,18,60,84,20,16,66,42,14,25,16,94,2,22,74,85,19,63,32,9,19,11,91,44,34,21,1,56,12,87,8,52,18,56,7,90,5,86,81,24,98,21,9,80,59,68,10,80,53,18,75,50,9,14,43,26,29,57,86,39,41,93,3,69,55,16,84,15,22,84,30,72,19,13,15,19,80,97,79,32,68,77,82,30,19,4,71,45,67,14,95,17,54,80,88,25,13,80,41,37,96,15,28,26,33,73,32,45,79,21,52,23,98,82,21,16,13,64,32,39,93,17,33,95,61,36,12,21,3,84,4,88,22,26,59,80,27,82,2,85,79,29,33,52,17,23,95,8,64,16,56,23,42,43,18,41,11,9,84,42,62,4,67,17,98,76,99,1,16,72,72,10,79,19,76,4,54,9,99,34,33,7,97,85,19,76,93,38,6,90,37,90,2,83,61,19,43,39,2,91,17,60,21,79,2,32,94,38,32,7,64,8,14,7,68,23,28,75,24,73,50,29,63,22,89,4,51,66,2,7,33,82,13,23,84,81,23,55,68,15,27,9,97,27,79,42,86,75,56,13,95,74,5,88,25,44,99,33,14,24,29,21,78,4,15,75,32,92,74,11,56,24,57,10,28,73,8,10,90,77,30,96,8,60,3,71,20,41,9,33,89,38,74,95,4,95,35,13,18,55,10,81,9,60,17,67,7,34,48,48,15,54,79,37,66,43,22,64,28,28,4,91,5,9,92,30,64,37,98,66,15,92,2,3,25,70,25,33,61,56,25,70,58,30,41,97,18,54,10,49,45,3,1,30,57,30,46,8,55,79,39,58,46,35,19,38,80,86,4,36,75,29,62,39,71,2,41,6,66,36,99,21,61,39,72,3,48,29,43,31,59,84,71,12,52,61,82,11,56,23,51,30,60,88,65,35,48,24,58,76,49,93,51,33,72,0,0,21,21,1,10,1,0,0,0,0,0,0]
        super().__init__(manual_input, program)
        self.found_it = False
        self.boardsize = 500
        self.action = 0
        self.gameboard = []
        self.new_board()

    def new_board(self):
        self.gameboard = [[9 for x in range(self.boardsize)] for x in range(self.boardsize)]
        self.position = [int(self.boardsize/2), int(self.boardsize/2)]
        self.gameboard[self.position[0]][self.position[1]] = 1

    def report(self):
        return self.input

    def update(self, action=None):
        #  os.system('clear')
        print("%"*len(self.gameboard[0]))
        for i, e in enumerate(self.gameboard):
            # if not sum(e) == 0:
            if True:
                msg = ''
                for y, x in enumerate(e):
                    if i == self.position[0] and y == self.position[1]: 
                        if   self.input == 1: msg += '^'
                        elif self.input == 2: msg += 'V'
                        elif self.input == 3: msg += '<'
                        elif self.input == 4: msg += '>'
                        else: msg += '!'
                    else:
                        if x == 0: msg += '#'
                        if x == 1: msg += '.'
                        if x == 2: msg += 'G'
                        if x == 9: msg += ' '
                print(msg)
        print("%"*len(self.gameboard[0]))
        print(f"Current Position: ({self.position[0]},{self.position[1]})")

    def take_action(self, action):
        if   action[0] == 0: output = 'WALL'
        elif action[0] == 1: output = 'OPEN -> MOVE'
        elif action[0] == 2: output = 'GOAL -> MOVE'
        self.action = action[0]

        tile_in_question = copy.copy(self.position)
        if   self.input == 1: tile_in_question[0] -= 1   # 1 is N
        elif self.input == 2: tile_in_question[0] += 1   # 2 is S
        elif self.input == 3: tile_in_question[1] -= 1   # 3 is W
        elif self.input == 4: tile_in_question[1] += 1   # 4 is E

        # Paint the Square ==> Then Move. Paint->Move
        self.gameboard[tile_in_question[0]][tile_in_question[1]] = action[0]

        if action[0] == 0: return
        
        self.position = copy.copy(tile_in_question)

        if action[0] == 2: self.found_it = True

        # add this new tile to the list of tiles visited.
        self.all_positions.append(copy.copy(self.position))

    def run(self, num_actions=2, draw=False):
        start = timer()
        while True:
            action = self.get_action(num_actions)
            if action == False: break
            self.take_action(action)
            self.counter += 1
            if draw:
                self.update(action)
                time.sleep(.05)
        return timer() - start

    def once(self):
        action = self.get_action(1)
        if action == False: return False
        self.take_action(action)
        self.counter += 1
        return True
    
    def start(self):
        runtime = self.run(num_actions=1, draw=False)
        print(f"Total Runtime: {runtime/60:.2f} mins")
        return runtime

    def translate(self, surr): return [self.gameboard[x[0]][x[1]] for x in surr]

    def surroundings(self):
        return [
            [self.position[0]-1,self.position[1]], # U
            [self.position[0]+1,self.position[1]], # D
            [self.position[0],self.position[1]-1], # L
            [self.position[0],self.position[1]+1], # R
        ]

    def direct(self, number):
        if   number == 1: return "UP"
        elif number == 2: return "DOWN"
        elif number == 3: return "LEFT"
        elif number == 4: return "RIGHT"

    def act(self, number):
        if   number == 0: return "WALL"
        elif number == 1: return "OPEN -> MOVE"
        elif number == 2: return "OPEN -> GOAL"


def main():
    os.system('clear')
    x = input(
        """

        1: Test Program
        2: Boost Program
        3: Thruster Amplifiers
        4: Arcade
        5: Painter Robot

        Program (1-5) >> """
        )
    try: x = int(x)
    except: print("Bad Response"); exit()
    if   x == 0: print("cmon.")
    elif x == 1: test_program()
    elif x == 2: boost_program()
    elif x == 3: thrusters()
    elif x == 4: arcade()
    elif x == 5: paint()
    else: print("Not a Valid Program.")

def paint():
    app = Painter()    #  Robot()
    app.start()
    print("fin")

def arcade():
    app = Arcade(True)
    try:
        app.run()
    except KeyboardInterrupt:
        exit("\n\nTHANKS FOR PLAYING!")

def thrusters():
    stack = {}
    stack_test = {'TEST': [9,7,8,5,6]}
    thread_stack = []
    computed = [0]
    counter = 0
    start = timer()
    ################################################
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    for e in range(5):
                        stack[counter] = [a,b,c,d,e]
                        counter += 1
    ################################################
    loop_stack = {}
    ################################################
    for a in range(5, 10):
        for b in range(5, 10):
            for c in range(5, 10):
                for d in range(5, 10):
                    for e in range(5, 10):
                        loop_stack[counter] = [a,b,c,d,e]
                        counter += 1
    ################################################
    def check_dup(pile):
        if len(pile) == len(set(pile)): return False
        else: return True

    for _, v in loop_stack.items():
        ################################################
        def work_stack(*args, **kwargs):
            _input = 0
            machine_stack = []
            breaker = False
            for element in args: machine_stack.append(ThrusterAmplifiers(element))
            while True:
                if breaker: break
                for index, machine in enumerate(machine_stack):
                    # print(f"Begining work on Machine {index+1} | input = {_input}")
                    result = machine.run_until_wait(_input)
                    if result is False:
                        computed.append(_input)
                        # print(f"Ending Machine Loop. with a correct answer of {_input}")
                        breaker = True
                        break
                    else:
                        _input = result
                        # print(f"Switching Machines with an output of {_input}")
                
            computed.append(_input)
            if True:
                print(f" Phase Setting Sequence: {[x for x in args]} | Power: {_input}")
        ################################################
        
        if not check_dup(v):
            t = threading.Thread(target=work_stack, args=v)
            thread_stack.append(t)
    
    for t in thread_stack: t.start()
    
    while True:
        for t in thread_stack:
            if not t.isAlive(): thread_stack.remove(t)
        if len(thread_stack) == 0: break
        else: 
            # print(f"Still running threads = {len(thread_stack)}")
            time.sleep(.5)
    runtime = timer() - start

    print(f"\nBest Thruster Power is {max(computed)}")
    print(f"Total Runtime is {runtime/60:.2f} mins")

def test_program():
    app = Int_Code_Comp()
    app.load_program_to_ram(app.TEST)
    while True:
        output = app.process(False)
        if type(output) is int:
            print(f"[OUTPUT] {output}")
        if not output: break
    print("finished")

def boost_program():
    app = Int_Code_Comp()
    app.load_program_to_ram(app.BOOST)
    while True:
        output = app.process(False)
        if type(output) is int:
            print(f"[OUTPUT] {output}")
        if not output: break


if __name__ == "__main__":
    main()
    