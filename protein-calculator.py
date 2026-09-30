#Estimate protein intake based on weight, activity level, and health goals.
KG_PER_POUND = 0.45359237

def calculate_protein(weight, unit, category):
	"""Return a (minimum, maximum) daily protein estimate in grams."""
	unit = unit.strip().lower()
	category = category.strip().lower()

	if unit in ("lb", "lbs", "pound", "pounds"):
		weight_kg = weight * KG_PER_POUND
	elif unit in ("kg", "kgs", "kilogram", "kilograms"):
		weight_kg = weight
	else:
		raise ValueError("Unit must be kg or lb.")
	if weight_kg <= 0:
		raise ValueError("Weight must be greater than zero.")

	rates = {
		"sedentary": (0.8, 0.8),
		"active": (1.2, 2.0),
		"older adult": (1.2, 1.6),
		"muscle gain": (1.6, 1.8),
		"weight loss": (2.0, 2.4),
		"calorie deficit": (2.0, 2.4),
		"advanced/high volume": (2.2, 2.64),
		"glp-1": (1.2, 1.6),
	}
	if category not in rates:
		raise ValueError("Category must be sedentary, active, older adult, muscle gain, weight loss, calorie deficit, advanced/high volume, or GLP-1.")
	low_rate, high_rate = rates[category]
	return weight_kg * low_rate, weight_kg * high_rate


def ask_yes_no(question):
	"""Ask a yes/no question and return True/False."""
	while True:
		answer = input(f"{question} (yes/no): ").strip().lower()
		if answer in ("yes", "y"):
			return True
		if answer in ("no", "n"):
			return False
		print("Please answer yes or no.")


def determine_category():
	"""Ask a few yes/no questions and infer the best fit category."""
	if ask_yes_no("Are you taking a GLP-1 medication such as semaglutide or tirzepatide?"):
		return "glp-1"
	if ask_yes_no("Are you age 65 or older?"):
		return "older adult"
	if ask_yes_no("Are you trying to build muscle or gain strength?"):
		return "muscle gain"
	if ask_yes_no("Are you trying to lose weight or following a calorie deficit?"):
		return "weight loss"
	if ask_yes_no("Are you doing very high-volume or advanced training?"):
		return "advanced/high volume"
	if ask_yes_no("Are you regularly active or exercising several times per week?"):
		return "active"
	return "sedentary"


def main():
	print("Daily protein calculator (estimates in grams)")
	try:
		weight = float(input("Weight: "))
		unit = input("Unit (kg/lb): ")
		print("Answer the following yes/no questions to estimate your protein needs.")
		category = determine_category()
		print(f"Estimated category: {category}")
		low, high = calculate_protein(weight, unit, category)
		if low == high:
			print(f"Suggested minimum: {low:.0f} g/day")
		else:
			print(f"Suggested range: {low:.0f}–{high:.0f} g/day")
	except ValueError as error:
		print(f"Invalid input: {error}")
	print("General estimate only; consult a healthcare professional for personal advice.")


if __name__ == "__main__":
	main()
