from typing import List

class TestCase(object):
    def __init__(self, _input, _output):
        self.input = _input
        self.output = _output

def runTest(test_case: TestCase, solutionFn, debug):
    result = solutionFn(*test_case.input)
    if (debug):
        print("INPUT:")
        for i in test_case.input:
            print (i)
        print("\nRUNNING TEST...")
        print("\nRESULT:")
        print (result)
        print("\nOUTPUT:")
        for i in test_case.output:
            print (i)
    if result == test_case.output:
        return True
    else:
        return False

def runAllTests(test_cases: List[TestCase], solutionFn, debug=False):
    for (test_num, test) in enumerate(test_cases):
       result = "passed" if runTest(test, solutionFn, debug) else "failed"
       print(f"test {test_num} -> {result}")
