from datetime import datetime, timezone, timedelta


def print_date(msg, d):
    print(msg, ":", str(d), f"tz={d.tzinfo}")


d1 = datetime.now()
d2 = datetime.utcnow()

print_date("d1", d1)
print_date("d2", d2)

d3 = datetime.now(tz=timezone(timedelta(hours=9)))

print_date("d3", d3)

# d1 : 2022-12-08 16:08:40.538784 tz=None
# d2 : 2022-12-08 07:08:40.538787 tz=None
# d3 : 2022-12-08 16:08:40.538885+09:00 tz=UTC+09:00
