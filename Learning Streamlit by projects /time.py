# current date minus a year
from datetime import datetime
from dateutil.relativedelta import relativedelta

# minus number of year
currentTimeDate = datetime.now() - relativedelta(years=5)
#currentTime = currentTimeDate.strftime('%Y')
time = str(currentTimeDate)
print(time[:10].strip())