import mdIntro from "./content/intro.md";
import mdSimpleConfig1 from "./content/simple-config-ex-1.md";
import mdSimpleConfig2 from "./content/simple-config-ex-2.md";
import mdSimpleConfig3 from "./content/simple-config-ex-3.md";

document.getElementById("intro").innerHTML = mdIntro;
document.getElementById("simple-config-ex-1").innerHTML = mdSimpleConfig1;
document.getElementById("simple-config-ex-2").innerHTML = mdSimpleConfig2;
document.getElementById("simple-config-ex-3").innerHTML = mdSimpleConfig3;

// Make sure these values match the markdown files!
const simpleMonPlanId = 'TWCORNEL5-488E42008B434177BC7D7BFF138D18EF';
const simpleLocId = '11';

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


document.getElementById("simpleMonPlanConfigButton").onclick=async ()=>{
  var monPlanElem = document.getElementById("simple-monitoring-plan-config-response");
  monPlanElem.innerHTML = 'loading...'

  var monPlanConfigResponse = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/configurations?orisCodes=3',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      "referrer": "https://usepa.github.io/",
      "method": "GET",
    });
  var monPlanData = await monPlanConfigResponse.json();
  monPlanElem.innerHTML = '<code class="language-json">'+JSON.stringify(monPlanData, null, 4);+'</code>'
};

document.getElementById("simpleEmissionsExportButton").onclick=async ()=>{
  var emissionsExportElem = document.getElementById("simple-emissions-export-response");
  emissionsExportElem.getElementsByClassName("code-response-style")[0].innerHTML = 'loading...'
  
  var emissionsExportResponse = await fetch('https://api.epa.gov/easey/beta/emissions-mgmt/emissions/export?monitorPlanId='+simpleMonPlanId+'&year=2022&quarter=4&reportedValuesOnly=true',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      referrerPolicy: "no-referrer",
      "method": "GET",
    });
    var emissionsExportData = await emissionsExportResponse.json();
  var summaryValueData = emissionsExportData["summaryValueData"];
  emissionsExportElem.innerHTML = '<h4>Summary Value Data from Emissions Export Endpoint</h4><table align="center" class="summaryTable" id="simpleSummaryValueDataTable" border="1"></table>'
  constructTable(summaryValueData, '#simpleSummaryValueDataTable');
  //emissionsExportElem.innerHTML = '<code class="language-json">'+JSON.stringify(emissionsExportData, null, 4);+'</code>'
};

document.getElementById("simpleLocationAttributeButton").onclick=async ()=>{
  var locationAttributeElem = document.getElementById("simple-location-attributes-response");
  locationAttributeElem.innerHTML = 'loading...'
  
  var locationAttributeResponse = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/locations/'+simpleLocId+'/attributes',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      referrerPolicy: "no-referrer",
      "method": "GET",
    });
    var locationAttributeData = await locationAttributeResponse.json();
  locationAttributeElem.innerHTML = '<code class="language-json">'+JSON.stringify(locationAttributeData, null, 4);+'</code>'
};

// Common stack examples
import mdCommonConfig1 from "./content/common-config-ex-1.md";
import mdCommonConfig2 from "./content/common-config-ex-2.md";
import mdCommonConfig3 from "./content/common-config-ex-3.md";

document.getElementById("intro").innerHTML = mdIntro;
document.getElementById("common-config-ex-1").innerHTML = mdCommonConfig1;
document.getElementById("common-config-ex-2").innerHTML = mdCommonConfig2;
document.getElementById("common-config-ex-3").innerHTML = mdCommonConfig3;

// Make sure these values match the markdown files!
const commonMonPlanId = 'TWCORNEL5-C0E3879920A14159BAA98E03F1980A7A';
const commonLocId6 = '6'; // location of the unit 1
const commonLocId7 = '7'; // location of the unit 2
const commonLocId5 = '5'; // location of the stack CS0AAN

document.getElementById("commonMonPlanConfigButton").onclick=async ()=>{
  var monPlanElem = document.getElementById("common-monitoring-plan-config-response");
  monPlanElem.innerHTML = 'loading...'

  var monPlanConfigResponse = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/configurations?orisCodes=3',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      "referrer": "https://usepa.github.io/",
      "method": "GET",
    });
  var monPlanData = await monPlanConfigResponse.json();
  monPlanElem.innerHTML = '<code class="language-json">'+JSON.stringify(monPlanData, null, 4);+'</code>'
};

document.getElementById("commonEmissionsExportButton").onclick=async ()=>{
  var emissionsExportElem = document.getElementById("common-emissions-export-response");
  emissionsExportElem.getElementsByClassName("code-response-style")[0].innerHTML = 'loading...'
  
  var emissionsExportResponse = await fetch('https://api.epa.gov/easey/beta/emissions-mgmt/emissions/export?monitorPlanId='+commonMonPlanId+'&year=2022&quarter=4&reportedValuesOnly=true',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      referrerPolicy: "no-referrer",
      "method": "GET",
    });
    var emissionsExportData = await emissionsExportResponse.json();
  var summaryValueData = emissionsExportData["summaryValueData"];
  emissionsExportElem.innerHTML = '<h4>Summary Value Data from Emissions Export Endpoint</h4><table align="center" class="summaryTable" id="commonSummaryValueDataTable" border="1"></table>'
  constructTable(summaryValueData, '#commonSummaryValueDataTable');
  //emissionsExportElem.innerHTML = '<code class="language-json">'+JSON.stringify(emissionsExportData, null, 4);+'</code>'
};

document.getElementById("commonLocationAttributeButton").onclick=async ()=>{
  var locationAttributeElem = document.getElementById("common-location-attributes-response");
  locationAttributeElem.getElementsByClassName("code-response-style")[0].innerHTML = 'loading...'
  
  var location6AttributeResponse = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/locations/'+commonLocId6+'/attributes',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      referrerPolicy: "no-referrer",
      "method": "GET",
    });
  var location6AttributeData = await location6AttributeResponse.json();
  var location7AttributeResponse = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/locations/'+commonLocId7+'/attributes',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      referrerPolicy: "no-referrer",
      "method": "GET",
    });
  var location7AttributeData = await location7AttributeResponse.json();
  var location5AttributeResponse = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/locations/'+commonLocId5+'/attributes',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      referrerPolicy: "no-referrer",
      "method": "GET",
    });
  var location5AttributeData = await location5AttributeResponse.json();
  locationAttributeElem.innerHTML = '<table align="center" class="summaryTable" id="commonLocation6SummaryValueDataTable" border="1"></table>'+
  '<table align="center" class="summaryTable" id="commonLocation7SummaryValueDataTable" border="1"></table>'+
  '<table align="center" class="summaryTable" id="commonLocation5SummaryValueDataTable" border="1"></table>'
  constructTable(location6AttributeData, '#commonLocation6SummaryValueDataTable');
  constructTable(location7AttributeData, '#commonLocation7SummaryValueDataTable');
  constructTable(location5AttributeData, '#commonLocation5SummaryValueDataTable');
  
  
  //locationAttributeElem.innerHTML = '<code class="language-json">'+JSON.stringify(locationAttributeData, null, 4);+'</code>'
};