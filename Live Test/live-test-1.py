# Write a function to make an hour-to-minute converter.

def hour_to_minute(hour):
    minute = hour * 60
    return minute
# to check if the func is working or not
hour = 3
result = hour_to_minute(hour)
print(hour, "hour =", result, "mins")