Scope:
```
_sourceCategory=juniper/mist AND "\"topic\":\"device-events\""

```

Expression:
```
| json "topic", "events[0]" as topic, event nodrop
| where topic="device-events"

| json field=event "device_name", "device_type", "site_name", "text", "type" as device_name, device_type, site_name, text, type nodrop
```
