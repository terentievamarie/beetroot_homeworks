class Mathematician:

     @staticmethod
     def square_nums(numbers):
         return [num**2 for num in numbers]

     @staticmethod
     def remove_positives(numbers):
         return [num for num in numbers if num<0]

     @staticmethod
     def filter_leaps(years):
         def is_leap_year(year):
             return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

         return [year for year in years if is_leap_year(year)]