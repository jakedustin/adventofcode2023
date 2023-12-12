from BaseSolution import BaseSolution

class DayTwoSolution(BaseSolution):  

    def solve(self):
        sumOfIndexes = 0
        totalCubes = {'red': 12, 'green': 13, 'blue': 14} 
        for s in self.input_data:
            strippedLine = s.rstrip()
            line = strippedLine.split(": ")
            index = int(line[0].split()[1])
            games = line[1].split("; ")
            cubes = {'red': 0, 'green': 0, 'blue': 0} 
            for game in games:
                cubes = game.split(", ")
                for cube in cubes:
                    cubeList = cube.split()
                    if int(cubeList[0]) > cubes[cubeList[1]]:
                        cubes[cubeList[1]] = int(cubeList[0])

            possible = True
            for color in totalCubes.keys():
                if cubes[color] < totalCubes[color]:
                    possible = False
                    break
            if possible:
                sumOfIndexes += index

        return sumOfIndexes
    
    def get_file_name(self):
        return "day2/"