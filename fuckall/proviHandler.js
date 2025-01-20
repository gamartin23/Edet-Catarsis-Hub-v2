document.addEventListener('DOMContentLoaded', () => {
    const selectElement = document.getElementById("provincia-select");
    selectElement.addEventListener("change", function(e) {
        const selectedProvince = this.value;
        const gridItems = document.querySelectorAll(".grid-item");
        
        gridItems.forEach((item) => {
            if (selectedProvince === "todas" || item.getAttribute("data-provincia") === selectedProvince) {
                item.style.display = "";
            } else {
                item.style.display = "none";
            }
        });
    });
});