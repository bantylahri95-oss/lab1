# Input
percentage = float(input("Enter 12th grade percentage: "))
maths = input("Did the student study Mathematics? (yes/no): ").lower()
entrance_score = float(input("Enter entrance exam score: "))

eligible = True

# Check conditions one by one
if percentage < 75:
    print("Not Eligible: Minimum 75% required in 12th grade.")
    eligible = False

if maths != "yes":
    print("Not Eligible: Mathematics is mandatory.")
    eligible = False

if entrance_score < 80:
    print("Not Eligible: Entrance exam score must be at least 80.")
    eligible = False

# Final result
if eligible:
    print("✅ Student is Eligible for Admission.")
