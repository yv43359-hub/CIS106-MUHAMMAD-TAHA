# Session 13 - Classes and Objects

# -----------------------------
# Problem 1 - Employee Class
# -----------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def compute_bonus(self, bonus_rate):
        bonus = self.salary * bonus_rate
        return bonus


# Testing Employee Class
emp1 = Employee("Taha", 5000)

bonus_rate = float(input("Enter bonus rate for employee: "))

bonus_amount = emp1.compute_bonus(bonus_rate)

print("Employee Name:", emp1.name)
print("Salary:", emp1.salary)
print("Bonus Amount:", bonus_amount)


print("\n-----------------------------\n")


# -----------------------------
# Problem 2 - Student Class
# -----------------------------

class Student:

    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):

        if self.district_code == "I":
            tuition = self.enrolled_credits * 250
        else:
            tuition = self.enrolled_credits * 500

        return tuition


# Testing Student Class

student1 = Student("Ali", "Khan", "I", 12)

tuition_amount = student1.compute_tuition()

print("Student Name:", student1.first_name, student1.last_name)
print("District Code:", student1.district_code)
print("Credits:", student1.enrolled_credits)
print("Tuition Owed: $", tuition_amount)