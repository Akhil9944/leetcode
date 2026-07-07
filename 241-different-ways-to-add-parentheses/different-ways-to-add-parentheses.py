class Solution(object):
    def diffWaysToCompute(self, expression):
        memo = {}

        def solve(exp):
            if exp in memo:
                return memo[exp]

            res = []

            for i in range(len(exp)):
                if exp[i] in "+-*":
                    left = solve(exp[:i])
                    right = solve(exp[i + 1:])

                    for l in left:
                        for r in right:
                            if exp[i] == "+":
                                res.append(l + r)
                            elif exp[i] == "-":
                                res.append(l - r)
                            else:  # '*'
                                res.append(l * r)

           
            if not res:
                res.append(int(exp))

            memo[exp] = res
            return res

        return solve(expression)