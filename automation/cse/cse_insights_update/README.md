# Purpose
`cse_insight_update.py` script can be used to list and update CSE Insights.

# Variables
```
optional arguments:
  -h, --help                show this help message and exit
  -test                     test mode (no change applied)
  -env ENV                  Sumo Logic Environment (default: "us2")
  -tag TAG                  new TAG to apply
  -comment COMMENT          new COMMENT to apply
  -status STATUS            new STATUS to apply
  -resolution RESOLUTION    new RESOLUTION to apply

required arguments:
  -accessid ACCESSID        Sumo Logic API Access ID
  -accesskey ACCESSKEY      Sumo Logic API Access KEY
  -filter FILTER            CSE Insight filter (ex: '-status="closed" -tag="custom"')
```

# Examples
## List (no action) non-closed insights with tag CUSTOM
```
python3 cse_insight_update.py -accessid XXXXX -accesskey XXXXX -filter '-status:"closed" -tag:"CUSTOM"' -test
```

## Add tag NEWTAG to non-closed insights with tag CUSTOM
```
python3 cse_insight_update.py -accessid XXXXX -accesskey XXXXX -filter '-status:"closed" -tag:"CUSTOM"' -tag 'NEWTAG'
```

## Close as "No Action" all non-closed insights with tag CUSTOM, Add tag NEWTAG, add comment, in us2 environment
```
python3 cse_insight_update.py -env=us2 -accessid XXXXX -accesskey XXXXX -filter '-status:"closed" -tag:"CUSTOM"' -tag 'NEWTAG' -comment 'NEWCOMMENT' -status 'closed' -resolution 'No Action'
```