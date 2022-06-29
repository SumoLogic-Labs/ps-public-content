# Palo Alto 10.x - `GLOBAL PROTECT` Field Extraction Rule

Reference:
- https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/globalprotect-log-fields

## Scope
```
_sourceCategory=network/paloalto ",GLOBALPROTECT,"
```

## FER
```
| csv _raw extract f1, receive_time, serial_number, type, subtype, f2, generated_time, virtual_system, event_id, stage, authentication_method, tunnel_type, source_user, source_region, machine_name, public_ip, public_ipv6, private_ip, private_ipv6, host_id, user_device_serial_number, client_version, client_os, client_os_version, repeat_count, reason, error, description, status, location, login_duration, connect_method, error_code, portal, sequence_number, action_flags, high_res_timestamp, selection_type, response_time, priority, attempted_gateways, gateway, device_group_hierarchy_level_1, device_group_hierarchy_level_2, device_group_hierarchy_level_3, device_group_hierarchy_level_4, virtual_system_name, device_name, virtual_system_id

| where type="GLOBALPROTECT"

| fields authentication_method, client_os, client_os_version, client_version, connect_method, description, device_name, event_id, host_id, machine_name, portal, private_ip, public_ip, public_ipv6, reason, sequence_number, source_region, source_user, stage, status, subtype, tunnel_type, type, user_device_serial_number
```