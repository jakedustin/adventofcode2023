from day1.DayOneSolution import DayOneSolution as day_one

class SolutionFactory:

    @staticmethod
    def create_solver(solver_type, input_data):
        if solver_type == 1:
            return day_one(input_data)
        else:
            raise ValueError("That solution has not been implemented yet.")