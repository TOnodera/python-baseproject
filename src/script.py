import memcache
import time

db = memcache.Client(["memcached:11211"])

db.set("web_page", "value1", time=1)
time.sleep(2)
print(db.get("web_page"))
