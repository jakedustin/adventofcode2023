from day1.DayOneSolution import DayOneSolution as day_one
from day2.DayTwoSolution import DayTwoSolution as day_two

class SolutionFactory:

    @staticmethod
    def create_solver(solver_type, input_data):
        if solver_type == 1:
            return day_one(input_data)
        elif solver_type == 2:
            return day_two(input_data)
        else:
            raise ValueError("That solution has not been implemented yet.")