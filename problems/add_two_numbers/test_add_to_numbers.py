#!/usr/bin/env python3
#
# Difficulty: Medium
# Date:       2025-05-19
# Problem:    Add two numbers
# Link:       https://leetcode.com/problems/add-two-numbers//description/

from lib.list_node import ListNode
from problems.add_two_numbers.solution import Solution

def test_add_two_numbers():
    sol = Solution()
    assert sol.addTwoNumbers(ListNode.from_list([2,4,3]), ListNode.from_list([5,6,4])) == [7,0,8]
    assert sol.addTwoNumbers(ListNode.from_list([0]), ListNode.from_list([0])) == [0]
    assert sol.addTwoNumbers(ListNode.from_list([9,9,9,9,9,9,9]), ListNode.from_list([9,9,9,9])) == [8,9,9,9,0,0,0,1]
    assert sol.addTwoNumbers(ListNode.from_list([2,4,9]), ListNode.from_list([5,6,4,9])) == [7,0,4,0,1]
