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
      },
    ],
  }
});
