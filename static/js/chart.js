var ctx = document.getElementById("myLineChart").getContext("2d");
var myLineChart = new Chart(ctx, {
	type: "line",
	data: {
		labels: ["January", "February", "March", "April", "May", "June", "July"],
		datasets: [
			{
				label: "Student Performance",
				data: [65, 59, 80, 81, 56, 55, 40],
				borderColor: "rgb(37, 65, 110)",
				backgroundColor: "rgba(37, 65, 110, 0.2)",
				fill: true,
			},
		],
	},
	options: {
		responsive: true,
		scales: {
			x: {
				beginAtZero: true,
			},
			y: {
				beginAtZero: true,
			},
		},
	},
});
