from collections import defaultdict


def analyze_data(data):
    if not data:
        print("\nNo study data available.\n")
        return

    total_time = 0
    completed_sessions = 0

    subject_time = defaultdict(int)
    subject_interruptions = defaultdict(int)
    focus_scores = []

    for session in data:
        total_time += session["duration"]

        subject_time[session["subject"]] += session["duration"]

        focus_scores.append(session["focus_rating"])

        if session["status"] == "completed":
            completed_sessions += 1
        else:
            subject_interruptions[session["subject"]] += 1

    total_sessions = len(data)

    completion_rate = (completed_sessions / total_sessions) * 100

    average_focus = sum(focus_scores) / len(focus_scores)

    most_studied_subject = max(subject_time, key=subject_time.get)

    print("\n========== STUDY ANALYSIS ==========")
    print(f"Total Sessions: {total_sessions}")
    print(f"Total Study Time: {total_time} minutes")
    print(f"Completion Rate: {completion_rate:.2f}%")
    print(f"Average Focus Rating: {average_focus:.2f}/5")
    print(f"Most Studied Subject: {most_studied_subject}")

    print("\n========== SMART INSIGHTS ==========")

    if completion_rate < 50:
        print("- Your completion rate is low.")
        print("- Try shorter study sessions for better consistency.")
    else:
        print("- Great consistency in completing sessions!")

    if average_focus < 3:
        print("- Your focus rating is below average.")
        print("- Consider reducing distractions while studying.")
    else:
        print("- Your focus levels are strong.")

    if subject_interruptions:
        most_interrupted = max(
            subject_interruptions,
            key=subject_interruptions.get
        )

        print(f"- Most interruptions occur during: {most_interrupted}")