document
  .getElementById("algorithm-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch("/visualize", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        const visualization = d3.select("#visualization");
        visualization.selectAll("*").remove();

        if (formData.get("algorithm") === "binary_search") {
          const width = 800;
          const height = 400;
          const barWidth = width / data[0].current_array.length;

          const svg = visualization
            .append("svg")
            .attr("width", width)
            .attr("height", height);

          data.forEach((step, i) => {
            setTimeout(() => {
              svg.selectAll("*").remove();

              svg
                .selectAll("rect")
                .data(step.current_array)
                .enter()
                .append("rect")
                .attr("x", (d, i) => i * barWidth)
                .attr("y", (d) => height - d * 5)
                .attr("width", barWidth - 2)
                .attr("height", (d) => d * 5)
                .attr("fill", (d, idx) => {
                  if (idx === step.low) return "green";
                  if (idx === step.mid) return "blue";
                  if (idx === step.high) return "red";
                  return "steelblue";
                });

              svg
                .selectAll("text")
                .data(["Low", "Mid", "High"])
                .enter()
                .append("text")
                .attr("x", (d, i) => {
                  if (d === "Low") return step.low * barWidth + barWidth / 2;
                  if (d === "Mid") return step.mid * barWidth + barWidth / 2;
                  if (d === "High") return step.high * barWidth + barWidth / 2;
                })
                .attr("y", 20)
                .attr("text-anchor", "middle")
                .attr("fill", "black")
                .text((d) => d);

              if (step.found) {
                svg
                  .append("text")
                  .attr("x", width / 2)
                  .attr("y", height / 2)
                  .attr("text-anchor", "middle")
                  .attr("fill", "green")
                  .attr("font-size", "24px")
                  .text("Target Found");
              }
            }, i * 1000);
          });
        } else {
          const width = 800;
          const height = 400;
          const svg = visualization
            .append("svg")
            .attr("width", width)
            .attr("height", height);

          const renderStep = (step, i) => {
            const bars = svg.selectAll("rect").data(step, (d) => d);

            bars
              .enter()
              .append("rect")
              .attr("x", (d, i) => i * (width / step.length))
              .attr("y", (d) => height - d * 5)
              .attr("width", width / step.length - 2)
              .attr("height", (d) => d * 5)
              .attr("fill", "steelblue");

            bars
              .transition()
              .duration(500)
              .attr("x", (d, i) => i * (width / step.length))
              .attr("y", (d) => height - d * 5)
              .attr("width", width / step.length - 2)
              .attr("height", (d) => d * 5)
              .attr("fill", "steelblue");

            bars.exit().remove();
          };

          data.forEach((step, i) => {
            setTimeout(() => renderStep(step, i), i * 1000);
          });
        }
      });
  });
