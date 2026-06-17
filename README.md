# Proyecto-de-graduacion
Este proyecto ayuda a reducir un poco el cambio climatico.

La idea que decidi tener propia de mi es la siguiente (Esta resumida por Gemini, ya que la idea original escrita por mi
estaba algo desordenada pero esta que le pedi que me resumiera esta mucho mejor y sigue explicando mi idea principal):

# Inicio de la idea/inspiracion:

EcoEcho Bot 🌍🎙️
EcoEcho Bot es un asistente virtual para Discord desarrollado en Python, diseñado para mitigar los efectos del cambio climático a través de la neurociencia de los hábitos. El proyecto no busca imponer grandes sacrificios físicos, sino automatizar la educación ambiental en los entornos digitales donde los jóvenes pasan su tiempo, promoviendo micro-acciones y hábitos sostenibles cotidianos mediante interacciones de texto y síntesis de voz (TTS).

🎯 Idea Principal y Funcionamiento
El bot opera bajo tres pilares fundamentales dentro de un servidor de Discord:

Concientización Activa por Voz: Al momento en que un usuario se conecta a un canal de voz, el bot se une brevemente y, utilizando síntesis de voz, reproduce un recordatorio ecológico rápido o un "micro-tip" de ahorro antes de retirarse.

Alertas Cotidianas Dinámicas: A través de canales de texto, el bot envía recordatorios aleatorios sobre tareas del día a día (gestión de residuos, apagado de electrodomésticos en modo espera, reciclaje, etc.).

Integración con el Clima Local (Eco-Adaptabilidad): Mediante la conexión con una API de clima, el bot analiza la temperatura y el estado del tiempo de la región configurada para ofrecer consejos adaptados al entorno real en ese instante (ej. optimización del uso de agua en días de lluvia o reducción de aire acondicionado/ventiladores).

🛠️ Tecnologías y Módulos de Clase Aplicados
Para el desarrollo de este proyecto se integran los siguientes conocimientos adquiridos en el curso:

Bots de Discord (discord.py): Gestión de eventos en tiempo real (detección de estado de voz con on_voice_state_update) y creación de comandos de interacción.

Clases y Métodos: Modularización y estructuración limpia del código orientada a objetos para manejar los diferentes módulos del bot.

Consumo de APIs Externas: Conexión con servicios meteorológicos en formato JSON para obtener datos en tiempo real de temperatura y predicción de lluvia.

Síntesis de Voz (Text-to-Speech): Implementación de librerías de procesamiento de voz para transformar los consejos de texto en audio directamente en los canales de Discord.

Archivos y Entornos Virtuales: Uso de variables de entorno (.env) para la protección de tokens y gestión aislada de dependencias.

Buenas Prácticas (PEP-8): Código limpio, estructurado y documentado que facilita su escalabilidad y revisión.

💡 Ejemplos de Micro-Tips Automatizados

🔊 Por voz: "¡Hola! Si vas a jugar por varias horas, recuerda reducir el brillo de tu pantalla un 10%. Ahorrarás energía sin darte cuenta."

💬 Por texto (Clima lluvioso): 🌧️ "Está lloviendo en tu zona. Es un gran momento para recordar recolectar agua lluvia para las plantas o las tareas del hogar."


# Bibliotecas a Instalar (pip install)
Estas son las fijas que vas a necesitar. Las puedes dejar anotadas en un archivo requirements.txt:

discord.py (Para el bot de Discord y conectar a los canales de voz).

requests (Para conectar con la API de clima).

python-dotenv (Para ocultar el Token del bot de forma segura).

gTTS o pyttsx3 (Para la síntesis de voz; revisaremos cuál te da mejor tono).

PyNaCl (Obligatoria para que Discord te deje reproducir audio en canales de voz).


💬 Por texto (Cotidiano): 🗑️ "Recordatorio de rutina: ¿Ya sacaste la basura y te aseguraste de clasificar los residuos en la caneca correspondiente?"

# Fin de la idea


# Una pequeña nota para los articulos que tal vez ayuden en futuro. (https://www.un.org/es/climatechange/science/causes-effects-climate-change), (https://www.un.org/es/un75/climate-crisis-race-we-can-win)


# Librerias y comandos de Entorno Virtual:

Primer comando: python -m venv .venv (Para crear el entorno virtual aislado de Python)

Segundo comando (Para activarlo En Windows (PowerShell): .venv\Scripts\Activate.ps1

(Si les sale un error al colocar el .venv\Scripts\Activate.ps1, sigan estos pasos:


Mira tu terminal abajo a la derecha. Arriba de las letras rojas, hay un menú desplegable que dice powershell junto a un icono de un bote de basura y un signo de más (+).

Dale clic a la flechita que apunta hacia abajo que está al lado del signo +.

Selecciona Command Prompt (o Git Bash si lo tienes instalado). Se te abrirá una pestaña de terminal nueva y limpia.

En esa nueva terminal, ejecuta este comando para activarlo (ojo, cambia un poquito la barra diagonal porque es CMD):

DOS
.venv\Scripts\activate.bat
Sabrás que funcionó perfectamente porque ahora verás las letras (.venv) al inicio de tu línea de comandos.)



Estas son el resto de librerias (las puedes colocar en un nuevo archivo de el VS Code llamado requirements.txt):

discord.py
python-dotenv
requests
PyNaCl
gTTS



# Procedimientos despues de esto:

Sigue estos pasos en esa misma terminal de Git Bash (donde dice (.venv)):

Escribe el siguiente comando y presiona Enter:

Bash
pip install -r requirements.txt
Verás que empiezan a salir un montón de líneas de texto mientras se descargan discord.py, gTTS y las demás librerías. Espera un momento a que termine y te vuelva a aparecer la línea normal para escribir.


Hecho esto sin problemas, ahora se puede hacer esto:

Siguiente Paso: Crear el archivo de configuración .env
El Token del bot es como la contraseña maestra. Para no dejarlo expuesto en el código, lo vamos a guardar en un archivo oculto del sistema.

En la parte izquierda de tu VS Code (en el explorador de archivos), crea un nuevo archivo llamado exactamente .env (ojo: empieza con un punto y no lleva ninguna extensión como .txt ni nada, solo .env).

Abre el archivo y escribe lo siguiente dentro:

Plaintext
DISCORD_TOKEN=tu_token_secreto_aqui


Ahora, ve a tu panel de desarrolladores de Discord (donde creaste el bot), copia el Token real y pégalo justo después del símbolo =, reemplazando el texto tu_token_secreto_aqui. (Asegúrate de que no queden espacios entre el = y tu token).

Guarda el archivo con Ctrl + S.
