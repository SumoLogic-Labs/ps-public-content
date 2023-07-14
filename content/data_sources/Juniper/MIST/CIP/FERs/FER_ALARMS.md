Scope: 
```
_sourceCategory=juniper/mist AND "\"topic\":\"alarms\""
```

Expression: 
```
|json "topic", "events[0]" as topic, event nodrop
| where topic="alarms"

| json field=event "group", "type", "hostnames[0]", "severity", "site_name", "reasons[0]"  as group, type, hostname, severity, site_name, reason nodrop
```
