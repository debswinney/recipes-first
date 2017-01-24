import datetime
import unittest.test
import json
from domain import Timeslot, Meal, Activity, Schedule, json_encode, json_decode

class _expectedResults():
    def __init__(self):
        self.timeslot_expected_results = """{
    "__class__": "Timeslot",
    "__kw__": {
        "start": {
            "__class__": "datetime.time",
            "__args__": [],
            "__kw__": {
                "hour": 9,
                "minute": 0,
                "second": 0,
                "microsecond": 0
            }
        },
        "end": {
            "__class__": "datetime.time",
            "__args__": [],
            "__kw__": {
                "hour": 10,
                "minute": 0,
                "second": 0,
                "microsecond": 0
            }
        }
    },
    "__args__": []
}"""
        self.breakfast_expected_results = """{
    "__class__": "Meal",
    "__kw__": {
        "name": "Breakfast",
        "timeslot": {
            "__class__": "Timeslot",
            "__kw__": {
                "start": {
                    "__class__": "datetime.time",
                    "__args__": [],
                    "__kw__": {
                        "hour": 9,
                        "minute": 0,
                        "second": 0,
                        "microsecond": 0
                    }
                },
                "end": {
                    "__class__": "datetime.time",
                    "__args__": [],
                    "__kw__": {
                        "hour": 10,
                        "minute": 0,
                        "second": 0,
                        "microsecond": 0
                    }
                }
            },
            "__args__": []
        }
    },
    "__args__": []
}"""
        self.tennis_expected_results = """{
    "__class__": "Activity",
    "__kw__": {
        "name": "Tennis",
        "busy_timeslot": {
            "__class__": "Timeslot",
            "__kw__": {
                "start": {
                    "__class__": "datetime.time",
                    "__args__": [],
                    "__kw__": {
                        "hour": 8,
                        "minute": 30,
                        "second": 0,
                        "microsecond": 0
                    }
                },
                "end": {
                    "__class__": "datetime.time",
                    "__args__": [],
                    "__kw__": {
                        "hour": 10,
                        "minute": 30,
                        "second": 0,
                        "microsecond": 0
                    }
                }
            },
            "__args__": []
        },
        "activity_timeslot": {
            "__class__": "Timeslot",
            "__kw__": {
                "start": {
                    "__class__": "datetime.time",
                    "__args__": [],
                    "__kw__": {
                        "hour": 9,
                        "minute": 0,
                        "second": 0,
                        "microsecond": 0
                    }
                },
                "end": {
                    "__class__": "datetime.time",
                    "__args__": [],
                    "__kw__": {
                        "hour": 10,
                        "minute": 0,
                        "second": 0,
                        "microsecond": 0
                    }
                }
            },
            "__args__": []
        }
    },
    "__args__": []
}"""
        self.schedule_expected_results = """{
    "__class__": "Schedule",
    "__kw__": {
        "days": 7,
        "activities": [
            {
                "__class__": "Activity",
                "__kw__": {
                    "name": "Tennis",
                    "busy_timeslot": {
                        "__class__": "Timeslot",
                        "__kw__": {
                            "start": {
                                "__class__": "datetime.time",
                                "__args__": [],
                                "__kw__": {
                                    "hour": 8,
                                    "minute": 30,
                                    "second": 0,
                                    "microsecond": 0
                                }
                            },
                            "end": {
                                "__class__": "datetime.time",
                                "__args__": [],
                                "__kw__": {
                                    "hour": 10,
                                    "minute": 30,
                                    "second": 0,
                                    "microsecond": 0
                                }
                            }
                        },
                        "__args__": []
                    },
                    "activity_timeslot": {
                        "__class__": "Timeslot",
                        "__kw__": {
                            "start": {
                                "__class__": "datetime.time",
                                "__args__": [],
                                "__kw__": {
                                    "hour": 9,
                                    "minute": 0,
                                    "second": 0,
                                    "microsecond": 0
                                }
                            },
                            "end": {
                                "__class__": "datetime.time",
                                "__args__": [],
                                "__kw__": {
                                    "hour": 10,
                                    "minute": 0,
                                    "second": 0,
                                    "microsecond": 0
                                }
                            }
                        },
                        "__args__": []
                    }
                },
                "__args__": []
            }
        ],
        "meals": [
            {
                "__class__": "Meal",
                "__kw__": {
                    "name": "Breakfast",
                    "timeslot": {
                        "__class__": "Timeslot",
                        "__kw__": {
                            "start": {
                                "__class__": "datetime.time",
                                "__args__": [],
                                "__kw__": {
                                    "hour": 9,
                                    "minute": 0,
                                    "second": 0,
                                    "microsecond": 0
                                }
                            },
                            "end": {
                                "__class__": "datetime.time",
                                "__args__": [],
                                "__kw__": {
                                    "hour": 10,
                                    "minute": 0,
                                    "second": 0,
                                    "microsecond": 0
                                }
                            }
                        },
                        "__args__": []
                    }
                },
                "__args__": []
            }
        ]
    },
    "__args__": []
}"""

class something_to_test(unittest.TestCase):
    def setUp(self):
        self.mealtime = Timeslot( datetime.time( 9 ), datetime.time( 10 ) )
        self.breakfast = Meal( "Breakfast", self.mealtime )

        traveltime = Timeslot( datetime.time( 8, 30 ), datetime.time( 10, 30 ) )
        self.tennis = Activity( "Tennis", traveltime, self.mealtime )

        self.schedule = Schedule()
        self.schedule.addActivity( self.tennis )
        self.schedule.addMeal( self.breakfast )

        self.expected_results = _expectedResults()

    def test_should_have_mealtime(self):
        assert self.breakfast.timeslot.start.hour == 9
        assert self.breakfast.timeslot.start.minute == 0
        assert self.breakfast.timeslot.end.hour == 10
        assert self.breakfast.timeslot.end.minute == 0

    def test_should_have_activity_times(self):
        assert self.tennis.busy_timeslot.start.hour == 8
        assert self.tennis.busy_timeslot.start.minute == 30
        assert self.tennis.activity_timeslot.start.hour == 9
        assert self.tennis.activity_timeslot.start.minute == 0
        assert self.tennis.activity_timeslot.end.hour == 10
        assert self.tennis.activity_timeslot.end.minute == 0
        assert self.tennis.busy_timeslot.end.hour == 10
        assert self.tennis.busy_timeslot.end.minute == 30

    def test_schedule_setup(self):
        assert self.schedule.days == 7
        assert len( self.schedule.meals ) == 1
        assert len( self.schedule.activities ) == 1

    def test_timeslot_to_json(self):
        str = json.dumps( self.mealtime, indent = 4, default=json_encode )
        assert self.expected_results.timeslot_expected_results == str

    def test_meal_to_json(self):
        str = json.dumps( self.breakfast, indent = 4, default=json_encode )
        assert self.expected_results.breakfast_expected_results == str

    def test_activity_to_json(self):
        str = json.dumps( self.tennis, indent = 4, default=json_encode )
        assert self.expected_results.tennis_expected_results == str

    def test_schedule_to_json(self):
        str = json.dumps( self.schedule, indent = 4, default=json_encode )
        assert self.expected_results.schedule_expected_results == str

    def test_timeslot_from_json(self):
        timeslot = json.loads( self.expected_results.timeslot_expected_results, object_hook=json_decode )
        assert isinstance( timeslot, Timeslot )
        assert timeslot.start.hour == 9
        assert timeslot.start.minute == 0
        assert timeslot.start.second == 0
        assert timeslot.start.microsecond == 0
        assert timeslot.end.hour == 10
        assert timeslot.end.minute == 0
        assert timeslot.end.second == 0
        assert timeslot.end.microsecond == 0

    def test_meal_from_json(self):
        meal = json.loads( self.expected_results.breakfast_expected_results, object_hook=json_decode )
        assert isinstance( meal, Meal )
        assert meal.name == "Breakfast"
        assert meal.timeslot.start.hour == 9
        assert meal.timeslot.end.hour == 10

    def test_activity_from_json(self):
        tennis = json.loads( self.expected_results.tennis_expected_results, object_hook=json_decode )
        assert isinstance( tennis, Activity )
        assert tennis.name == "Tennis"
        assert isinstance( tennis.busy_timeslot, Timeslot )
        assert tennis.busy_timeslot.start.hour == 8
        assert tennis.busy_timeslot.start.minute == 30
        assert tennis.busy_timeslot.end.hour == 10
        assert tennis.busy_timeslot.end.minute == 30
        assert isinstance( tennis.activity_timeslot, Timeslot )
        assert tennis.activity_timeslot.start.hour == 9
        assert tennis.activity_timeslot.end.hour == 10

    def test_schedule_from_json(self):
        schedule = json.loads( self.expected_results.schedule_expected_results, object_hook=json_decode )
        assert isinstance( schedule, Schedule )
        assert schedule.days == 7
        assert len( schedule.activities ) == 1
        assert len( schedule.meals ) == 1
