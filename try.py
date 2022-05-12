import datetime


class TestTodayMonth:
    """Stores today's tests"""

    def test_today_day(self):
        assert datetime.datetime.now().day == 9
        print("Day was verified")

    def test_today_month(self):
        """Test today's date"""
        assert datetime.datetime.now().month == 5
        print("Month was verified")
