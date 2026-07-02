months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Dictionary to map month name → number
month_to_num = {name: i + 1 for i, name in enumerate(months)}

while True:
    try:
        date_input = input("Date: ").strip()  # remove extra spaces

        # Try numeric format: month/day/year
        if "/" in date_input:
            month_str, day_str, year_str = date_input.split("/")
            month = int(month_str)
            day = int(day_str)
            year = int(year_str)

        # Try textual format: Month day, year
        else:
            # Example: "September 8, 1636"
            parts = date_input.replace(",", "").split()  # remove comma and split
            month_name, day_str, year_str = parts
            month = month_to_num.get(month_name)  # convert name to number
            if month is None:
                raise ValueError("Invalid month name")
            day = int(day_str)
            year = int(year_str)

        # Optional: check ranges (1–12 for month, 1–31 for day)
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError("Month or day out of range")

        # If everything is valid, print formatted output
        print(f"{year}-{month:02d}-{day:02d}")
        break  # exit loop

    except (ValueError, IndexError):
        continue  # invalid input → prompt again