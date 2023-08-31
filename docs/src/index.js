import mdIntro from "./content/intro.md";
import mdSimpleConfig1 from "./content/simple-config-ex-1.md";
import mdSimpleConfig2 from "./content/simple-config-ex-2.md";
import mdSimpleConfig3 from "./content/simple-config-ex-3.md";

document.getElementById("intro").innerHTML = mdIntro;
document.getElementById("simple-config-ex-1").innerHTML = mdSimpleConfig1;
document.getElementById("simple-config-ex-2").innerHTML = mdSimpleConfig2;
document.getElementById("simple-config-ex-3").innerHTML = mdSimpleConfig3;

// Make sure these values match the markdown files!
const monPlanId = 'TWCORNEL5-488E42008B434177BC7D7BFF138D18EF';
const locId = '11';

// GENERAL FUNCTIONS
function constructTable(list, selector) {
             
  // Getting the all column names
  var cols = constructHeaders(list, selector); 

  // Traversing the JSON data
  for (var i = 0; i < list.length; i++) {
      var row = $('<tr/>');  
      for (var colIndex = 0; colIndex < cols.length; colIndex++)
      {
          var val = list[i][cols[colIndex]];
           
          // If there is any key, which is matching
          // with the column name
          if (val == null) val = ""; 
              row.append($('<td/>').html(val));
      }
       
      // Adding each row to the table
      $(selector).append(row);
  }
}

function constructHeaders(list, selector) {
  var columns = [];
  var header = $('<tr/>');
   
  for (var i = 0; i < list.length; i++) {
      var row = list[i];
       
      for (var k in row) {
          if ($.inArray(k, columns) == -1) {
              columns.push(k);
               
              // Creating the header
              header.append($('<th/>').html(k));
          }
      }
  }
   
  // Appending the header to the table
  $(selector).append(header);
      return columns;
} 
// END GENERAL FUNCTIONS


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
  const summaryValueData = emissionsExportData["summaryValueData"];
  constructTable(summaryValueData, '#summaryValueDataTable');
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
