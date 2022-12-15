
var socket =  io(location.origin);
var span = document.getElementById("data");

function button_handler() {
    socket.emit("start_data");
}

socket.on("new_data", function(data) {
    span.innerHTML = data.value;
});

socket.on("connect", function(_) {
    console.log("Connected:", _);
});