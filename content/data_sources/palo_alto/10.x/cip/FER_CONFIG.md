# Palo Alto 10.x - `CONFIG` Field Extraction Rule

Reference:
- https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/config-log-fields

## Scope
```
_sourceCategory=network/paloalto ",CONFIG,"
```

## FER
```
| csv _raw extract f1, receive_time, serial_number, type, subtype, f2, generated_time, host, virtual_system, command, admin, client, result, configuration_path, before_change_detail, after_change_detail, sequence_number, action_flags, device_group_hierarchy_level_1, device_group_hierarchy_level_2, device_group_hierarchy_level_3, device_group_hierarchy_level_4, virtual_system_name, device_name, device_group, audit_comment

| where type="CONFIG"

| fields admin, after_change_detail, before_change_detail, client, command, configuration_path, device_name, host, result, type
```