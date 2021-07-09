from datetime import datetime
import pytz
niu = datetime.now()#naive
niu = datetime.now(tz=pytz.UTC)#aware
nu = datetime.utcnow().replace(tzinfo=pytz.UTC)
# astimezone to convert to switch between diff timezones can be done only on aware datetimes
dt_mum = niu.astimezone(pytz.timezone('Asia/Calcutta'))
print(niu)
print(nu)
print(str(dt_mum))


#localize for naive datetime  to make them aware
dt_mum = datetime.now()
print(dt_mum)
mum_tz = pytz.timezone('Asia/Calcutta')
dt_mum = mum_tz.localize(dt_mum)#made it aware using localize
print(dt_mum)

# aware to naive 4 ways
# localise 
# datetime.now(tz=pytz.UTC)
# astimezone(pytz.timezone('Asia/Calcutta'))
# datetime.utcnow().replace(tzinfo=pytz.UTC)(specific to utc now since we cant pass tz as a paramter to the constructor )

# string formats 
# dt_mum = datetime.now(tz = pytz.timezone('Asia/Calcutta'))
# print(dt_mum.strftime('%A -> %B %d,%Y '))
# s = 'September 09,2020'
# dt = datetime.strptime(s,'%B %d,%Y')
# print(type(dt))

# strftime ->converts datetime to a string 
# strptimee ->converts string to datetime