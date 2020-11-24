#averageSalary

class Solution:
    def average(self, salary: List[int]) -> float:
        a = 0
        salary.sort()
        salary.pop(-1)
        salary.pop(0)
        for i in salary:
            a += i
        a = a/len(salary)
        return a
            
        