function openJSON() {
window.open("data/data.json", "_blank");
}
function openXML() {
window.open("data/data.xml", "_blank")

}
function dark_mode() {
    var element = document.body;
    element.classList.toggle("dark-mode");
}
      function updateData() {
        fetch("data/data.json")
          .then(function (response) {
            return response.json();
          })
          .then(function (data) {
            document.getElementById("zeit").innerText = data["Time"];
            document.getElementById("boden").innerText =
              data["Boden Feuchtigkeit"];
            document.getElementById("temp_sht").innerText =
              data["Temperatur von SHT30"];
            document.getElementById("luft_sht").innerText =
              data["Luftfeuchte von SHT30"];
            document.getElementById("temp_sen").innerText =
              data["Temeratur von Sensor"];
          });
      }