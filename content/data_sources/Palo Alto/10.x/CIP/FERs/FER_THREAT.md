# Palo Alto 10.x - `THREAT` Field Extraction Rule

References (note: several fields names have been modified in the FER below to work with the following three formats):
- https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/threat-log-fields
- https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/url-filtering-log-fields
- https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/data-filtering-log-fields

## Scope
```
_sourceCategory=network/paloalto ",THREAT,"
```

## FER
```
| csv _raw extract f1, receive_time, serial_number, type, subtype, f2, generated_time, source_address, destination_address, nat_source_ip, nat_destination_ip, rule_name, source_user, destination_user, application, virtual_system, source_zone, destination_zone, inbound_interface, outbound_interface, log_action, f3, session_id, repeat_count, source_port, destination_port, nat_source_port, nat_destination_port, flags, ip_protocol, action, url_filename, threat_id, category, severity, direction, sequence_number, action_flags, source_country, destination_country, f4, content_type, pcap_id, file_digest, cloud, url_index, user_agent, file_type, x_forwarded_for, referer, sender, subject, recipient, report_id, device_group_hierarchy_level_1, device_group_hierarchy_level_2, device_group_hierarchy_level_3, device_group_hierarchy_level_4, virtual_system_name, device_name, f5, source_vm_uuid, destination_vm_uuid, http_method, tunnel_id_imsi, monitor_tag_imei, parent_session_id, parent_start_time, tunnel_type, threat_category, content_version, f6, sctp_association_id, payload_protocol_id, http_headers, url_category_list, rule_uuid, http_2_connection, dynamic_user_group_name, xff_address, source_device_category, source_device_profile, source_device_model, source_device_vendor, source_device_os_family, source_device_os_version, source_hostname, source_mac_address, destination_device_category, destination_device_profile, destination_device_model, destination_device_vendor, destination_device_os_family, destination_device_os_version, destination_hostname, destination_mac_address, container_id, pod_namespace, pod_name, source_external_dynamic_list, destination_external_dynamic_list, host_id, user_device_serial_number, domain_edl, source_dynamic_address_group, destination_dynamic_address_group, partial_hash, high_resolution_timestamp, reason, justification, a_slice_service_type, application_subcategory, application_category, application_technology, application_risk, application_characteristic, application_container, tunneled_application, application_saas, application_sanctioned_state, cloud_report_id

| where type="THREAT"

| fields action, application, application_category, application_characteristic, application_container, application_risk, application_sanctioned_state, application_subcategory, application_technology, category, content_version, destination_address, destination_country, destination_hostname, destination_mac_address, destination_port, destination_user, destination_zone, device_name, direction, file_digest, file_type, http_method, inbound_interface, ip_protocol, nat_destination_ip, nat_destination_port, nat_source_ip, nat_source_port, outbound_interface, reason, recipient, referer, repeat_count, rule_name, rule_uuid, sender, sequence_number, session_id, severity, source_address, source_country, source_hostname, source_mac_address, source_port, source_user, source_zone, subject, subtype, threat_category, type, threat_id
```
