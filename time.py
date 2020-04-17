class Time():
    def __init__(self, hours=0, mins=0):
        self.hours = hours
        self.mins = mins

    def addTime(self, t1, t2):
        self.hours = t1.hours + t2.hours
        self.mins = t1.mins + t2.mins
        while self.mins >= 60:
            self.hours += 1
            self.mins -= 60
        return self

    def display_time(self):
        print(f"Time is {self.hours} hours and {self.mins} minutes.")

    def display_minute(self):
        minutes = self.hours * 60 + self.mins
        print(f"total {minutes} minutes.")


a = Time(2, 59)
b = Time(1, 20)
c = Time().addTime(a, b)
c.display_time()
c.display_minute()
