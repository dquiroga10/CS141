fiveKtime = float(input("Enter 5k finishing time (in minutes):"))
orig_pace = fiveKtime / 3.1
marathon_time = orig_pace * 1.3 * 26.2
hours  = round(marathon_time / 60)
minutes = round(marathon_time // 60)
print("Predicted marathon finish time is" , hours , "hours and" , minutes , "minutes.")
