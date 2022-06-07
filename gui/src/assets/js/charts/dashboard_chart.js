// var ctx = document.getElementById("chart-bars").getContext("2d");
// new Chart(ctx, {
//     type: "bar",
//     data: {
//     labels: ["M", "T", "W", "T", "F", "S", "S"],
//     datasets: [{
//         label: "Alerts",
//         tension: 0.4,
//         borderWidth: 0,
//         borderRadius: 4,
//         borderSkipped: false,
//         backgroundColor: "rgba(255, 255, 255, .8)",
//         data: [20, 39, 40, 52, 20, 15, 28],
//         maxBarThickness: 6
//     }, ],
//     },
//     options: {
//     responsive: true,
//     maintainAspectRatio: false,
//     plugins: {
//         legend: {
//         display: false,
//         }
//     },
//     interaction: {
//         intersect: false,
//         mode: 'index',
//     },
//     scales: {
//         y: {
//         grid: {
//             drawBorder: false,
//             display: true,
//             drawOnChartArea: true,
//             drawTicks: false,
//             borderDash: [5, 5],
//             color: 'rgba(255, 255, 255, .2)'
//         },
//         ticks: {
//             suggestedMin: 0,
//             suggestedMax: 500,
//             beginAtZero: true,
//             padding: 10,
//             font: {
//             size: 14,
//             weight: 300,
//             family: "Roboto",
//             style: 'normal',
//             lineHeight: 2
//             },
//             color: "#fff"
//         },
//         },
//         x: {
//         grid: {
//             drawBorder: false,
//             display: true,
//             drawOnChartArea: true,
//             drawTicks: false,
//             borderDash: [5, 5],
//             color: 'rgba(255, 255, 255, .2)'
//         },
//         ticks: {
//             display: true,
//             color: '#f8f9fa',
//             padding: 10,
//             font: {
//             size: 14,
//             weight: 300,
//             family: "Roboto",
//             style: 'normal',
//             lineHeight: 2
//             },
//         }
//         },
//     },
//     },
// });


// var ctx2 = document.getElementById("chart-line").getContext("2d");
// new Chart(ctx2, {
//     type: "line",
//     data: {
//     labels: ["M", "T", "W", "T", "F", "S", "S"],
//     datasets: [{
//         label: "Total Alerts (Weekly)",
//         tension: 0,
//         borderWidth: 0,
//         pointRadius: 5,
//         pointBackgroundColor: "rgba(255, 255, 255, .8)",
//         pointBorderColor: "transparent",
//         borderColor: "rgba(255, 255, 255, .8)",
//         borderColor: "rgba(255, 255, 255, .8)",
//         borderWidth: 4,
//         backgroundColor: "transparent",
//         fill: true,
//         data: [20, 59, 89, 141, 161, 176, 204],
//         maxBarThickness: 6

//     }],
//     },
//     options: {
//     responsive: true,
//     maintainAspectRatio: false,
//     plugins: {
//         legend: {
//         display: false,
//         }
//     },
//     interaction: {
//         intersect: false,
//         mode: 'index',
//     },
//     scales: {
//         y: {
//         grid: {
//             drawBorder: false,
//             display: true,
//             drawOnChartArea: true,
//             drawTicks: false,
//             borderDash: [5, 5],
//             color: 'rgba(255, 255, 255, .2)'
//         },
//         ticks: {
//             display: true,
//             color: '#f8f9fa',
//             padding: 10,
//             font: {
//             size: 14,
//             weight: 300,
//             family: "Roboto",
//             style: 'normal',
//             lineHeight: 2
//             },
//         }
//         },
//         x: {
//         grid: {
//             drawBorder: false,
//             display: false,
//             drawOnChartArea: false,
//             drawTicks: false,
//             borderDash: [5, 5]
//         },
//         ticks: {
//             display: true,
//             color: '#f8f9fa',
//             padding: 10,
//             font: {
//             size: 14,
//             weight: 300,
//             family: "Roboto",
//             style: 'normal',
//             lineHeight: 2
//             },
//         }
//         },
//     },
//     },
// });

// var ctx3 = document.getElementById("chart-line-tasks").getContext("2d");
// new Chart(ctx3, {
//     type: "line",
//     data: {
//     labels: ["Jan","Feb","Mar","Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
//     datasets: [{
//         label: "Total Rules",
//         tension: 0,
//         borderWidth: 0,
//         pointRadius: 5,
//         pointBackgroundColor: "rgba(255, 255, 255, .8)",
//         pointBorderColor: "transparent",
//         borderColor: "rgba(255, 255, 255, .8)",
//         borderWidth: 4,
//         backgroundColor: "transparent",
//         fill: true,
//         data: [20000, 20002, 19996, 20007, 20014, 20022, 20022, 20030, 20035, 20020, 20020, 20022],
//         maxBarThickness: 6

//     }],
//     },
//     options: {
//     responsive: true,
//     maintainAspectRatio: false,
//     plugins: {
//         legend: {
//         display: false,
//         }
//     },
//     interaction: {
//         intersect: false,
//         mode: 'index',
//     },
//     scales: {
//         y: {
//         grid: {
//             drawBorder: false,
//             display: true,
//             drawOnChartArea: true,
//             drawTicks: false,
//             borderDash: [5, 5],
//             color: 'rgba(255, 255, 255, .2)'
//         },
//         ticks: {
//             display: true,
//             padding: 10,
//             color: '#f8f9fa',
//             font: {
//             size: 14,
//             weight: 300,
//             family: "Roboto",
//             style: 'normal',
//             lineHeight: 2
//             },
//         }
//         },
//         x: {
//         grid: {
//             drawBorder: false,
//             display: false,
//             drawOnChartArea: false,
//             drawTicks: false,
//             borderDash: [5, 5]
//         },
//         ticks: {
//             display: true,
//             color: '#f8f9fa',
//             padding: 10,
//             font: {
//             size: 14,
//             weight: 300,
//             family: "Roboto",
//             style: 'normal',
//             lineHeight: 2
//             },
//         }
//         },
//     },
//     },
// });

// var ctx4 = document.getElementById("pie-chart0").getContext("2d");
// new Chart(ctx4, {
//     type: "pie",
//     data: {
//     labels: [
//     'High',
//     'Medium',
//     'Low'
//     ],
//     datasets: [{
//     label: 'My First Dataset',
//     data: [300, 50, 100],
//     backgroundColor: [
//         'rgb(255, 99, 132)',
//         'rgb(255, 205, 86)',
//         'rgb(76, 244, 59)'
//     ],
//     hoverOffset: 4
//     }]
// },
// });