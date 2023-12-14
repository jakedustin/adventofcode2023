from BaseSolution import BaseSolution


class DayOneSolution(BaseSolution):
    table = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    # def solve(self):
    #     total = 0
    #     for s in self.input_data:
    #         print(s)
    #         n = ''.join(c for c in s if c.isdigit())
    #         print(n[0] + "," + n[-1])
    #         n = n[0] + n[-1]
    #         total += int(n)
    #     return total

    def solve(self):
        # find first digit
        # parser to find string representations of digits
        total = 0
        for s in self.input_data:
            digits = ""
            for i in range(len(s)):
                if s[i].isdigit():
                    digits += s[i]
                else:
                    if i + 5 < len(s):
                        if s[i:-1].find("three") == 0:
                            digits += "3"
                        elif s[i:-1].find("seven") == 0:
                            digits += "7"
                        elif s[i:-1].find("eight") == 0:
                            digits += "8"
                    if i + 4 < len(s):
                        if s[i:-1].find("four") == 0:
                            digits += "4"
                        elif s[i:-1].find("five") == 0:
                            digits += "5"
                        elif s[i:-1].find("nine") == 0:
                            digits += "9"
                    if i + 3 < len(s):
                        if s[i:-1].find("one") == 0:
                            digits += "1"
                        elif s[i:-1].find("two") == 0:
                            digits += "2"
                        elif s[i:-1].find("six") == 0:
                            digits += "6"

            total += int(digits[0] + digits[-1])

        return total

    def get_file_name(self):
        return "day1/"
