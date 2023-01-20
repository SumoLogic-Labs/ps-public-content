# Fortinet VPN Queries

Those queries require the Fortinet FER to be applied.
Replace `*fortinet*` by correct source category in your environment.

## Fortinet: VPN Failed Authentication Report
```
_sourceCategory=*fortinet* type="event" subtype="vpn" action="ssl-login-fail" user=*
| toUpperCase(user) as user
| formatDate(_messageTime, "yyyy-MM-dd HH:mm", "America/Denver") as timestamp
| lookup country_code, region, city from geo://location on ip=remip
| format("%s - %s (%s, %s, %s)", timestamp, remip, city, region, country_code) as connection_details
| count as connections, values(connection_details) as connection_details by user
| order by user asc
```

## Fortinet: VPN Successful Authentication Report
```
_sourceCategory=*fortinet* type="event" subtype="vpn" action="tunnel-up" user=*
| toUpperCase(user) as user
| formatDate(_messageTime, "yyyy-MM-dd HH:mm", "America/Denver") as timestamp
| lookup country_code, region, city from geo://location on ip=remip
| format("%s - %s (%s, %s, %s)", timestamp, remip, city, region, country_code) as connection_details
| count as connections, values(connection_details) as connection_details by user
| order by user asc
```

## Fortinet: VPN Successful Authentication Report - per User and State (detailed)
```
_sourceCategory=*fortinet* type="event" subtype="vpn" action="tunnel-up" user=*

| geoip remip
| if(IsPublicIp(remip), state, "** Internal IP **") as state

| count as number_of_connections,
  last(_messageTime) as first_connection,
  first(_messageTime) as last_connection, 
  values(remip) as ip_addresses,
  values(country_name) as countries,
  values(state) as states,
  values(city) as cities
  by user

| formatDate(last_connection, "yyyy-MM-dd HH:mm:ss") as last_connection
| formatDate(first_connection, "yyyy-MM-dd HH:mm:ss") as first_connection

| replace(ip_addresses, "\n", ",") as ip_addresses
| replace(countries, "\n", ",") as countries
| replace(states, "\n", ",") as states
| replace(cities, "\n", ",") as cities

| order by user asc
```

## Fortinet: VPN Successful Authentication Report - per User and State (summary)
```
_sourceCategory=*fortinet* type="event" subtype="vpn" action="tunnel-up" user=*
| geoip remip
| if(IsPublicIp(remip), state, "** Internal IP **") as state
| values(state) as states by user
| replace(states, "\n", ",") as states
| order by user asc
```
