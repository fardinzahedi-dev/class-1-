import csv

daily_calories = {}
max_cal_food = ""
max_calories = 0
max_protein_food = ""
max_protein = 0

with open('meals.csv', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        date = row['date']
        food = row['food']
        calories = int(row['calories'])
        protein = int(row['protein_g'])

        # Track calories per day
        if date not in daily_calories:
            daily_calories[date] = 0
        daily_calories[date] += calories

        # Food with most calories
        if calories > max_calories:
            max_calories = calories
            max_cal_food = food

        # Food with most protein
        if protein > max_protein:
            max_protein = protein
            max_protein_food = food

# Find day with most calories
max_day = max(daily_calories, key=daily_calories.get)

print("\n--- Calorie Analytics ---")

print("\nCalories per day:")
for day, cal in daily_calories.items():
    print(day, ":", cal)

print("\nDay with most calories:", max_day, "-", daily_calories[max_day])
print("Food with most calories:", max_cal_food, "-", max_calories)
print("Food with most protein:", max_protein_food, "-", max_protein)
