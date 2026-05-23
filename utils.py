def get_valid_duration():
    while True:
        try:
            duration = int(input("Enter study duration (minutes): "))

            if duration <= 0:
                print("Duration must be greater than 0.")
            else:
                return duration

        except ValueError:
            print("Please enter a valid number.")


def get_valid_focus_rating():
    while True:
        try:
            rating = int(input("Rate your focus level (1-5): "))

            if 1 <= rating <= 5:
                return rating
            else:
                print("Focus rating must be between 1 and 5.")

        except ValueError:
            print("Please enter a valid number.")