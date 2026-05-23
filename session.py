# Classes/Objects
class StudySession:
    def __init__(self, subject, duration, status, focus_rating):
        self.subject = subject
        self.duration = duration
        self.status = status
        self.focus_rating = focus_rating

    def to_dict(self):
        return {
            "subject": self.subject,
            "duration": self.duration,
            "status": self.status,
            "focus_rating": self.focus_rating
        }