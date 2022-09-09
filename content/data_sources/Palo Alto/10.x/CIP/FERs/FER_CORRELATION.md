# Palo Alto 10.x - `CORRELATION` Field Extraction Rule

Reference:
- https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/correlated-events-log-fields

## Scope
```
_sourceCategory=network/paloalto ",CORRELATION,"
```

## FER
```
| csv _raw extract f1, receive_time, serial_number, type, content_threat_type, f2, generated_time, source_address, source_user, virtual_system, category, severity, device_group_hierarchy_level_1, device_group_hierarchy_level_2, device_group_hierarchy_level_3, device_group_hierarchy_level_4, virtual_system_name, device_name, virtual_system_id, object_name, object_id, evidence

| where type="CORRELATION"

| fields category, content_threat_type, device_name, evidence, object_id, object_name, severity, source_address, source_user, type
```