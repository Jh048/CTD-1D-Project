def time_string_to_seconds(time_str):
    """Convert HH:MM:SS formatted time string to seconds."""
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def secs_to_clock(sec):
    """Convert seconds into HH:MM:SS format."""
    mins, secs = divmod(sec, 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"

def sum_activity_times(archive_dict):
    """Sum total elapsed and paused times across all activities."""
    total_elapsed_time = 0
    total_paused_time = 0
    
    # Print activity-wise breakdown
    print("Activity-wise Breakdown:")
    for activity, times in archive_dict.items():
        elapsed_time = time_string_to_seconds(times['Total Elapsed Time'])
        paused_time = time_string_to_seconds(times['Total Paused Time'])
        
        # Display individual activity times
        print(f"\nActivity: {activity}")
        print(f"  Total Elapsed Time: {times['Total Elapsed Time']}")
        print(f"  Total Paused Time: {times['Total Paused Time']}")
        
        # Sum the times
        total_elapsed_time += elapsed_time
        total_paused_time += paused_time
    
    # Convert summed times back to HH:MM:SS format
    total_elapsed_time_str = secs_to_clock(total_elapsed_time)
    total_paused_time_str = secs_to_clock(total_paused_time)
    
    return {
        "Total Elapsed Time": total_elapsed_time_str,
        "Total Paused Time": total_paused_time_str
    }

# Example archive_dict
archive_dict = {
    'math': {'Total Elapsed Time': '00:00:10', 'Total Paused Time': '00:00:00'},
    'math_break': {'Total Elapsed Time': '00:00:06', 'Total Paused Time': '00:00:00'},
    'work': {'Total Elapsed Time': '00:00:03', 'Total Paused Time': '00:00:00'},
    'work_break': {'Total Elapsed Time': '00:00:05', 'Total Paused Time': '00:00:00'}
}

# Summing the times across activities
total_times = sum_activity_times(archive_dict)

# Displaying the total summed times
print("\nTotal Time Across All Activities:")
print(f"Total Elapsed Time: {total_times['Total Elapsed Time']}")
print(f"Total Paused Time: {total_times['Total Paused Time']}")