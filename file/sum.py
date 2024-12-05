from timerA import *
def display_time_summary(archive_dict):
    """
    Displays the activity-wise breakdown and total elapsed and paused times across all activities.

    Args:
        archive_dict (dict): A dictionary containing activity data with elapsed and paused times.

    Returns:
        dict: Total elapsed and paused times across all activities in HH:MM:SS format.
    """
    def time_string_to_seconds(time_str):
        """Convert HH:MM:SS formatted time string to seconds."""
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds

    def secs_to_clock(sec):
        """Convert seconds into HH:MM:SS format."""
        mins, secs = divmod(sec, 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

    total_elapsed_time = 0
    total_paused_time = 0

    # Activity-wise breakdown
    print("Activity-wise Breakdown:")
    for activity, times in archive_dict.items():
        elapsed_time = time_string_to_seconds(times['Elapsed_time'])
        paused_time = time_string_to_seconds(times['Total_paused_time'])
        
        total_elapsed_time += elapsed_time
        total_paused_time += paused_time
        
        elapsed_time_str = secs_to_clock(elapsed_time)
        paused_time_str = secs_to_clock(paused_time)

        print(f"\nActivity: {activity}")
        print(f"  Total Elapsed Time: {elapsed_time_str}")
        print(f"  Total Paused Time: {paused_time_str}")
    
    # Total time across all activities
    total_elapsed_time_str = secs_to_clock(total_elapsed_time)
    total_paused_time_str = secs_to_clock(total_paused_time)

    print("\nTotal Time Across All Activities:")
    print(f"Total Elapsed Time: {total_elapsed_time_str}")
    print(f"Total Paused Time: {total_paused_time_str}")

    # Return total times as a dictionary
    return {
        "Total Elapsed Time": total_elapsed_time_str,
        "Total Paused Time": total_paused_time_str
    }

# # Example archive_dict
# archive_dict = {
#     'math': {'Total Elapsed Time': '00:00:10', 'Total Paused Time': '00:00:00'},
#     'math_break': {'Total Elapsed Time': '00:00:06', 'Total Paused Time': '00:00:00'},
#     'work': {'Total Elapsed Time': '00:00:03', 'Total Paused Time': '00:00:00'},
#     'work_break': {'Total Elapsed Time': '00:00:05', 'Total Paused Time': '00:00:00'}
# }

# Call the function
if __name__ == "__main__":
    display_time_summary(archive_dict)
