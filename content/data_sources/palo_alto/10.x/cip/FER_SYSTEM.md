# Palo Alto 10.x - `SYSTEM` Field Extraction Rule

Reference:
- https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/system-log-fields

## Scope
```
_sourceCategory=network/paloalto ",SYSTEM,"
```

## FER
```
| csv _raw extract f1, receive_time, serial_number, type, content_threat_type, f2, generated_time, virtual_system, event_id, object, f3, f4, module, severity, description, sequence_number, action_flags, device_group_hierarchy_level_1, device_group_hierarchy_level_2, device_group_hierarchy_level_3, device_group_hierarchy_level_4, virtual_system_name, device_name, f5, f6, high_resolution_timestamp

| where type="SYSTEM"

| fields content_threat_type, description, device_name, event_id, module, object, sequence_number, severity, type
```
