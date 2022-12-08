# https://stackoverflow.com/questions/3489183/how-can-i-get-a-human-readable-timezone-name-in-python

import dateutil.tz as dtz
import pytz
import datetime as dt
import collections

result = collections.defaultdict(list)
for name in pytz.common_timezones:
    timezone = dtz.gettz(name)
    now = dt.datetime.now(timezone)
    offset = now.strftime('%z')
    abbrev = now.strftime('%Z')
    result[offset].append(name)
    result[abbrev].append(name)

for k, v in result.items():
    print(k, v)
