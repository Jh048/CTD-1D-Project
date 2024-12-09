# CTD-1D-Project

Timer Program

Overview

This program allows users to manage their tasks with a timer, offering features such as work/rest sessions, pausing, and history tracking. It supports custom work and rest times, along with pre-defined study and work modes.

Setup and Running the Program

Requirements
	1.	Python 3.8 or higher.
	2.	Required modules:
        •	time
        •	threading
        •	sys
        •	datetime
        •	copy

Ensure you have Python installed on your system. To check, run:

python --version

Steps to Run the Program
	1.	Download or Clone the Repository:
Save the program files (function.py and menu.py) in the same directory.
	2.	Run the Program:
Open a terminal or command prompt, navigate to the folder containing function.py, and run:

python function.py

    3.	Interactive Menu:
Follow the on-screen menu prompts to select your activity, set timers, view history, or exit the program.

Program Features

1. Modes:
   •	Study: Focused study sessions with 25-minute work blocks and 5-minute breaks.
   •	Work: Work sessions with 45-minute blocks and 15-minute breaks.
   •	Custom: Set your own durations for work and rest activities like meditation, cooking, etc.
2. Controls During Timer:
   •	Press p to pause.
   •	Press r to resume.
   •	Press q to quit the current timer.
3. History Tracking:
   •	Tracks elapsed and paused time for each activity.
   •	Provides a summary of all activities upon request.
4. Reset Options:
   •	Clear history or start fresh.
5. Exit Options:
   •	Continue, view history, or exit the program.

Common Issues
	1.	Input Format Error:
        •	Ensure time inputs are in the format HH,MM,SS.
        •	Example: 0,25,0 for 25 minutes.
	2.	Program Stops Unexpectedly:
        •	Verify you have all dependencies installed.
        •	Restart the program if needed.
	3.	History Reset Warning:
        •	Resetting history will delete all previous activity data.
