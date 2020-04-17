class Time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def add_time(self, t1, t2):
        self.hours = t1.hours + t2.hours
        self.minutes = t1.minutes + t2.minutes
        while self.minutes >= 60:
            self.hours += 1
            self.minutes -= 60
        return self

    def display_time(self):
        print(f"Time is {self.hours} hours and {self.minutes} minutes.")

    def display_minute(self):
        minutes = self.hours * 60 + self.minutes
        print(f"total {minutes} minutes.")


a = Time(2, 59)
b = Time(1, 20)
c = Time().add_time(a, b)
c.display_time()
c.display_minute()
