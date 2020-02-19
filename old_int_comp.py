import math, time, copy
import grams

class Int_Code_Comp(object):
    """
    This is updated to handle all inputs until day 9.
    """
    def __init__(self, config=None, manual_input=True):
        print("Initializing Int Code Computer Ver. day.5")
        self.config = config
        self.manual_input = manual_input
        self.pointer = 0
        self.input = 0
        self.ram = 0
        self.day2 = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,9,19,23,2,23,10,27,1,6,27,31,1,31,6,35,2,35,10,39,1,39,5,43,2,6,43,47,2,47,10,51,1,51,6,55,1,55,6,59,1,9,59,63,1,63,9,67,1,67,6,71,2,71,13,75,1,75,5,79,1,79,9,83,2,6,83,87,1,87,5,91,2,6,91,95,1,95,9,99,2,6,99,103,1,5,103,107,1,6,107,111,1,111,10,115,2,115,13,119,1,119,6,123,1,123,2,127,1,127,5,0,99,2,14,0,0]
        self.test = [[104,1125899906842624,99], [1102,34915192,34915192,7,4,7,99,0], [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]]
        self.TEST = [3,225,1,225,6,6,1100,1,238,225,104,0,101,14,135,224,101,-69,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,102,90,169,224,1001,224,-4590,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1102,90,45,224,1001,224,-4050,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,1001,144,32,224,101,-72,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,36,93,225,1101,88,52,225,1002,102,38,224,101,-3534,224,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1102,15,57,225,1102,55,49,225,1102,11,33,225,1101,56,40,225,1,131,105,224,101,-103,224,224,4,224,102,8,223,223,1001,224,2,224,1,224,223,223,1102,51,39,225,1101,45,90,225,2,173,139,224,101,-495,224,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1101,68,86,224,1001,224,-154,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,344,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,359,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,374,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,389,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,404,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,419,101,1,223,223,1007,677,226,224,1002,223,2,223,1006,224,434,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,449,101,1,223,223,8,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,479,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,677,677,224,102,2,223,223,1006,224,509,101,1,223,223,1008,677,677,224,102,2,223,223,1005,224,524,1001,223,1,223,107,226,226,224,1002,223,2,223,1005,224,539,101,1,223,223,7,226,226,224,102,2,223,223,1005,224,554,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,569,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,584,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,108,226,226,224,1002,223,2,223,1005,224,614,101,1,223,223,1008,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,644,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,659,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226]
        self.BOOST = [1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,0,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1101,0,38,1019,1102,1,37,1008,1101,252,0,1023,1102,24,1,1004,1102,35,1,1017,1101,0,28,1011,1101,0,36,1003,1102,30,1,1013,1101,0,0,1020,1102,1,1,1021,1102,897,1,1028,1101,20,0,1000,1101,0,22,1005,1102,29,1,1007,1101,0,34,1009,1102,1,259,1022,1101,310,0,1025,1102,892,1,1029,1101,21,0,1014,1102,1,315,1024,1101,0,33,1002,1102,31,1,1015,1102,190,1,1027,1102,1,39,1001,1101,26,0,1010,1101,27,0,1016,1102,1,23,1018,1101,0,32,1012,1101,0,25,1006,1102,1,197,1026,109,34,2106,0,-7,1001,64,1,64,1106,0,199,4,187,1002,64,2,64,109,-22,2108,34,-3,63,1005,63,221,4,205,1001,64,1,64,1106,0,221,1002,64,2,64,109,-10,1208,-1,42,63,1005,63,237,1106,0,243,4,227,1001,64,1,64,1002,64,2,64,109,20,2105,1,1,1001,64,1,64,1105,1,261,4,249,1002,64,2,64,109,1,21108,40,40,-6,1005,1017,283,4,267,1001,64,1,64,1105,1,283,1002,64,2,64,109,7,1205,-9,301,4,289,1001,64,1,64,1105,1,301,1002,64,2,64,109,-1,2105,1,-5,4,307,1106,0,319,1001,64,1,64,1002,64,2,64,109,-8,1206,0,331,1105,1,337,4,325,1001,64,1,64,1002,64,2,64,109,-6,21108,41,38,0,1005,1015,353,1105,1,359,4,343,1001,64,1,64,1002,64,2,64,109,11,1206,-6,377,4,365,1001,64,1,64,1106,0,377,1002,64,2,64,109,1,21101,42,0,-8,1008,1019,42,63,1005,63,399,4,383,1105,1,403,1001,64,1,64,1002,64,2,64,109,-29,1202,6,1,63,1008,63,24,63,1005,63,425,4,409,1106,0,429,1001,64,1,64,1002,64,2,64,109,14,1201,-3,0,63,1008,63,34,63,1005,63,451,4,435,1105,1,455,1001,64,1,64,1002,64,2,64,109,10,21101,43,0,-9,1008,1013,41,63,1005,63,475,1106,0,481,4,461,1001,64,1,64,1002,64,2,64,109,-17,2101,0,0,63,1008,63,21,63,1005,63,501,1106,0,507,4,487,1001,64,1,64,1002,64,2,64,109,-5,2107,21,5,63,1005,63,525,4,513,1105,1,529,1001,64,1,64,1002,64,2,64,109,13,1202,-7,1,63,1008,63,26,63,1005,63,553,1001,64,1,64,1106,0,555,4,535,1002,64,2,64,109,5,21107,44,45,-8,1005,1010,573,4,561,1105,1,577,1001,64,1,64,1002,64,2,64,109,-6,21102,45,1,7,1008,1019,45,63,1005,63,603,4,583,1001,64,1,64,1105,1,603,1002,64,2,64,109,-15,1207,10,28,63,1005,63,623,1001,64,1,64,1106,0,625,4,609,1002,64,2,64,109,8,2108,37,-4,63,1005,63,645,1001,64,1,64,1105,1,647,4,631,1002,64,2,64,109,6,21102,46,1,1,1008,1012,44,63,1005,63,671,1001,64,1,64,1106,0,673,4,653,1002,64,2,64,109,4,1207,-6,35,63,1005,63,695,4,679,1001,64,1,64,1106,0,695,1002,64,2,64,109,1,2107,38,-8,63,1005,63,715,1001,64,1,64,1105,1,717,4,701,1002,64,2,64,109,-23,1208,10,36,63,1005,63,739,4,723,1001,64,1,64,1105,1,739,1002,64,2,64,109,4,2102,1,7,63,1008,63,24,63,1005,63,765,4,745,1001,64,1,64,1105,1,765,1002,64,2,64,109,13,2102,1,-4,63,1008,63,22,63,1005,63,789,1001,64,1,64,1105,1,791,4,771,1002,64,2,64,109,-8,1201,5,0,63,1008,63,32,63,1005,63,811,1106,0,817,4,797,1001,64,1,64,1002,64,2,64,109,11,1205,7,829,1105,1,835,4,823,1001,64,1,64,1002,64,2,64,109,-1,2101,0,-6,63,1008,63,25,63,1005,63,857,4,841,1106,0,861,1001,64,1,64,1002,64,2,64,109,8,21107,47,46,-9,1005,1011,877,1106,0,883,4,867,1001,64,1,64,1002,64,2,64,109,9,2106,0,-1,4,889,1106,0,901,1001,64,1,64,4,64,99,21101,0,27,1,21102,915,1,0,1105,1,922,21201,1,59500,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,0,942,0,1105,1,922,21201,1,0,-1,21201,-2,-3,1,21101,0,957,0,1105,1,922,22201,1,-1,-2,1105,1,968,21201,-2,0,-2,109,-3,2105,1,0]
        self.paint = [3,8,1005,8,299,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,28,1006,0,85,1,106,14,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,58,1,1109,15,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,84,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,105,1006,0,48,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,130,1006,0,46,1,1001,17,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,160,2,109,20,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,185,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,207,1006,0,89,2,1002,6,10,1,1007,0,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,241,2,4,14,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,267,1,1107,8,10,1,109,16,10,2,1107,4,10,101,1,9,9,1007,9,1003,10,1005,10,15,99,109,621,104,0,104,1,21101,0,387239486208,1,21102,316,1,0,1106,0,420,21101,0,936994976664,1,21102,327,1,0,1105,1,420,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,1,29192457307,1,21102,1,374,0,1106,0,420,21101,0,3450965211,1,21101,0,385,0,1106,0,420,3,10,104,0,104,0,3,10,104,0,104,0,21102,1,837901103972,1,21101,408,0,0,1106,0,420,21102,867965752164,1,1,21101,0,419,0,1105,1,420,99,109,2,22102,1,-1,1,21102,40,1,2,21102,451,1,3,21102,1,441,0,1106,0,484,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,446,447,462,4,0,1001,446,1,446,108,4,446,10,1006,10,478,1102,0,1,446,109,-2,2105,1,0,0,109,4,1201,-1,0,483,1207,-3,0,10,1006,10,501,21101,0,0,-3,22101,0,-3,1,22102,1,-2,2,21101,1,0,3,21101,520,0,0,1106,0,525,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,548,2207,-4,-2,10,1006,10,548,21201,-4,0,-4,1105,1,616,22101,0,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,0,567,0,1106,0,525,22101,0,1,-4,21101,1,0,-1,2207,-4,-2,10,1006,10,586,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,608,21202,-1,1,1,21102,608,1,0,106,0,483,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]

    def load_program_to_ram(self, program, noun=None, verb=None):
        self.ram = [0 for x in range(56000)]  # might need 34463338 ram
        self.pointer = 0
        for i, e in enumerate(program):
            self.ram[i] = e
        print("Finished Loading Program to RAM")
        print(f"Initial Program len is {len(self.ram)}")
        if noun: self.ram[1] = noun
        if verb: self.ram[2] = verb

    def process(self, verbose=True):
        op_code = int(str(self.ram[self.pointer])[-2:])
        if verbose: print(f"P: {self.pointer} | OP: {self.ram[self.pointer]}")
        if op_code is 99: return False
        if op_code is  1: return self.op_one(verbose)
        if op_code is  2: return self.op_two(verbose)
        if op_code is  3: return self.op_three(verbose)
        if op_code is  4: return self.op_four(verbose)
        if op_code is  5: return self.op_five(verbose)
        if op_code is  6: return self.op_six(verbose)
        if op_code is  7: return self.op_seven(verbose)
        if op_code is  8: return self.op_eight(verbose)
        if op_code is  9: return self.op_nine(verbose)
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

    def op_three(self, verbose=True, INPUT=False):
        operation = str(self.ram[self.pointer])
        if len(operation) < 5:
            operation = "0"*(5-len(operation)) + operation
        op_code = int(operation[-2:])
        var_1_mode = int(operation[2])
        input_one = int(self.ram[self.pointer+1])
        if var_1_mode == 0: one = input_one
        if var_1_mode == 2: one = input_one + self.ram[-1]
        if not INPUT:
            self.ram[one] = int(input("PLEASE INPUT A VARIABLE(1): ")) or 1
        else: self.ram[self.input]
        self.pointer += 2
        return True

    def op_four(self, verbose=True): 
        operation = str(self.ram[self.pointer])
        if len(operation) < 5:
            operation = "0"*(5-len(operation)) + operation
        op_code = int(operation[-2:])
        var_1_mode = int(operation[2])
        input_one = int(self.ram[self.pointer+1])
        if var_1_mode == 0: one = input_one
        if var_1_mode == 1: one = self.ram[input_one]
        if var_1_mode == 2: one = input_one + self.ram[-1]
        if verbose: print(f"[OUTPUT] 0x{one} ==> {self.ram[one]}")
        self.pointer += 2
        # self.input = self.ram[one]  # this is wrong! only here to not do again.
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
        if verbose: print(f"\tDoes {one} == 0 ?? {one == 0} | if False pointer = {two} else {self.pointer + 3}")
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

        if verbose: print(f"\tGot opcode 5 | {operation} | Jump-If-True")
        if verbose: print(f"\tFULL LINE: {operation}, {input_one}, {input_two}" )
        if verbose: print(f"\tin_1_mode = {var_1_mode}")
        if verbose: print(f"\tin_2_mode = {var_2_mode}")
        if verbose: print(f"\tDoes {one} == 0 ?? {one == 0} | if False pointer = {two} else {self.pointer + 3}")
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

if __name__ == "__main__":
    app = Int_Code_Comp()
    app.load_program_to_ram(app.BOOST)
    while True:
        if not app.again(False): break