document.addEventListener("DOMContentLoaded", function () {

    const raw = JSON.parse(document.getElementById("topic-data").textContent.trim());

    const topics = Object.keys(raw);
    const metrics = {
        "Avg Score":      topics.map(t => raw[t].average_score),
        "Avg Answers":    topics.map(t => raw[t].average_answer_count),
        "Resolved %":     topics.map(t => raw[t].resolved_percentage),
        "Accepted Rate %":topics.map(t => raw[t].accepted_resolution_rate),
    };

    const palette = [
        { bg: "rgba(79,142,255,0.75)",  border: "rgba(79,142,255,1)"  },
        { bg: "rgba(45,212,191,0.75)",  border: "rgba(45,212,191,1)"  },
        { bg: "rgba(167,139,250,0.75)", border: "rgba(167,139,250,1)" },
        { bg: "rgba(251,146,60,0.75)",  border: "rgba(251,146,60,1)"  },
    ];

    const datasets = Object.entries(metrics).map(([label, data], i) => ({
        label,
        data,
        backgroundColor: palette[i].bg,
        borderColor: palette[i].border,
        borderWidth: 1,
        borderRadius: 4,
        borderSkipped: false,
    }));

    const ctx = document.getElementById("topicsChart").getContext("2d");

    new Chart(ctx, {
        type: "bar",
        data: { labels: topics, datasets },
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
                },
                tooltip: {
                    backgroundColor: "#13161e",
                    borderColor: "rgba(255,255,255,0.1)",
                    borderWidth: 1,
                    titleColor: "#e8eaf0",
                    bodyColor: "#7a8096",
                    titleFont: { family: "'Plus Jakarta Sans', sans-serif", size: 13, weight: "600" },
                    bodyFont: { family: "'DM Mono', monospace", size: 12 },
                    padding: 12,
                    cornerRadius: 8,
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: "#7a8096",
                        font: { family: "'DM Mono', monospace", size: 12 },
                    },
                    grid:   { color: "rgba(255,255,255,0.04)" },
                    border: { color: "rgba(255,255,255,0.07)" }
                },
                y: {
                    ticks: {
                        color: "#7a8096",
                        font: { family: "'DM Mono', monospace", size: 11 },
                    },
                    grid:   { color: "rgba(255,255,255,0.04)" },
                    border: { color: "rgba(255,255,255,0.07)" }
                }
            }
        }
    });
});