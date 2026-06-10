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
