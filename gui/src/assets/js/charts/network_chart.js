var ctx5 = document.getElementById("chart-bars-2").getContext("2d");
new Chart(ctx5, {
    type: "bar",
    data: {
    labels: ["M", "T", "W", "T", "F", "S", "S"],
    datasets: [{
        label: "Alerts",
        tension: 0.4,
        borderWidth: 0,
        borderRadius: 4,
        borderSkipped: false,
        backgroundColor: "rgba(255, 255, 255, .8)",
        data: [100, 200, 40, 52, 20, 15, 28],
        maxBarThickness: 6
    }, ],
    },
    options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
        display: false,
        }
    },
    interaction: {
        intersect: false,
        mode: 'index',
    },
    scales: {
        y: {
        grid: {
            drawBorder: false,
            display: true,
            drawOnChartArea: true,
            drawTicks: false,
            borderDash: [5, 5],
            color: 'rgba(255, 255, 255, .2)'
        },
        ticks: {
            suggestedMin: 0,
            suggestedMax: 500,
            beginAtZero: true,
            padding: 10,
            font: {
            size: 14,
            weight: 300,
            family: "Roboto",
            style: 'normal',
            lineHeight: 2
            },
            color: "#fff"
        },
        },
        x: {
        grid: {
            drawBorder: false,
            display: true,
            drawOnChartArea: true,
            drawTicks: false,
            borderDash: [5, 5],
            color: 'rgba(255, 255, 255, .2)'
        },
        ticks: {
            display: true,
            color: '#f8f9fa',
            padding: 10,
            font: {
            size: 14,
            weight: 300,
            family: "Roboto",
            style: 'normal',
            lineHeight: 2
            },
        }
        },
    },
    },
});

var ctx6 = document.getElementById("chart-bars-3").getContext("2d");
new Chart(ctx6, {
    type: "bar",
    data: {
    labels: ["M", "T", "W", "T", "F", "S", "S"],
    datasets: [{
        label: "Alerts",
        tension: 0.4,
        borderWidth: 0,
        borderRadius: 4,
        borderSkipped: false,
        backgroundColor: "rgba(255, 255, 255, .8)",
        data: [120, 39, 40, 52, 20, 15, 28],
        maxBarThickness: 6
    }, ],
    },
    options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
        display: false,
        }
    },
    interaction: {
        intersect: false,
        mode: 'index',
    },
    scales: {
        y: {
        grid: {
            drawBorder: false,
            display: true,
            drawOnChartArea: true,
            drawTicks: false,
            borderDash: [5, 5],
            color: 'rgba(255, 255, 255, .2)'
        },
        ticks: {
            suggestedMin: 0,
            suggestedMax: 500,
            beginAtZero: true,
            padding: 10,
            font: {
            size: 14,
            weight: 300,
            family: "Roboto",
            style: 'normal',
            lineHeight: 2
            },
            color: "#fff"
        },
        },
        x: {
        grid: {
            drawBorder: false,
            display: true,
            drawOnChartArea: true,
            drawTicks: false,
            borderDash: [5, 5],
            color: 'rgba(255, 255, 255, .2)'
        },
        ticks: {
            display: true,
            color: '#f8f9fa',
            padding: 10,
            font: {
            size: 14,
            weight: 300,
            family: "Roboto",
            style: 'normal',
            lineHeight: 2
            },
        }
        },
    },
    },
});