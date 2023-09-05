# Field Extraction Rule:

```
| parse regex "^(?<timestamp>\d+\/\d+\/\d+\s\d+\:\d+\:\d+\s\S+\s)(?<remaining_message>.*)$" nodrop
| where !isEmpty(timestamp)

| parse regex field=remaining_message "\s*(?<thread_id>\S+)(?<remaining_message>.*)$" nodrop
| parse regex field=remaining_message "\s*(?<event_type>\S+)(?<remaining_message>.*)$" nodrop
| parse regex field=remaining_message "\s*(?<packet_identifier>\S+)(?<remaining_message>.*)$" nodrop
| parse regex field=remaining_message "\s*(?<protocol>\S+)(?<remaining_message>.*)$" nodrop
| parse regex field=remaining_message "\s*(?<direction>\S+)(?<remaining_message>.*)$" nodrop
| parse regex field=remaining_message "\s*(?<remote_ip>\S+)(?<remaining_message>.*)$" nodrop
| parse regex field=remaining_message "\s*(?<transaction_id>\S+)(?<remaining_message>.*)$" nodrop
| parse regex field=remaining_message "\s*(?<opcode>\S+)(?<remaining_message>.*)$" nodrop
| parse regex field=remaining_message "\s*\[(?<flags>[^\]]+)\](?<remaining_message>.*)$" nodrop
| parse regex field=remaining_message "\s*(?<record_type>[^\(]+)(?<remaining_message>.*)$" nodrop
| parse regex field=remaining_message "\s*(?<request>.*)$" nodrop

| parse regex field=flags "^(?<flag_code>[^\s]+)(?<remaining_flags>.*)$" nodrop
| parse regex field=remaining_flags "(?<flag_type>[^\s]*)\s*(?<flag_message>[^\s]*)$" nodrop
| parse regex field=flag_type "^\s+(?<flag_type>.*)" nodrop
| parse regex field=flag_type "(?<flag_type>.*)\s+$" nodrop

| parse regex field=record_type "(?<record_type>[^\s]+)" nodrop

| parse regex "\s+\(\d+\)(?<request>[^\s]*)\(0\)$" nodrop
| parse regex "\s+\(\d+\)(?<request>[^\s]*)\(0\)\n" nodrop
| replace(request, /\(\d+\)/, ".") as domain
| parse regex field=domain "(?<top_domain>[^\.]+\.[^\.]+)$" nodrop

| "UNKNOWN" as record_type_description
| if(record_type="A", "Host record", record_type_description) as record_type_description
| if(record_type="AAAA", "Host record (IPv6)", record_type_description) as record_type_description
| if(record_type="NS", "Name server record", record_type_description) as record_type_description
| if(record_type="CNAME", "Alias record", record_type_description) as record_type_description
| if(record_type="PTR", "Reverse-lookup record", record_type_description) as record_type_description
| if(record_type="MX", "Mail exchange record", record_type_description) as record_type_description
| if(record_type="SRV", "Service record", record_type_description) as record_type_description
| if(record_type="IXFR", "Incremental zone transfer record", record_type_description) as record_type_description
| if(record_type="AXFR", "Standard zone transfer record", record_type_description) as record_type_description
| if(record_type="All", "All records Domain", record_type_description) as record_type_description

| "Query" as opcode_description
| if(opcode="R", "Response", opcode_description) as opcode_description
| if(opcode="Q", "Standard Query", opcode_description) as opcode_description
| if(opcode="N", "Notify", opcode_description) as opcode_description
| if(opcode="U", "Update", opcode_description) as opcode_description
| if(opcode="?", "Unknown", opcode_description) as opcode_description

| "-" as flag_type_description
| if(flag_type contains "A", concat(flag_type_description, "\n- Authoritative Answer"), flag_type_description) as flag_type_description
| if(flag_type contains "T", concat(flag_type_description, "\n- Truncated Response"), flag_type_description) as flag_type_description
| if(flag_type contains "D", concat(flag_type_description, "\n- Recursion Desire"), flag_type_description) as flag_type_description
| if(flag_type contains "R", concat(flag_type_description, "\n- Recursion Available"), flag_type_description) as flag_type_description
| replace(flag_type_description, /^\-\n/, "") as flag_type_description

| fields thread_id, event_type, packet_identifier, protocol, direction, remote_ip, transaction_id, opcode, opcode_description, flag_code, flag_type, flag_type_description, flag_message, record_type, record_type_description, domain, top_domain
```
