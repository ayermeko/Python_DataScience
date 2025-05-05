import time
from datetime import datetime

epoch_time = time.time() #current time in seconds
print(f"Seconds since January 1, 1970: {epoch_time:,.4f} or {epoch_time:.2e}")
current_time = datetime.now().strftime("%b %d %Y")
print(current_time)
