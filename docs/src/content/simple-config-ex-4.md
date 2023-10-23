### Use a location and unit id (get unit controls)

Continuing to use the the fifth monitoring plan form the monitoring plan configuration response above, our location id is 11 and unit id is 5 (named unitId under the location object). For this example we'll use the location and unit id.

Below is a javascript example script collecting data from the unit controls endpoint from the [Monitoring Plan API](https://www.epa.gov/power-sector/cam-api-portal#/swagger/beta-monitor-plan-mgmt).

```
const simpleLocId = '11'
const simpleUnitId = '5'
```

```
const response = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/locations/'+simpleLocId+'/units/'+simpleUnitId+'/unit-controls',
{
    headers: {
        "x-api-key": "YOUR_API_KEY_HERE"
    },
    "method": "GET",
    });
const data = await response.json();
```