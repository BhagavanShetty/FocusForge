from session import StudySession

from file_handler import load_data, save_data

from analysis import analyze_data

from visualization import (
    plot_study_time,
    plot_focus_ratings
)

from utils import (
    get_valid_duration,
    get_valid_focus_rating
)


# -----------------------------------
# Add Study Session
# -----------------------------------
def add_study_session():
    print("\n===== ADD STUDY SESSION =====")

    subject = input("Enter subject name: ")

    duration = get_valid_duration()

    status_input = input(
        "Was the session completed? (yes/no): "
    ).lower()

    if status_input == "yes":
        status = "completed"
    else:
        status = "interrupted"

    focus_rating = get_valid_focus_rating()

    session = StudySession(
        subject,
        duration,
        status,
        focus_rating
    )

    data = load_data()

    data.append(session.to_dict())

    save_data(data)

    print("\nStudy session added successfully!\n")


# -----------------------------------
# View All Sessions
# -----------------------------------
def view_sessions():
    data = load_data()

    if not data:
        print("\nNo study sessions found.\n")
        return

    print("\n===== ALL STUDY SESSIONS =====")

    for index, session in enumerate(data, start=1):
        print(f"\nSession {index}")

        print(f"Subject: {session['subject']}")
        print(f"Duration: {session['duration']} minutes")
        print(f"Status: {session['status']}")
        print(f"Focus Rating: {session['focus_rating']}/5")


# -----------------------------------
# Main Menu
# -----------------------------------
def main():
    while True:
        print("\n========== FOCUSFORGE ==========")

        print("1. Add Study Session")
        print("2. View Study Sessions")
        print("3. Analyze Study Data")
        print("4. Plot Study Time Graph")
        print("5. Plot Focus Rating Trend")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_study_session()

        elif choice == "2":
            view_sessions()

        elif choice == "3":
            data = load_data()

            analyze_data(data)

        elif choice == "4":
            data = load_data()

            plot_study_time(data)

        elif choice == "5":
            data = load_data()

            plot_focus_ratings(data)

        elif choice == "6":
            print("\nThank you for using FocusForge!")

            break

        else:
            print("\nInvalid choice. Please try again.")


# -----------------------------------
# Run Program
# -----------------------------------
if __name__ == "__main__":
    main()