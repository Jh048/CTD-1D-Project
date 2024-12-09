def time_to_seconds(time_str):
    """Convert HH:MM:SS format to total seconds."""
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_time(total_seconds):
    """Convert total seconds to HH:MM:SS format."""
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def sum_timer_data(timer_data):
    """Sum elapsed and paused times from the timer data."""
    total_elapsed_seconds = 0
    total_paused_seconds = 0

    for entry in timer_data:
        elapsed_time = entry.get("elapsed_time", "00:00:00")
        paused_time = entry.get("paused_time", "00:00:00")

        total_elapsed_seconds += time_to_seconds(elapsed_time)
        total_paused_seconds += time_to_seconds(paused_time)

    total_elapsed = seconds_to_time(total_elapsed_seconds)
    total_paused = seconds_to_time(total_paused_seconds)

    return {"total_elapsed": total_elapsed, "total_paused": total_paused}

# Example usage
timer_data = [
    {'math_Elapsed_time': '00:00:03', 'math_paused_time': '00:00:00'},
    {'math_rest_Elapsed_time': '00:00:03', 'math_rest_paused_time': '00:00:00'}
]

result = sum_timer_data(timer_data)
print(result)  # Output: {'total_elapsed': '00:00:10', 'total_paused': '00:00:00'}
print(timer_data) 