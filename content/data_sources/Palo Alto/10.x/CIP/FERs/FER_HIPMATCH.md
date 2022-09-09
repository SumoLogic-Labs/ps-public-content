# Palo Alto 10.x - `HIPMATCH` Field Extraction Rule

Reference:
- https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/hip-match-log-fields

## Scope
```
_sourceCategory=network/paloalto ",HIPMATCH,"
```

## FER
```
| csv _raw extract f1, receive_time, serial_number, type, subtype, f2, generated_time, source_user, virtual_system, machine_name, operating_system, source_address, hip, repeat_count, hip_type, f3, f4, sequence_number, action_flags, device_group_hierarchy_level_1, device_group_hierarchy_level_2, device_group_hierarchy_level_3, device_group_hierarchy_level_4, virtual_system_name, device_name, virtual_system_id, ipv6_source_address, host_id, user_device_serial_number, device_mac_address, high_resolution_timestamp

| where type="HIPMATCH"

| fields device_name, hip, hip_type, host_id, ipv6_source_address, machine_name, operating_system, source_address, source_user, type, user_device_serial_number
```
