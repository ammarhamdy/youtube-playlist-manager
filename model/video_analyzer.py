

class VideoAnalyser:
    def __init__(self):
        self.count = 0
        self.total_views = 0
        self.total_likes = 0
        self.total_comment = 0
        self.total_hours = 0
        self.total_minutes = 0
        self.total_seconds = 0

    def calculate_total(self, info: tuple):
        #('L9lcWd6WJ0o', 'title', '2021-10-21 10:09:41', '65674', 542, '0', '0:8:2')
        # id, title, date, views, likes, comments, duration
        self.count += 1
        self.total_views += int(info[3])
        self.total_likes += int(info[4])
        self.total_comment += int(info[5])
        self.calculate_duration(info[6])

    def calculate_duration(self, duration: str):
        """ calculate total videos duration """
        hours, minutes, seconds = duration.split(":")
        self.total_hours += int(hours)
        self.total_minutes += int(minutes)
        self.total_seconds += int(seconds)

    def get_total_duration(self):
        extra_minutes, total_seconds = divmod(self.total_seconds, 60)
        extra_hours, total_minutes = divmod(self.total_minutes + extra_minutes, 60)
        return f"{self.total_hours + extra_hours}:{total_minutes}:{total_seconds}"
