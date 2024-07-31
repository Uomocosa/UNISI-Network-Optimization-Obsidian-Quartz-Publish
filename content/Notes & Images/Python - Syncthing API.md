
[GitHub - Original](https://github.com/blakev/python-syncthing)

```python
from syncthing import Syncthing

API_KEY = "..."

s = Syncthing(API_KEY)

# name spaced by API endpoints
s.system.connections()

# supports GET/POST semantics
sync_errors = s.system.errors()
s.system.clear()

if sync_errors:
    for e in sync_errors:
        print(e)

# supports event long-polling
event_stream = s.events(limit=10)
for event in event_stream:
    # do something with `event`
    if event_stream.count > 100:
        event_stream.stop()
```