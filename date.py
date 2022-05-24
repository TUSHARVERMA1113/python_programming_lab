from datetime import datetime

today = datetime.now()
print("Current Date and Time = ", today)

# Formatting
dt = today.strftime("%B %d, %Y %H:%M:%S")
print("Current Date and Time = ", dt)
