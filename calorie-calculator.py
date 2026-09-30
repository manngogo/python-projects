# Estimate daily calorie and macronutrient targets.

ACTIVITY_FACTORS = {
	1: (1.2, "Sedentary — little to no exercise"),
	2: (1.375, "Lightly active — light exercise 1–3 days/week"),
	3: (1.55, "Moderately active — exercise 3–5 days/week"),
	4: (1.725, "Very active — hard exercise 6–7 days/week"),
	5: (1.9, "Extremely active — physical labor or heavy training"),
}


def _read_number(prompt, minimum=0):
	while True:
		try:
			value = float(input(prompt))
			if value <= minimum:
				print(f"Enter a number greater than {minimum}.")
				continue
			return value
		except ValueError:
			print("Enter a valid number.")


def get_user_inputs():
	# Prompt for measurements, biological sex, activity, and goal.
	weight = _read_number("Weight (pounds): ")
	feet = _read_number("Height — feet: ", minimum=-1)
	inches = _read_number("Additional inches (0–11): ", minimum=-1)
	while inches >= 12:
		print("Inches must be less than 12.")
		inches = _read_number("Additional inches (0–11): ", minimum=-1)
	age = _read_number("Age (years): ")

	while True:
		sex = input("Biological sex for the Mifflin-St Jeor equation (male/female): ").strip().lower()
		if sex in ("male", "female"):
			break
		print("Enter male or female.")

	print("Activity level:")
	for number, (_, description) in ACTIVITY_FACTORS.items():
		print(f"  {number}. {description}")
	while True:
		try:
			activity_level = int(input("Choose 1–5: "))
			if activity_level in ACTIVITY_FACTORS:
				break
		except ValueError:
			pass
		print("Choose a whole number from 1 to 5.")

	goals = {"1": "lose", "2": "maintain", "3": "gain"}
	while True:
		choice = input("Goal — 1) lose, 2) maintain, 3) gain: ").strip().lower()
		if choice in goals:
			goal = goals[choice]
			break
		if choice in ("lose", "maintain", "gain"):
			goal = choice
			break
		print("Choose lose, maintain, or gain (or 1, 2, or 3).")

	return weight, feet * 12 + inches, age, sex, activity_level, goal


def calculate_tdee(weight, height, age, sex, activity_level):
	# Return estimated BMR and maintenance calories from US measurements.
	weight_kg = weight * 0.453592
	height_cm = height * 2.54
	sex = sex.strip().lower()
	if sex == "male":
		bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
	elif sex == "female":
		bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
	else:
		raise ValueError("sex must be 'male' or 'female'")

	try:
		factor = ACTIVITY_FACTORS[int(activity_level)][0]
	except (KeyError, ValueError, TypeError):
		raise ValueError("activity_level must be an integer from 1 to 5") from None
	return bmr, bmr * factor


def calculate_macros(tdee, goal):
	# Return calorie target and balanced macro grams for the selected goal.
	goal = goal.strip().lower()
	adjustments = {"lose": -400, "maintain": 0, "gain": 350}
	if goal not in adjustments:
		raise ValueError("goal must be 'lose', 'maintain', or 'gain'")
	target_calories = max(0, tdee + adjustments[goal])
	return {
		"goal": goal,
		"calories": target_calories,
		"protein_g": target_calories * 0.30 / 4,
		"fat_g": target_calories * 0.30 / 9,
		"carbohydrate_g": target_calories * 0.40 / 4,
	}


def main():
	weight, height, age, sex, activity_level, goal = get_user_inputs()
	bmr, tdee = calculate_tdee(weight, height, age, sex, activity_level)
	summary = calculate_macros(tdee, goal)
	print("\nEstimated daily targets (not medical advice):")
	print(f"BMR: {bmr:.0f} calories/day")
	print(f"Maintenance (TDEE): {tdee:.0f} calories/day")
	print(f"Target: {summary['calories']:.0f} calories/day ({goal})")
	print(f"Protein: {summary['protein_g']:.0f} g")
	print(f"Fat: {summary['fat_g']:.0f} g")
	print(f"Carbohydrates: {summary['carbohydrate_g']:.0f} g")


if __name__ == "__main__":
	main()
