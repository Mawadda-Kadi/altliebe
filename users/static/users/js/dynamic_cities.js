document.addEventListener("DOMContentLoaded", function () {
    const stateSelect = document.querySelector("#id_state");
    const cityInput = document.querySelector("#id_city");

    stateSelect.addEventListener("change", function () {
        const stateId = this.value;
        fetch(`/get-cities/${stateId}/`)
            .then(response => response.json())
            .then(data => {
                cityInput.innerHTML = '';
                data.cities.forEach(city => {
                    const option = new Option(city.name, city.id);
                    cityInput.appendChild(option);
                });
            });
    });
});
