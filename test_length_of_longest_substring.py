#!/usr/bin/env python3
#
# Difficulty: Medium
# Date:       2025-05-19
# Problem:    Longest Substring Without Repeating Characters
# Link:       https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from length_of_longest_substring import Solution

def test_length_of_longest_substring():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring(" ") == 1
    assert sol.lengthOfLongestSubstring("dvdf") == 3
