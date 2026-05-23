# Functions, Containers, Data Visualization, Advanced Concepts
import matplotlib.pyplot as plt
from collections import defaultdict


def plot_study_time(data):
    if not data:
        print("\nNo data available for plotting.\n")
        return

    subject_time = defaultdict(int)

    for session in data:
        subject_time[session["subject"]] += session["duration"]

    subjects = list(subject_time.keys())
    durations = list(subject_time.values())

    plt.figure(figsize=(8, 5))

    plt.bar(subjects, durations)

    plt.title("Study Time Per Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Minutes Studied")

    plt.tight_layout()

    plt.show()


def plot_focus_ratings(data):
    if not data:
        print("\nNo data available for plotting.\n")
        return

    ratings = []

    for session in data:
        ratings.append(session["focus_rating"])

    session_numbers = list(range(1, len(ratings) + 1))

    plt.figure(figsize=(8, 5))

    plt.plot(session_numbers, ratings, marker='o')

    plt.title("Focus Rating Trend")
    plt.xlabel("Session Number")
    plt.ylabel("Focus Rating")

    plt.ylim(1, 5)

    plt.tight_layout()

    plt.show()