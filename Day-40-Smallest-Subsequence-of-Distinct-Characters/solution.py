class Solution(object):
    def smallestSubsequence(self, s):
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        visited = set()
        
        for i, c in enumerate(s):
            if c in visited:
                continue
                
            while stack and stack[-1] > c and last_occurrence[stack[-1]] > i:
                visited.remove(stack.pop())
                
            stack.append(c)
            visited.add(c)
            
        return "".join(stack)
