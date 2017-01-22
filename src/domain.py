class Recipe:
    '''The basic recipe class'''
    pass

class Timeslot:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isInTimeslot(self, timeToCheck):
        if self.start < timeToCheck and self.end > timeToCheck:
            return True
        else:
            return False

class Meal:
    def __init__(self, name, timeslot):
        self.name = name
        self.timeslot = timeslot

class Activity:
    def __init__(self, name, busy_timeslot, activity_timeslot):
        if not isinstance(busy_timeslot, Timeslot):
            busy_timeslot = activity_timeslot
        self.name = name
        self.busy_timeslot = busy_timeslot
        self.activity_timeslot = activity_timeslot

def main():
    pass

if __name__ == "__main__":
    main()
