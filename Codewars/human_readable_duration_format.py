def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:

        duration: dict = {'seconds': seconds % 60, 'minutes': seconds % 3600, 'hours': seconds % 86400,
                          'days': seconds % 2592000, 'months': seconds % 31104000, 'years': 0}
        if seconds / 31104000 > 1:
            duration['years'] = int(seconds / 31104000)
        return duration


print(format_duration(140063843))
