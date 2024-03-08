console.log("TEST")
document.addEventListener("DOMContentLoaded", function () {
    const stateSelect = document.querySelector("#id_state");
    const citySelect = document.querySelector("#id_city");
    stateSelect.addEventListener("change", function () {
        const stateId = this.value;
        console.log(`/api/get-cities/${stateId}/`);
        fetch(`/api/get-cities/${stateId}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                citySelect.innerHTML = '';
                data.forEach(city => {
                    const option = new Option(city.name, city.id);
                    citySelect.appendChild(option);
                });
            })
            .catch(error => {
                console.error('There has been a problem with your fetch operation:', error);
            })
            .then(data => {
                citySelect.innerHTML = '';
                data.cities.forEach(city => {
                    const option = new Option(city.name, city.id);
                    citySelect.appendChild(option);
                })
                    .catch(error => {
                        console.error('There has been a problem with your fetch operation:', error);
                    });
            });
    });
});
