function component() {
  const element = document.createElement('div');

  // Lodash, currently included via a script, is required for this line to work
  element.innerHTML = _.join(['Hello', 'webpack'], ' ');

  return element;
}

document.body.appendChild(component());

console.log(process.env.API_KEY);

(async () => {
  var API_KEY = process.env.API_KEY;
  const monPlanConfigResponse = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/configurations?orisCodes=3',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      "referrer": "https://usepa.github.io/",
      "method": "GET",
    });
  const monPlanData = await monPlanConfigResponse.json();
  const monPlanElem = document.getElementById("monitoringPlanConfigResponse");
  monPlanElem.innerHTML = '<code class="language-json">'+JSON.stringify(monPlanData, null, 4);+'</code>'
  const monPlanId = monPlanData[0].id;
  document.getElementById("monitoringPlanId").innerHTML = monPlanId;
  
  const emissionsExportResponse = await fetch('https://api.epa.gov/easey/beta/emissions-mgmt/emissions/export?monitorPlanId='+monPlanId+'&year=2022&quarter=4',
    {
      headers: {
        "x-api-key": "DEMO_KEY"
      },
      "referrer": "https://usepa.github.io/",
      "method": "GET",
    });
  const emissionsExportData = await emissionsExportResponse.json();
  const emissionsExportElem = document.getElementById("emissionsExportResponse");
  emissionsExportElem.innerHTML = '<code class="language-json">'+JSON.stringify(emissionsExportData, null, 4);+'</code>'
})();