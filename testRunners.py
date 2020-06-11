from typing import List
from collections import Counter

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
    all_results = []
    for (test_num, test) in enumerate(test_cases):
       result = runTest(test, solutionFn, debug)
       all_results.append(result)
       result_str = "passed" if result else "failed"
       print(f"test {test_num} -> {result_str}")
    total_passed = Counter(all_results)[True]
    print(f"passed {total_passed} out of {len(all_results)}")
