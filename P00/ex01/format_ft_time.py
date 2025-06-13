import datetime
import time

epoch_time = time.time()
print(f"Seconds since January 1, 1970: {epoch_time:,.4f} or {epoch_time:,.3} in scientific notation")
formated_way = datetime.datetime.now().strftime("%b %d %Y")
print(formated_way)