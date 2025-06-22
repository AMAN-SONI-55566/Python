# example we have 5000 sec 

def convert_seconds(seconds):
    # 1 hour = 3600 seconds
    # We use // instead / for division :- beacause it performs integer division (floor division), 
    # rounding down to the nearest whole number.
    hours = seconds // 3600 
    
    # Remaining seconds after extracting hours
    remaining = seconds % 3600
    
    # 1 minute = 60 seconds
    minutes = remaining // 60
    
    # Remaining seconds after extracting minutes
    remaining_seconds = remaining % 60
    
    return hours, minutes, remaining_seconds

# Example use
hours, minutes, seconds = convert_seconds(5000)
print(f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)")
