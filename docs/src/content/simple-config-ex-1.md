### Use an Oris Code (Facility Id) to get a monitoring plan configuration

The best place to start for most people is with the **configurations endpoint** in the [Monitoring Plan API](https://www.epa.gov/power-sector/cam-api-portal#/swagger/beta-monitor-plan-mgmt)

Below is a javascript example script making a call to the configurations endpoint using oris code 3 (Barry).

```
const response = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/configurations?orisCodes=3',
{
    headers: {
        "x-api-key": "YOUR_API_KEY_HERE"
    },
    referrerPolicy: "no-referrer",
    "method": "GET",
});
const data = await response.json();
```