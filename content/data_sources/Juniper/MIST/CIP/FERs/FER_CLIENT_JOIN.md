Scope:
```
_sourceCategory=juniper/mist AND "\"topic\":\"client-join\""
```

Expression:
```
| json "topic", "events[0]" as topic, event nodrop
| where topic="client-join"

| json field=event "ap_name", "site_name", "ssid", "mac" as ap_name, site_name, ssid, mac nodrop
```
