# https://leetcode.com/problems/top-k-frequent-words/
from queue import PriorityQueue
from testRunners import (TestCase, runAllTests)

testCases = [
    TestCase([["i", "love", "leetcode", "i", "love", "coding"], 2],
            ["i", "love"]),
    TestCase([["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4],
            ["the", "is", "sunny", "day"])
]

class WordCount(object):
    def __init__(self, word, count):
        self.word = word
        self.count = count
    def __lt__(self, other):
        return (self.count > other.count) or (self.count == other.count and self.word < other.word)
    def __str__(self):
        return f"({self.count}) {self.word}"

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freqMap = {}
        for w in words:
            count = freqMap.get(w, 0)
            freqMap[w] = count + 1
        q = PriorityQueue()
        for w in freqMap.keys():
            q.put(WordCount(w, freqMap[w]))
        return [q.get().word for i in range(k)]

runAllTests(testCases, Solution().topKFrequent)
