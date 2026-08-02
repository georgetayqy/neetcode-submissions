class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # condition is close < open always
        # BFS?

        if n == 1:
            return ["()"]

        start = [(n, n, "")]
        all_parenthesis = []

        while start:
            current = start.pop()
            left, right, parenthesis = current

            if left < 0 or right < 0:
                continue

            if left == right and left == 0:
                all_parenthesis.append(parenthesis)
            elif right == left:
                start.append((left - 1, right, parenthesis + "("))
            else:
                # if opening (left) > close (right), we can add as many closing
                # as we want
                if left - 1 >= 0:
                    start.append((left - 1, right, parenthesis + "("))
                
                if right - 1 >= 0:
                    start.append((left, right - 1, parenthesis + ")"))

        return all_parenthesis
