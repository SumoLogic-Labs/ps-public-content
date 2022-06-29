# Palo Alto 10.x - `TRAFFIC` Field Extraction Rule

Reference:
- https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/traffic-log-fields

## Scope
```
_sourceCategory=network/paloalto ",TRAFFIC,"
```

## FER
```
| csv _raw extract f1, receive_time, serial_number, type, subtype, f2, generated_time, source_address, destination_address, nat_source_ip, nat_destination_ip, rule_name, source_user, destination_user, application, virtual_system, source_zone, destination_zone, inbound_interface, outbound_interface, log_action, f3, session_id, repeat_count, source_port, destination_port, nat_source_port, nat_destination_port, flags, protocol, action, bytes, bytes_sent, bytes_received, packets, start_time, elapsed_time, category, f4, sequence_number, action_flags, source_country, destination_country, f5, packets_sent, packets_received, session_end_reason, device_group_hierarchy_level_1, device_group_hierarchy_level_2, device_group_hierarchy_level_3, device_group_hierarchy_level_4, virtual_system_name, device_name, action_source, source_vm_uuid, destination_vm_uuid, tunnel_id_imsi, monitor_tag_imei, parent_session_id, parent_start_time, tunnel_type, sctp_association_id, sctp_chunks, sctp_chunks_sent, sctp_chunks_received, rule_uuid, http_2_connection, app_flap_count, policy_id, link_switches, sd_wan_cluster, sd_wan_device_type, sd_wan_cluster_type, sd_wan_site, dynamic_user_group_name, xff_address, source_device_category, source_device_profile, source_device_model, source_device_vendor, source_device_os_family, source_device_os_version, source_hostname, source_mac_address, destination_device_category, destination_device_profile, destination_device_model, destination_device_vendor, destination_device_os_family, destination_device_os_version, destination_hostname, destination_mac_address, container_id, pod_namespace, pod_name, source_external_dynamic_list, destination_external_dynamic_list, host_id, user_device_serial_number, source_dynamic_address_group, destination_dynamic_address_group, session_owner, high_resolution_timestamp, a_slice_service_type, a_slice_differentiator, application_subcategory, application_category, application_technology, application_risk, application_characteristic, application_container, tunneled_application, application_saas, application_sanctioned_state, offloaded

| where type="TRAFFIC"

| fields action, action_source, application, application_category, application_characteristic, application_container, application_risk, application_sanctioned_state, application_subcategory, application_technology, bytes, bytes_received, bytes_sent, category, destination_address, destination_country, destination_hostname, destination_port, destination_user, destination_zone, device_name, elapsed_time, inbound_interface, nat_destination_ip, nat_destination_port, nat_source_ip, nat_source_port, packets, packets_received, packets_sent, protocol, rule_name, rule_uuid, sequence_number, session_end_reason, session_id, source_address, source_country, source_hostname, source_mac_address, source_port, source_user, source_zone, subtype, tunneled_application, type, xff_address
```