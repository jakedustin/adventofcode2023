from SolutionFactory import SolutionFactory as factory

class App:
    short_input = 's'
    long_input = 'l'

    def __init__(self, day, input_type):
        self.day = day
        self.input_type = input_type

    def run(self):
        try:
            solver = factory.create_solver(self.day, self.input_type)
            solution = solver.solve()
            print("Solution: " + str(solution))
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    day = int(input("Enter the day you are attempting to solve: "))
    input_type = input("Test against short or long input (s/l)? ")
    # day = 1
    # input_type = "s"
    app = App(day, input_type)
    app.run()