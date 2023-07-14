Scope:
```
_sourceCategory=juniper/mist AND "\"topic\":\"audits\""

```

Expression:
```
| json "topic", "events[0]" as topic, event nodrop
| where topic="audits"

| json field=event "admin_name", "site_name", "message", "src_ip", "before", "after" as admin_name, site_name, message, src_ip, before, after nodrop
```
