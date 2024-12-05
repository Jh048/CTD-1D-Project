# time_calculator.py

from datetime import timedelta

def calculate_total_times(archive_dict):
    def time_string_to_seconds(time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        return timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()

    def seconds_to_time_string(seconds):
        return str(timedelta(seconds=seconds))

    total_times = {}

    for key_name, activities in archive_dict.items():
        total_elapsed = 0
        total_paused = 0
        
        for activity in activities:
            total_elapsed += time_string_to_seconds(activity['Elapsed_time'])
            total_paused += time_string_to_seconds(activity['Total_paused_time'])
        
        total_elapsed_time_str = seconds_to_time_string(total_elapsed)
        total_paused_time_str = seconds_to_time_string(total_paused)
        
        total_times[key_name] = {
            'Total Elapsed Time': total_elapsed_time_str,
            'Total Paused Time': total_paused_time_str
        }

    return total_times