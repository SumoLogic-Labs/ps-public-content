# Palo Alto 10.x - `USERID` Field Extraction Rule

Reference:
- https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/user-id-log-fields

## Scope
```
_sourceCategory=network/paloalto ",USERID,"
```

## FER
```
| csv _raw extract f1, receive_time, serial_number, type, subtype, f2, generated_time, virtual_system, source_ip, user, data_source_name, event_id, repeat_count, time_out_threshold, source_port, destination_port, data_source, data_source_type, sequence_number, action_flags, device_group_hierarchy_level_1, device_group_hierarchy_level_2, device_group_hierarchy_level_3, device_group_hierarchy_level_4, virtual_system_name, device_name, virtual_system_id, factor_type, factor_completion_time, factor_number, f3, f4, user_group_flags, user_by_source, high_resolution_timestamp

| where type="USERID"

| fields data_source, data_source_name, device_name, sequence_number, source_ip, subtype, type, user
```
