'use strict';
console.log($('#bar-chart'))
new Chart($('#bar-chart'), {
  type: 'bar',
  data: {
      labels: [
        "orly",
        "suncoat",
        "marcelle", 
        ],
  
     
    datasets: [
      {
        label: "Average Product Rating",
        data: [3.6, 3.76, 4.25],
        backgroundColor: [
          "#F4F7C1",
          "#C1F7F4",
          "#E4CDF7",
        ],
      },
    ],
  }
});
