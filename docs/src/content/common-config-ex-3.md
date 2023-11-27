### Use a location id

In the monitoring plan configuration response above (first example), the "Id" under the location objects are the unique identifier (Id) of a monitoring location record. You will see this as parameters to use in other endpoints (named: locId). For example, lets take the same second monitoring plan and use the location id.

Below is a javascript example script collecting data from the location methods endpoint from the [Monitoring Plan API](https://www.epa.gov/power-sector/cam-api-portal#/swagger/beta-monitor-plan-mgmt).

**_NOTE:_**  There are multiple location Ids in this example.

```
const commonLocId6 = '6'; // location of the unit 1
const commonLocId7 = '7'; // location of the unit 2
const commonLocId5 = '5'; // location of the stack CS0AAN
```

```
var response = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/locations/'+commonLocId6+'/methods',
{
    headers: {
        "x-api-key": "YOUR_API_KEY_HERE"
    },
    "method": "GET",
    });
const unit1Data = await response.json();

var response = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/locations/'+commonLocId7+'/methods',
{
    headers: {
        "x-api-key": "YOUR_API_KEY_HERE"
    },
    "method": "GET",
    });
const unit2Data = await response.json();

var response = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/locations/'+commonLocId5+'/methods',
{
    headers: {
        "x-api-key": "YOUR_API_KEY_HERE"
    },
    "method": "GET",
    });
const stackCS0AANData = await response.json();
```