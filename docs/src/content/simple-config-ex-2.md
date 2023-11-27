### Use a monitoring plan id

The first "Id" of each object in the response above is the unique identifier (Id) of a monitoring configuration record. You will see this as parameters to use in other endpoints (named: monitorPlanId, monPlanIds or planIds). For example, lets take the fifth monitoring plan id in the response above and use it.

Below is a javascript example script collecting data from the emissions export endpoint from the [Emissions API](https://www.epa.gov/power-sector/cam-api-portal#/swagger/beta-emissions-mgmt).

**_NOTE:_**  We use the fifth monitoring plan because this is a simple stack configuration.

```
const simpleMonPlanId = 'TWCORNEL5-488E42008B434177BC7D7BFF138D18EF'
```

```
const response = await fetch('https://api.epa.gov/easey/beta/emissions-mgmt/emissions/export?monitorPlanId='+simpleMonPlanId+'&year=2022&quarter=4&reportedValuesOnly=true',
{
    headers: {
        "x-api-key": "YOUR_API_KEY_HERE"
    },
    "method": "GET",
    });
const data = await response.json();
```



