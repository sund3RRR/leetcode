#!/usr/bin/env python3
#
# Difficulty: Easy
# Date:       2025-04-26
# Problem:    Two Sum
# Link:       https://leetcode.com/problems/two-sum/description/

class Solution:
    def two_sum(self, arr: list[int], target: int) -> list[int]:
        cache = {}
        for i, num in enumerate(arr):
            if target - num in cache:
                return [cache[target-num], i]
            cache[num] = i
        return [0]
