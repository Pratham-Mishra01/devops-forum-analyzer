document.addEventListener("DOMContentLoaded", function () {

    const labelsText = document.getElementById("tag-labels").textContent.trim();
    const valuesText = document.getElementById("tag-values").textContent.trim();

    const labels = JSON.parse(labelsText);
    const values = JSON.parse(valuesText);

    const wrappedLabels = labels.map(label => {
        if (label.length > 12) {
            return label.split("-");
        }
        return label;
    });

    const ctx = document.getElementById("tagsChart").getContext("2d");

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: wrappedLabels,
            datasets: [{
                label: "Tag Frequency",
                data: values,
                backgroundColor: "rgba(79, 142, 255, 0.7)",
                borderColor: "rgba(79, 142, 255, 1)",
                borderWidth: 1,
                borderRadius: 5,
                borderSkipped: false,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    labels: {
                        color: "#7a8096",
                        font: { family: "'DM Mono', monospace", size: 12 },
                        boxWidth: 14,
                        boxHeight: 14,
                    }
                }
            },
            scales: {
                x: {
                    ticks: {
                        maxRotation: 0,
                        minRotation: 0,
                        autoSkip: false,
                        color: "#7a8096",
                        font: { family: "'DM Mono', monospace", size: 11 },
                    },
                    grid: {
                        color: "rgba(255,255,255,0.04)",
                    },
                    border: {
                        color: "rgba(255,255,255,0.07)"
                    }
                },
                y: {
                    ticks: {
                        color: "#7a8096",
                        font: { family: "'DM Mono', monospace", size: 11 },
                    },
                    grid: {
                        color: "rgba(255,255,255,0.04)",
                    },
                    border: {
                        color: "rgba(255,255,255,0.07)"
                    }
                }
            }
        }
    });

});