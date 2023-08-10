### Use a location id

In the monitoring plan configuration response above (first example), the "Id" under the location objects are the unique identifier (Id) of a monitoring location record. You will see this as parameters to use in other endpoints (named: locId). For example, lets take the same fifth monitoring plan and use the location id.

Below is a javascript example script collecting data from the location attributes endpoint from the [Monitoring Plan API](https://www.epa.gov/power-sector/cam-api-portal#/swagger/beta-monitor-plan-mgmt).

**_NOTE:_**  There is only one location Id in this example, but that may not always be the case.

```
const locId = 11
```

```
const response = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/locations/11/attributes',
{
    headers: {
        "x-api-key": "YOUR_API_KEY_HERE"
    },
    referrerPolicy: "no-referrer",
    "method": "GET",
    });
const data = await response.json();
```



