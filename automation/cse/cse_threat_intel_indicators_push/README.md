# Purpose
`cse_threat_intel_indicators_push.py` script can be used to push IOCs from a CSV file to a CSE Threat Intel Source.

# Variables
```
optional arguments:
  -h, --help            show this help message and exit
  -env ENV              Sumo Logic Environment (default: "us2")

required arguments:
  -accessid ACCESSID                          Sumo Logic API Access ID
  -accesskey ACCESSKEY                        Sumo Logic API Access KEY
  -threatIntelSourceId  THREATINTELSOURCEID   CSE Threat Intel Source ID
  -input INPUT          Input CSV file
```

# Input CSV file
Input CSV file must be in the folllowing format (with headers):
```
value,description,expiration
www.google.xxx,bad domain,
10.10.10.10,bad IP,2023-07-05T17:04:50Z
user@domain.com,bad user,
```

# Example
## Push IOCs to source ID 1
```
/usr/local/bin/python3 ./cse_threat_intel_indicators_push.py -accessid XXXXX -accesskey XXXXX -threatIntelSourceId 1 -input example_indicators.csv
```

## Output:
```
Adding IOC: www.google.xxx                 | bad domain                               | 
        - OK
Adding IOC: 10.10.10.10                    | bad IP                                   | 2023-07-05T17:04:50Z
        - OK
Adding IOC: user@domain.com                | bad user                                 | 
        - OK
```

## Results:
<img width="1240" alt="image" src="https://user-images.githubusercontent.com/1272790/177391884-6852ec9d-fafa-4957-ad06-e3906a3a87d3.png">
