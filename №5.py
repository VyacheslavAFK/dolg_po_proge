def convert_to_12_hour_format(hours: int, minutes: int):
    if minutes == 0:
        minutes = "00"
    if hours > 24 or minutes > 60:
        return "Неорректный формат времени"
    if minutes == 60:
        minutes = "00"
        hours += 1
        if hours > 24:
            hours -= 12
    if hours > 12:
        hours -= 12
        return f"{hours}:{minutes} PM"
    else:
        return f"{hours}:{minutes} AM"


print(convert_to_12_hour_format(24, 60))
