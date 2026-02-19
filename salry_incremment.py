rating = int(input("Enter performance rating (1-5): "))
experience = int(input("Enter years of experience: "))
attendance = float(input("Enter attendance percentage: "))

increment = 0

# Base increment from rating
if rating == 5:
    increment = 20
elif rating == 4:
    increment = 15
elif rating == 3:
    increment = 10
elif rating == 2:
    increment = 5
else:
    increment = 0

# Experience bonus
if experience >= 10:
    increment += 10
elif experience >= 5:
    increment += 5

# Attendance adjustment
if attendance >= 95:
    increment += 5
elif attendance >= 85:
    increment += 2
elif attendance < 75:
    increment -= 5

print("Total Increment Percentage:", increment, "%")
