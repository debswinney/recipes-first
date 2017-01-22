import datetime
import unittest.test
from domain import Timeslot, Meal, Activity

class something_to_test(unittest.TestCase):
    def setUp(self):
        mealtime = Timeslot( datetime.time( 9 ), datetime.time( 10 ) )
        self.breakfast = Meal( "Breakfast", mealtime )

        traveltime = Timeslot( datetime.time( 8, 30 ), datetime.time( 10, 30 ) )
        self.tennis = Activity( "Tennis", traveltime, mealtime )

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

    def test_is_in_timelot(self):
        before = datetime.time( 8, 59 )
        assert not self.tennis.activity_timeslot.isInTimeslot( before )
        assert self.tennis.busy_timeslot.isInTimeslot( before )