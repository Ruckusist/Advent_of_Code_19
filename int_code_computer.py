import math, time, copy
import grams

class Int_Code_Comp(object):
    def __init__(self, config=None):
        print("Initializing Int Code Computer Ver. day.2")
        self.config = config
        self.pointer = 0
        self.ram = 0

    def load_program_to_ram(self, program, noun=None, verb=None):
        self.ram = [0 for x in range(56000)]  # might need 34463338 ram
        self.pointer = 0
        for i, e in enumerate(program):
            self.ram[i] = e
        if noun: self.ram[1] = noun
        if verb: self.ram[2] = verb

    def operate(self, op_code, input_one, input_one_mode, input_two=None, input_two_mode=None, output=0):
        # time.sleep(.1) 
        if op_code == 99:  # if 99 dump immediatly
            return False
        # DEAL WITH INPUT MODES
        if not input_one_mode:
            one = self.ram[input_one]
        else: one = input_one
        if input_two:
            if not input_two_mode: 
                two = self.ram[input_two]
            else: two = input_two
        # DEAL WITH THE OP CODES
        if op_code == 1:
            self.ram[output] = one + two
        if op_code == 2:
            self.ram[output] = one * two
        if op_code == 3:
            self.ram[input_one] = input("PLEASE INPUT A VARIABLE(1): ") or 1
        if op_code == 4:
            print(f"[OUTPUT] addr 0x{input_one}: {self.ram[input_one]}")
        return True
        
    def run_prog(self, verbose=True):
        exec_loop = 0
        while True:
            operation = str(self.ram[self.pointer])
            if len(operation) <= 2:  # classic operation default modes
                op_code = operation
                input_one_mode = 0  # default
                input_two_mode = 0  # default
                output_mode    = 0  # default  | i dont know if this is a thing..??
                input_one = self.ram[self.pointer+1]
                input_two = self.ram[self.pointer+2]
                output    = self.ram[self.pointer+3]
                # print(f"executing Step #{exec_loop}")
                if self.operate(op_code, input_one, input_one_mode, input_two, input_two_mode, output):
                    self.pointer += 4
                    exec_loop += 1
                    continue
                else:
                    break
            elif len(operation) >= 4:  # new operation mode.
                operators = len(operation)
                op_code = operation[-2:]
                print(f"Evaluating this Operation: {operation}")
                print(f"OP_CODE: {op_code}")
                print(f"INPUT MODE ONE: {operation[1]}")
                print(f"INPUT MODE TWO: {operation[0]}")

                self.pointer += operators
                exit()
        return self.ram[0]
    
    def run_program(self, verbose=True):
        exec_loop = 0
        while True:
            if verbose: print(f"# || # Beginning of Loop # {exec_loop}")
            exec_loop += 1
            operation = str(self.ram[self.pointer])
            operators = len(operation)
            op_code = int(operation[-2:])
            if verbose: print(f"Current State: OP=[{str(self.ram[self.pointer])}] @@ address: 0x{self.pointer}")
            if verbose: print(f"\tOP_CODE: {op_code}")
            if op_code == 99: 
                if verbose: print("OP_CODE: 99 ==> END PROGRAM")
                break
            elif op_code == 3: 
                if verbose: print("OP_CODE: 3 ==> TAKE A USER INPUT.")
                self.ram[self.ram[self.pointer+1]] = int(input("PLEASE INPUT A VARIABLE(1): ")) or 1
                self.pointer += 2
                continue
            elif op_code == 4:
                if verbose: print("OP_CODE: 4 ==> PRINT DATA TO SCREEN")
                print(f"[OUTPUT] data @ address: 0x{self.pointer+1} = {self.ram[self.pointer+1]}")
                print(f"ASSERT {int(self.ram[self.pointer+1])} == 0")
                assert int(self.ram[self.pointer+1]) == 0
                self.pointer += 2 if operators < 2 else operators
                continue

            elif op_code == 1 or op_code == 2:
                if len(operation) == 3:
                    if verbose: print("WILDCARD!! prepending a zero.")
                    input_two_mode = 0
                    input_one_mode = int(operation[0])

                elif len(operation) == 4:  # a more complex action
                    input_one_mode = int(operation[1])
                    input_two_mode = int(operation[0])
                else:
                    input_one_mode = 0
                    input_two_mode = 0
                
                input_one = self.ram[self.pointer+1]
                input_two = self.ram[self.pointer+2]
                output    = self.ram[self.pointer+3]

                # print(f"FULL LIN
                # E: {operation}, {input_one}, {input_two}, {output}" )
                # print(f"in_1_mode = {input_one_mode}")
                if not input_one_mode:
                    one = int(self.ram[input_one])
                else: 
                    one = int(input_one)

                if not input_two_mode:
                    two = int(self.ram[input_two])
                else: 
                    two = int(input_two)
                
                if op_code == 1:
                    if verbose: print("OP_CODE: 1 ==> ADDITION.")
                    self.ram[output] = one + two
                    
                if op_code == 2:
                    if verbose: print("OP_CODE: 2 ==> MULITPLY.")
                    self.ram[output] = one * two
                    
                print(f"output addr 0x{output} ==> {self.ram[output]}")
                self.pointer += operators if operators > 2 else 4
                
            else:
                print("BAD OP CODE>>> WTF> OVER")
                exit()
            time.sleep(.25)
        return self.ram[0]


    def main(self):
        for program_name, program in grams.programs.items():
            print(f"starting Work on {program_name} Debug")
            if program_name is "day2": 
                continue
                print("need to find correct Noun Verb combo for Output: 19690720")
                self.load_program_to_ram(program, 12, 2)
                standard_value = self.run_program()
                print(f"this program Runs Standard with an output of: {standard_value}")
                for noun in range(100):
                    for verb in range(100):
                        self.ram = None
                        self.load_program_to_ram(program, noun, verb)
                        if self.run_program() == 19690720:
                            print(f"Found it! Verb: {verb} | Noun: {noun}")
                            ans = (100*verb)+noun
                            print(f"Answer is {ans}")

            if program_name.endswith("day5"):
                # continue
                # print("When 1 is the only input what is the output?")
                self.load_program_to_ram(program)
                standard_value = self.run_program()
                # break


if __name__ == "__main__":
    app = Int_Code_Comp()
    app.main()