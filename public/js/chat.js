var socket = io(); // Inicializa la conexión Socket.io

// Escucha el evento 'DOMContentLoaded' para asegurar que el HTML ha sido cargado completamente
document.addEventListener("DOMContentLoaded", (event) => {
    var form = document.getElementById('form');
    var input = document.getElementById('input');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        if (input.value) {
            socket.emit('chat message', input.value);
            input.value = '';
        }
    });

    socket.on('chat message', function(msg) {
        var item = document.createElement('li');
        item.textContent = msg;
        document.getElementById('messages').appendChild(item);
        window.scrollTo(0, document.body.scrollHeight);
    });
});
