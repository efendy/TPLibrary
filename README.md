#How to use

Authentication
```
from tp.auth import Authentication

auth = Authentication(environment[ENV]["user"], environment[ENV]["pass"])
MPX_TOKEN = auth.get_token()
```

Data Service Client
```
from tp.client import DataServiceClient

ds = DataServiceClient({DSObjectClass}, MPX_TOKEN, ACCOUNT_URI)
```

Data Service Client for Retrieve Media
```
from tp.client import DataServiceClient
from tp.objects import Media

ds = DataServiceClient(Media, MPX_TOKEN, ACCOUNT_URI)
ds.queries({ "fields": "id,title,guid" })

if (ds.request_get()):
   for entry in ds.get_entries():
      pass
   entries_size = ds.get_size()
```
