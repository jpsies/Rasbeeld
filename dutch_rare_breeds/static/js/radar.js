var myConfig = {
    "type":"radar",
    "plot":{
        "aspect":"area",
        "value-box":{ //Value Boxes
        "font-family":"Georgia",
        "font-weight":"normal"
        }
    },
    "scale-k": {
    "labels": ["Vrouwelijke fokdieren", "Trend in vrouwelijke fokdieren", "Inteelt ratio per generatie", "Geografische spreiding", "Rasvereniging", "Socio-economische context"], //Scale Labels
    "item": { //To style your scale labels.
      "font-color": "orange",
      "font-family": "Georgia",
      "font-size": 12,
      "font-weight": "bold",
      "font-style": "italic"
      },
    "tick": { //Tick Marks
      "line-color": "orange",
      "line-width": 3,
      "size": 15,
      "placement": "outer"
      }
    },
    "scale-v":{
    "values":"0:5:1", //To set your min/max/step.
    "item":{ //To style your scale labels.
      "font-color":"orange",
      "font-family":"Georgia",
      "font-size":12,
      "font-weight":"bold",
      "font-style":"italic"
      },
    "guide":{ //Guides (both lines and background colors)
      "background-color":"#f0f0f5 #e0e0eb"
      }
    },
    "series":[
        {
            "values":radarvalues
        },
    ]
};

zingchart.render({ 
	id : 'myChart', 
	data : myConfig, 
	height: '100%', 
	width: '100%' 
});
