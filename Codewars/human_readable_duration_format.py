def format_duration(seconds):
    if seconds == 0:
        return now
    else:
        sec = seconds % 60
        min = seconds % 3600
        hou = seconds % 86400
        day = seconds % 2592000
        mon = seconds % 31104000
        yea = seconds / 31104000
