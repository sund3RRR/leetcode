#!/usr/bin/env python3
#
# Difficulty: Medium
# Date:       2025-05-19
# Problem:    Add two numbers
# Link:       https://leetcode.com/problems/add-two-numbers//description/

from lib.list_node import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        acc = 0
        while l1 is not None:
            # Add l2 if it exists
            if l2 is not None:
                l1.val += l2.val
                l2 = l2.next
            # Add acc if it exists
            if acc == 1:
                l1.val += acc
            acc = 0
            # Check for carry
            if l1.val >= 10:
                acc = 1
                l1.val %= 10
            # Deal with next if l1 is done
            if l1.next is None:
                # Swap lists if l2 is not done
                if l2 is not None:
                    l1.next = l2
                    l2 = None
                # Add carry if both lists is done
                elif acc == 1:
                    l1.next = ListNode(1)
                    acc = 0
            # Move to next
            l1 = l1.next
        return head
