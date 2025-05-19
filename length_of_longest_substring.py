#!/usr/bin/env python3
#
# Difficulty: Medium
# Date:       2025-05-19
# Problem:    Longest Substring Without Repeating Characters
# Link:       https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        max_length = 0
        left = 0
        for i in range(0, len(s)):
            if s[i] in cache:
                max_length = max(max_length, len(cache))
                for j in range(left, i):
                    cache.pop(s[j])
                    if s[j] == s[i]:
                        left = j + 1
                        break
            cache[s[i]] =  None
        return max(max_length, len(cache))
