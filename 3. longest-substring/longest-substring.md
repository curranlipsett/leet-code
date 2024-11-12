Given a string s, find the length of the longest substring without repeating characters.

Substring
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Notes:
- Looking for the longest substring that doesn't have a repeated character, the alphabetical 
order is not relevant. In example 3, wke is correct because the first 3 characters, pww have
a w repeated, so that length is 2. wke is the longest substring, and ends because of the w at 
end of the whole string