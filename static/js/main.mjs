
var socket =  io.connect(location.origin);
var button = document.getElementById("start");
var span = document.getElementById("data")

button.addEventListener("click", function() {
    socket.emit("start_data", function(response) {
        console.log(response);
    });
});

socket.on("new_data", function(data) {
    span.innerHTML = data.value;
});