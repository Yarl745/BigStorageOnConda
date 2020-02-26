def make_readable(seconds):
    hours, minutes = 0, 0
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    return "{hours:02}:{minutes:02}:{seconds:02}".format(hours=hours, minutes=minutes, seconds=seconds)
print(make_readable(0))