const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Servir archivos estáticos desde la carpeta 'public'
app.use(express.static('public'));

io.on('connection', (socket) => {
    console.log('Un usuario se ha conectado');

    socket.on('disconnect', () => {
        console.log('Usuario desconectado');
    });

    socket.on('chat message', (msg) => {
        io.emit('chat message', msg); // Enviar mensaje a todos los usuarios conectados
    });
});

server.listen(3000, () => {
    console.log('Servidor escuchando en http://localhost:3000');
});
