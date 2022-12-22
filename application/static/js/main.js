
var socket =  io(location.origin);
var span = document.getElementById("data");

function button_handler() {
    socket.emit("start_data_stream");
}

socket.on("new_data", function(data) {
    span.innerHTML = data.value;
});
