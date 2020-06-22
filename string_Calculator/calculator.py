import re
import logging
import time

regex = re.compile(r'\d+') 

logging.basicConfig(filename = "string_Calculator/calculator.py", level=logging.DEBUG, format="%(asctime)s %(message)s")
logger = logging.getLogger()

class StringCalculator():
    def __init__(self,numbers):
        self.numbers = numbers
    
    def add(self, selfnumbers):
        if len(numbers) == 0:
            return 0
        else:
            string_values = re.findall(r"\d+|-\d+", numbers)
            print(string_values)
            total = 0
            negatives = []
            for i in range(len(string_values)):
                if int(string_values[i]) < 0:
                    logger.info("A negative number: " + string_values[i] + " was found")
                    negatives.append(string_values[i])
                    continue
                if int(string_values[i]) <= 1000:
                    total += int(string_values[i])
            if len(negatives) == 0:
                return total
            else:
                negative_values_string = ""
                for i in range(len(negatives)):
                    if i != len(negatives) - 1:
                        negative_values_string += negatives[i] + ","
                    else:
                        negative_values_string += negatives[i]
                raise Exception("negatives not allowed " + negative_values_string)


def main():
    calculator = StringCalculator()
    print(calculator.add("//4\n142"))
if __name__ == '__main__':
    main()
