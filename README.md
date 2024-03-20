# Fast chat
* Se necesitan las siguientes librerias de NodeJS:
```sh
npm init -y
npm install express
npm install socket.io
```
fast_chat/
│
├── node_modules/                   # Directorio de módulos de Node.js (creado por npm)
│
├── public/                         # Carpeta para archivos estáticos accesibles al cliente
│   ├── css/                        # Hojas de estilo CSS
│   │   └── main.css                # Estilo principal
│   ├── js/                         # Código JavaScript del lado del cliente
│   │   └── chat.js                 # Lógica del chat del lado del cliente
│   └── index.html                  # Página principal de la aplicación de chat
│
├── src/                            # Código fuente del lado del servidor
│   ├── routes/                     # Rutas de tu aplicación
│   │   └── index.js                # Archivo de rutas principal
│   ├── controllers/                # Controladores para manejar la lógica de negocio
│   ├── models/                     # Modelos de datos (si estás utilizando una base de datos)
│   └── server.js                   # Punto de entrada del servidor y configuración de socket.io
│
├── .gitignore                      # Archivos y carpetas ignorados por Git (node_modules, .env, etc.)
├── package.json                    # Configuración del proyecto y dependencias de npm
├── package-lock.json               # Bloqueo de versiones de dependencias para asegurar compatibilidad
└── README.md                       # Documentación inicial del proyecto
