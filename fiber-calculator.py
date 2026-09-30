# Calculate a recommended daily fiber intake.

def calculate_fiber(age: int, sex: str, calories: float | None = None) -> float:
	# Estimate fiber grams/day from age, sex, or calorie intake.
	#
	# Uses 25 g/day for women and 38 g/day for men through age 50, and
	# 21 g/day for women and 30 g/day after age 50. If calories are provided,
	# uses the alternative guideline of about 14 g per 1,000 calories.
	if age < 0:
		raise ValueError("Age must be zero or greater.")
	if calories is not None:
		if calories < 0:
			raise ValueError("Calories must be zero or greater.")
		return calories * 14 / 1000

	normalized_sex = sex.strip().lower()
	if normalized_sex in ("woman", "women", "female"):
		return 21 if age > 50 else 25
	if normalized_sex in ("man", "men", "male"):
		return 30 if age > 50 else 38
	raise ValueError("Enter woman or man for sex.")


def main() -> None:
	print("Recommended Daily Fiber Intake")
	try:
		age = int(input("Age: "))
		sex = input("Sex (woman/man): ")
		calorie_text = input("Daily calories (optional; press Enter to skip): ").strip()
		calories = float(calorie_text) if calorie_text else None
		target = calculate_fiber(age, sex, calories)
	except ValueError as error:
		print(f"Invalid input: {error}")
		return

	print(f"Recommended daily fiber: {target:g} grams")


if __name__ == "__main__":
	main()
