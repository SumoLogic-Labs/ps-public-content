# Purpose
`cse_travelling_users_sync.py` script can be used to maintain a list of travelling users in a match list (with auto-expiration), and synchronize entity tags adn entity criticality (add or remove).

# How-to
## Create a new CSE Match list:
- Name: `travelling_users`
- Description: `Users currently travelling. This match list is used to disable some rules (impossible travel, first seen country, etc.) via tuning rule "Travelling Users". When adding a new user, set the auto-expiration date.`
- TTL: none
- Target column: `Username`  

## Create a new CSE Tuning Rule:
- Name: `Travelling Users`
- Rules:
  - `THRESHOLD-S00097: Impossible Travel - Successful`
  - `THRESHOLD-S00098: Impossible Travel - Unsuccessful`
  - `FIRST-S00029: First Seen Successful Authentication From Unexpected Country`
- Type: `EXCLUDE`
- Expression: `array_contains(listMatches, 'travelling_users')`

## Create a new CSE Entity Criticality:
- Name: `Travelling Users`
- Expression: `severity + 2`

## Add travelling users into the "travelling_users" match list.
- Add an expiration date, so the user will be automatically removed from the list

## Update the script with:
- `CSE_TRAVELLING_USERS_MATCHLIST_ID`
- `CSE_TRAVELLING_USERS_TAG`
- `CSE_TRAVELLING_USERS_CRITICALITY`
- `SUMO_API_ACCESS_ID`
- `SUMO_API_ACCESS_KEY`

## Run
- Schedule the execution of that script at least once a day to synchornize (add/remove) the tag and criticality on entities.
