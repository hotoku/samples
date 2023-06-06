import pdb
from datetime import datetime, timezone, timedelta
import dateutil.tz as dtz


def print_date(msg, d):
    print(msg, ":", str(d), f"tz={d.tzinfo}")


d1 = datetime.now()
d2 = datetime.utcnow()

print_date("d1", d1)
print_date("d2", d2)

d3 = datetime.now(tz=timezone(timedelta(hours=9)))

print_date("d3", d3)

d4 = datetime.now(dtz.gettz("Asia/Tokyo"))

print_date("d4", d4)

# d1 : 2022-12-08 16:56:39.969149 tz=None
# d2 : 2022-12-08 07:56:39.969151 tz=None
# d3 : 2022-12-08 16:56:39.969163+09:00 tz=UTC+09:00
# d4 : 2022-12-08 16:56:39.969271+09:00 tz=tzfile('/usr/share/zoneinfo/Asia/Tokyo')
