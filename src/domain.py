import datetime
import json

class Recipe:
    '''The basic recipe class'''
    pass

class Timeslot:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @property
    def _json(self):
        return dict(
            __class__ = self.__class__.__name__,
            __kw__ = dict( start = self.start, end = self.end ),
            __args__ = []
        )

class Meal:
    def __init__(self, name, timeslot):
        self.name = name
        self.timeslot = timeslot

    @property
    def _json(self):
        return dict(
            __class__ = self.__class__.__name__,
            __kw__ = dict( name = self.name, timeslot = self.timeslot ),
            __args__ = []
        )

class Activity:
    def __init__(self, name, busy_timeslot, activity_timeslot):
        if not isinstance(busy_timeslot, Timeslot):
            busy_timeslot = activity_timeslot
        self.name = name
        self.busy_timeslot = busy_timeslot
        self.activity_timeslot = activity_timeslot

    @property
    def _json(self):
        return dict(
            __class__ = self.__class__.__name__,
            __kw__ = dict( name = self.name, busy_timeslot = self.busy_timeslot, activity_timeslot = self.activity_timeslot ),
            __args__ = []
        )

class Schedule:
    def __init__(self, days = 7, activities = None, meals = None):
        self.days = days
        if activities == None:
            self.activities = []
        else:
            self.activities = activities
        if meals == None:
            self.meals = []
        else:
            self.meals = meals

    def addMeal(self, meal):
        self.meals.append(meal)

    def addActivity(self, activity):
        self.activities.append(activity)

    @property
    def _json(self):
        return dict(
            __class__ = self.__class__.__name__,
            __kw__ = dict( days = self.days, activities = self.activities, meals = self.meals ),
            __args__ = []
        )

def json_encode( obj ):
    if isinstance( obj, datetime.time ):
        return dict(
            __class__ = "datetime.time",
            __args__ = [],
            __kw__  = dict( hour = obj.hour, minute = obj.minute, second = obj.second, microsecond = obj.microsecond )
        )
    else:
        try:
            result = obj._json
        except AttributeError:
            result = json.JSONEncoder.default(obj)
        return result

def json_decode( some_dict ):
    if set( some_dict.keys() ) == set( [ "__class__", "__args__", "__kw__" ] ):
        class_ = eval( some_dict['__class__'] )
        return class_( *some_dict['__args__'], **some_dict['__kw__'] )
    else:
        return some_dict

def main():
    pass

if __name__ == "__main__":
    main()
