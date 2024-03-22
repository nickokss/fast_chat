# Fast chat
* Se necesitan las siguientes librerias de NodeJS:
```sh
npm init -y
npm install express
npm install socket.io
```

* Ejecutar la aplicación:
```
node src/server.js
```
* Estructura del proyecto
```
fast_chat/
│
├── node_modules/
│   └── (dependencias de npm)
│
├── public/
│   ├── css/
│   │   └── estilos.css         # Estilos CSS para tu frontend
│   │
│   ├── js/
│   │   └── chat.js             # Lógica de JavaScript para el frontend
│   │
│   └── index.html              # Página principal del chat (cliente)
│
├── src/
│   ├── controllers/            # Controladores para manejar la lógica específica
│   │   └── chatController.js
│   │
│   ├── models/                 # Modelos de datos (si decides interactuar con una base de datos)
│   │   └── userModel.js
│   │
│   ├── routes/                 # Rutas para tu aplicación web
│   │   └── chatRoutes.js
│   │
│   └── server.js               # Archivo principal del servidor
│
├── .gitignore                  # Archivos y carpetas ignoradas por git
├── package.json                # Configuración del proyecto y dependencias
└── README.md                   # Documentación del proyecto
```
