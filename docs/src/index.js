
var API_KEY = process.env.API_KEY;
const monPlanId = 'TWCORNEL5-488E42008B434177BC7D7BFF138D18EF';
document.getElementById("monitoring-plan-id").innerHTML = monPlanId;
document.getElementById("emissions-export-url").innerHTML = 'https://api.epa.gov/easey/beta/emissions-mgmt/emissions/export?monitorPlanId='+monPlanId+'&year=2022&quarter=4&reportedValuesOnly=true';

const locId = '11';
document.getElementById("location-id").innerHTML = locId;
document.getElementById("location-attributes-url").innerHTML = 'https://api.epa.gov/easey/beta/monitor-plan-mgmt/locations/'+locId+'/attributes';

document.getElementById("monPlanConfigButton").onclick=async ()=>{
  const monPlanElem = document.getElementById("monitoring-plan-config-response");
  monPlanElem.innerHTML = 'loading...'

  const monPlanConfigResponse = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/configurations?orisCodes=3',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      "referrer": "https://usepa.github.io/",
      "method": "GET",
    });
  const monPlanData = await monPlanConfigResponse.json();
  monPlanElem.innerHTML = '<code class="language-json">'+JSON.stringify(monPlanData, null, 4);+'</code>'
};

document.getElementById("emissionsExportButton").onclick=async ()=>{
  const emissionsExportElem = document.getElementById("emissions-export-response");
  emissionsExportElem.innerHTML = 'loading...'
  
  const emissionsExportResponse = await fetch('https://api.epa.gov/easey/beta/emissions-mgmt/emissions/export?monitorPlanId='+monPlanId+'&year=2022&quarter=4&reportedValuesOnly=true',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      referrerPolicy: "no-referrer",
      "method": "GET",
    });
  const emissionsExportData = await emissionsExportResponse.json();
  emissionsExportElem.innerHTML = '<code class="language-json">'+JSON.stringify(emissionsExportData, null, 4);+'</code>'
};

document.getElementById("locationAttributeButton").onclick=async ()=>{
  const locationAttributeElem = document.getElementById("location-attributes-response");
  locationAttributeElem.innerHTML = 'loading...'
  
  const locationAttributeResponse = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/locations/'+locId+'/attributes',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      referrerPolicy: "no-referrer",
      "method": "GET",
    });
  const locationAttributeData = await locationAttributeResponse.json();
  locationAttributeElem.innerHTML = '<code class="language-json">'+JSON.stringify(locationAttributeData, null, 4);+'</code>'
};
