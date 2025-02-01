# Get user input (case insensitive)
input_test = input("Enter names of people you met in the last 24 hours (separated by spaces): ").lower()

# Define the list of names to check
names_to_check = ["john", "jordan", "mary", "rose"]

# Check for each name separately and print only the corresponding confirmation
for name in names_to_check:
    if name in input_test:
        print(f"{name.capitalize()} in input: True")
        print(f"✅ True! You met {name.capitalize()} in the last 24 hours!")
        break  # Stop checking after finding the first match
else:
    print("No recognized names found.")
