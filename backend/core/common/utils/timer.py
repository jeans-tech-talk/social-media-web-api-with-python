from datetime import datetime, timedelta
from typing import Optional

from django.utils import timezone


class Timer:
    def __init__(self, created_at: datetime) -> None:
        self.created_at = created_at

    def calculate_time_different(self) -> Optional[str]:
        time_different = timezone.now() - self.created_at

        return (
                self.get_years_weeks_days(time_different=time_different)
                or self.get_hours_minutes_seconds(time_different=time_different)
        )

    @staticmethod
    def get_years_weeks_days(time_different: timedelta) -> Optional[str]:
        time_units = [('y', 365), ('w', 7), ('d', 1)]

        for unit, divisor in time_units:
            unit_count = time_different.days // divisor
            if unit_count > 0:
                return f'{unit_count}{unit}'

        return None

    @staticmethod
    def get_hours_minutes_seconds(time_different: timedelta) -> Optional[str]:
        time_units = [('h', 3600), ('m', 60), ('s', 1)]

        for unit, divisor in time_units:
            unit_count = int(time_different.total_seconds() // divisor)
            if unit_count > 0:
                return f'{unit_count}{unit}'

        return None
