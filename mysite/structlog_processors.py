from django.utils import timezone

class TimeWithTimezone:
    def __init__(self):
        self._tz = timezone.get_current_timezone()
        
    def __call__(self, logger, name, event_dict):
        now = timezone.now().astimezone(self._tz)
        event_dict["timestamp"] = now.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
        return event_dict