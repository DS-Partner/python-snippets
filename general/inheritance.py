class Calculator:
    def add(self, x, y):
        return x + y
      
class ScientificCalculator(Calculator):
    def exponential(self, x, n):
        return x**n 
      
my_cal = ScientificCalculator()
my_cal.add(3, 5)
my_cal.exponential(2, 5)
