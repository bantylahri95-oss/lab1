age = int(input("Enter patient age: "))
heart_rate = int(input("Enter heart rate: "))
severe_injury = input("Severe injury? (yes/no): ").lower()

# Define abnormal heart rate
if heart_rate < 60 or heart_rate > 100 or severe_injury == "yes":
    priority = "Critical"
elif age > 65:
    priority = "Moderate (Upgraded Priority due to age)"
else:
    priority = "Normal"

# Upgrade moderate if age > 65
if priority == "Moderate" and age > 65:
    priority = "Critical"

print("Patient Priority Level:", priority)
