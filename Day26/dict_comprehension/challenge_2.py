weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

def convert_to_farenheight(temp_c):
    return (temp_c *9/5) + 32

print({day:convert_to_farenheight(temp_c) for (day, temp_c) in weather_c.items()})