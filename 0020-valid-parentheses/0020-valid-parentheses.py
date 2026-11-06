class Solution(object):
    def isValid(self, s):
        stack = []

        map = {")" : "(", "}" : "{", "]" : "["}

        for char in s:
            if char in map:
                top_element = stack.pop() if stack else '#'

                if map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
        