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
// GENERAL FUNCTIONS
function constructTable(parentList, selector) {

  // Getting the all column names
  var cols = constructHeaders(parentList[0]["tableData"], selector); 

  // Start body
  var body = $('<tbody/>');

  for (var i = 0; i < parentList.length; i++){
    var obj = parentList[i];

    var list = obj["tableData"]

    $(selector).append('<tr><td class="bg-primary-lighter" colspan="'+String(cols.length+1)+'">'+obj["name"]+'</tr></td>');

    // Traversing the JSON data
    for (var j = 0; j < list.length; j++) {
        var row = $('<tr/>');  
        for (var colIndex = 0; colIndex < cols.length; colIndex++)
        {
            var val = list[j][cols[colIndex]];

            // If there is any key, which is matching
            // with the column name
            if (val == null) val = ""; 
                row.append($('<td/>').html(val));
        }

        // Adding each row to the body
        body.append(row);
    }
    // Adding body to table
    $(selector).append(body);
  }
}

function constructHeaders(list, selector) {
  var columns = [];
  // Construct the headercand header row
  var header = $('<thead/>');
  var headerrow = $('<tr/>');
  //header.append($('<tr/>').html(k));
   
  for (var i = 0; i < list.length; i++) {
      var row = list[i];
       
      for (var k in row) {
          if ($.inArray(k, columns) == -1) {
              columns.push(k);
               
              // Creating the header
              headerrow.append($('<th/>').html(k));
          }
      }
  }
  
  header.append(headerrow);
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
  emissionsExportElem.innerHTML = '<h4>Summary Value Data from Emissions Export Endpoint</h4><table class="usa-table usa-table--striped" id="simpleSummaryValueDataTable"></table>'
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
  emissionsExportElem.innerHTML = '<h4>Summary Value Data from Emissions Export Endpoint</h4><table class="usa-table usa-table--striped" id="commonSummaryValueDataTable"></table>'
  constructTable(summaryValueData, '#commonSummaryValueDataTable');
  //emissionsExportElem.innerHTML = '<code class="language-json">'+JSON.stringify(emissionsExportData, null, 4);+'</code>'
};

document.getElementById("commonLocationAttributeButton").onclick=async ()=>{
  var locationAttributeElem = document.getElementById("common-location-attributes-response");
  locationAttributeElem.getElementsByClassName("code-response-style")[0].innerHTML = 'loading...'
  
  var location6AttributeResponse = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/locations/'+commonLocId6+'/methods',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      referrerPolicy: "no-referrer",
      "method": "GET",
    });
  var location6AttributeData = await location6AttributeResponse.json();
  var location7AttributeResponse = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/locations/'+commonLocId7+'/methods',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      referrerPolicy: "no-referrer",
      "method": "GET",
    });
  var location7AttributeData = await location7AttributeResponse.json();
  var location5AttributeResponse = await fetch('https://api.epa.gov/easey/beta/monitor-plan-mgmt/locations/'+commonLocId5+'/methods',
    {
      headers: {
        "x-api-key": process.env.API_KEY
      },
      referrerPolicy: "no-referrer",
      "method": "GET",
    });
  var location5AttributeData = await location5AttributeResponse.json();
  //var locationAttributeData = location6AttributeData.concat(location7AttributeData);
  //locationAttributeData = locationAttributeData.concat(location5AttributeData);

  var locationAttributeData = [
    {
      "name": "Unit 1",
      "tableData": location6AttributeData
    },
    {
      "name": "Unit 2",
      "tableData": location7AttributeData},
    {
      "name": "Stack CS0AAN",
      "tableData": location5AttributeData}
  ]

  locationAttributeElem.innerHTML = '<h4 class="margin-x-2">Unit 1:</h4><table class="usa-table usa-table--striped" id="commonLocation6SummaryValueDataTable"></table>'
  constructTable(locationAttributeData, '#commonLocation6SummaryValueDataTable');
  //constructTable(location7AttributeData, '#commonLocation7SummaryValueDataTable');
  //constructTable(location5AttributeData, '#commonLocation5SummaryValueDataTable');
  
  
  //locationAttributeElem.innerHTML = '<code class="language-json">'+JSON.stringify(locationAttributeData, null, 4);+'</code>'
};