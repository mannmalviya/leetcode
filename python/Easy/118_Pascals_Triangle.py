#############################################################################
# LeetCode Problem: 118. Pascal's Triangle                                 #
# Date Solved: August 1st, 2025                                             #
#                                                                           #
# Thought Process:                                                          #
# - My first thought was to use the binomial formula to compute the rows of #
#   Pascal's triangle using the binomial formula (This approach is          #
#   implemented in the formula_approach function below)                     #
# - But the accepted solution is the one in generate(), which uses the      #
#   relation between consecutive rows of Pascal's triangle - the relation   #
#   that each row's elements are the sum of consecutive pairs of elements   #
#   from the previous row, padded with 1 at the start and end               #
#                                                                           #
# Notes:                                                                   #
# - This was a LeetCode Easy. I had already solved this a year ago, but     #
#   solved it again since it was the daily problem                          #
#############################################################################

class Solution:
    def generate(self, numRows):
        pascals_triangle = [[1]]
        prev = [1]

        for c in range(0, numRows-1):
            i = 0
            j = i+1
            l = []
            while(j < len(prev)):
                l.append(prev[i]+prev[j])
                i+=1
                j+=1
            l.insert(0, 1)
            l.append(1)
            prev = l
            pascals_triangle.append(l)

        return(pascals_triangle)

    def fact(self, num):
        fact = 1
        if (num == 0):
            return fact
        for i in range(1,num+1):
            fact = fact * i

        return fact

    def formula_approach(self, numRows):
        pascals_triangle = []

        for i in range(0, numRows):
            row = []
            k = 0
            while k <= i:
                row.append(int(self.fact(i)/(self.fact(k)*self.fact(i-k))))
                k += 1
            pascals_triangle.append(row)

        return pascals_triangle
def main():
    sol = Solution()

    print("1st approach=",sol.generate(5))
    print("formula approach=", sol.formula_approach(5))

    return(sol.generate(5))

if __name__ == "__main__":
    main()
