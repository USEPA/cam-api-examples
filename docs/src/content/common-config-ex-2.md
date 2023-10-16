### Use a monitoring plan id

The first "Id" of each object in the response above is the unique identifier (Id) of a monitoring configuration record. You will see this as parameters to use in other endpoints (named: monitorPlanId, monPlanIds or planIds). For example, lets take the second monitoring plan id in the response above and use it.

Below is a javascript example script collecting data from the emissions export endpoint from the [Emissions API](https://www.epa.gov/power-sector/cam-api-portal#/swagger/beta-emissions-mgmt).

**_NOTE:_**  We use the second monitoring plan because this is a common stack configuration.

```
const commonMonPlanId = 'TWCORNEL5-C0E3879920A14159BAA98E03F1980A7A'
```

```
const response = await fetch('https://api.epa.gov/easey/beta/emissions-mgmt/emissions/export?monitorPlanId='+commonMonPlanId+'&year=2022&quarter=4&reportedValuesOnly=true',
{
    headers: {
        "x-api-key": "YOUR_API_KEY_HERE"
    },
    referrerPolicy: "no-referrer",
    "method": "GET",
    });
const data = await response.json();
```
