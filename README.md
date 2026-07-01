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


OJO: Asegúrate de que no haya espacios alrededor del signo igual (=). Debe ir la palabra DISCORD_TOKEN, luego el =, y de inmediato tu código secreto o Token. 


Despues de esto, puedes continuar con:

Copia este bloque de código y pégalo dentro de main.py:


import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Cargamos de forma manual las variables del archivo .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


# Creamos la clase principal de nuestro bot de forma organizada
class MottainaiBot(commands.Bot):

    def __init__(self):
        # Configuramos los permisos (intents) necesarios para Discord
        intents = discord.Intents.default()
        intents.message_content = True  # Para leer comandos de texto
        intents.voice_states = True     # Para detectar canales de voz luego

        # Inicializamos el bot con el prefijo "!" y sus permisos
        super().__init__(command_prefix="!", intents=intents)

    # Evento automático que avisa cuando el bot se conecta a Discord
    async def on_ready(self):
        print("─" * 50)
        print("✨ ¡MottainaiBot (もったいない) está en línea! ✨")
        print(f"Conectado con éxito como: {self.user.name}")
        print("─" * 50)


# Punto de arranque de la aplicación
if __name__ == "__main__":
    bot = MottainaiBot()
    bot.run(TOKEN)



Una vez hecho esto. Siguiente Paso: ¡Encender el Bot!
Una vez que pegues el código en main.py y lo guardes (Ctrl + S), sigue estos pasos para ponerlo en marcha:

Ve a la terminal de Git Bash abajo (donde sale (.venv)).

Escribe el comando para ejecutar tu archivo principal:

Bash
python main.py
Presiona Enter.

Si todo está bien configurado con el token y los permisos en el panel de Discord, deberías ver cómo se imprime en tu terminal el mensaje decorado:
✨ ¡MottainaiBot (もったいない) está en línea! ✨




Sin embargo, si hay alguna falla en el codigo, aqui esta uno completo tipo "punto de control" funcional por si cualquier cosa.

Codigo:

```

import random
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True


bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


tips_ecologicos = [
    {
        "categoria": "energia",
        "texto": (
            "Si vas a jugar o estudiar por varias horas, recuerda "
            "reducir el brillo de tu pantalla un 10%. Ahorrarás."
        )
    },
    {
        "categoria": "energia",
        "texto": (
            "Terminaste de usar tu consola o PC? Recuerda apagar "
            "la multitoma. En modo espera siguen consumiendo luz."
        )
    },
    {
        "categoria": "residuos",
        "texto": (
            "Recordatorio de rutina: Asegúrate de separar bien los "
            "residuos. El plástico y cartón limpio van al reciclaje."
        )
    },
    {
        "categoria": "agua",
        "texto": (
            "Al lavarte los dientes, cierra la llave mientras te "
            "cepillas. Es un micro-hábito que salva litros de agua."
        )
    }
]


@bot.event
async def on_ready():

    print("─" * 50)

    print("✨ ¡MottainaiBot está en línea! ✨")

    print(f"Conectado como: {bot.user}")

    print("COMANDOS CARGADOS:")

    for comando in bot.commands:
        print(comando.name)

    print("─" * 50)


@bot.command(name="tip")
async def enviar_tip(ctx):

    tip = random.choice(tips_ecologicos)

    await ctx.send(
        f"🌱 **[Mottainai Tip]** {tip['texto']}"
    )


@bot.command(name="ecohelp")
async def ecohelp(ctx):

    mensaje = (
        "🌍 **EcoEcho Bot - Comandos disponibles**\n\n"

        "🌱 `!tip`\n"
        "Muestra un consejo ecológico aleatorio.\n\n"

        "📖 `!ecohelp`\n"
        "Muestra la lista de comandos disponibles."
    )

    await ctx.send(mensaje)


bot.run(TOKEN)

```


# Codigo mejorado funcional:

```

import random
import os
import requests
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

CIUDAD = "Medellin"

LATITUD = "6.25184"
LONGITUD = "-75.56359"

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True


bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


tips_ecologicos = [
    {
        "categoria": "energia",
        "texto": (
            "Si vas a jugar o estudiar por varias horas, recuerda "
            "reducir el brillo de tu pantalla un 10%. Ahorrarás."
        )
    },
    {
        "categoria": "energia",
        "texto": (
            "¿Terminaste de usar tu consola o PC? Recuerda apagar "
            "la multitoma. En modo espera siguen consumiendo luz."
        )
    },
    {
        "categoria": "residuos",
        "texto": (
            "Recordatorio de rutina: Asegúrate de separar bien los "
            "residuos. El plástico y cartón limpio van al reciclaje."
        )
    },
    {
        "categoria": "agua",
        "texto": (
            "Al lavarte los dientes, cierra la llave mientras te "
            "cepillas. Es un micro-hábito que salva litros de agua."
        )
    },
    {
        "categoria": "energia",
        "texto": (
            "Si sales de una habitación por varios minutos, "
            "apaga las luces que no estés utilizando."
        )
    },
    {
        "categoria": "agua",
        "texto": (
            "Utiliza un vaso al cepillarte los dientes. "
            "Así evitarás desperdiciar agua."
        )
    },
    {
        "categoria": "residuos",
        "texto": (
            "Antes de botar un recipiente, revisa si puede "
            "ser reutilizado en casa."
        )
    },
    {
        "categoria": "transporte",
        "texto": (
            "Si un trayecto es corto, considera caminar "
            "en lugar de usar un vehículo."
        )
    },
    {
        "categoria": "energia",
        "texto": (
            "Desconecta los cargadores que no estés usando. "
            "Siguen consumiendo energía."
        )
    },
    {
        "categoria": "consumo",
        "texto": (
            "Lleva una botella reutilizable cuando salgas "
            "de casa para reducir residuos plásticos."
        )
    },
    {
        "categoria": "tecnologia",
        "texto": (
            "Activa el modo ahorro de energía en tu celular "
            "cuando no necesites el máximo rendimiento."
        )
    }
]


CANAL_RECORDATORIOS = "eco-recordatorios"

ultimo_tip = None


@bot.event
async def on_ready():

    print("─" * 50)

    print("✨ ¡MottainaiBot está en línea! ✨")

    print(f"Conectado como: {bot.user}")

    print("COMANDOS CARGADOS:")

    for comando in bot.commands:
        print(comando.name)

    print("─" * 50)
    if not enviar_recordatorios.is_running():

        enviar_recordatorios.start()


@tasks.loop(minutes=30)
async def enviar_recordatorios():

    canal = None

    for servidor in bot.guilds:

        canal = discord.utils.get(
            servidor.text_channels,
            name=CANAL_RECORDATORIOS
        )

        if canal:

            global ultimo_tip

            tip = random.choice(tips_ecologicos)

            while tip == ultimo_tip:

                tip = random.choice(tips_ecologicos)

            ultimo_tip = tip

            await canal.send(
                f"🌍 **EcoEcho Recordatorio**\n\n"
                f"{tip['texto']}"
            )


@bot.command(name="tip")
async def enviar_tip(ctx):

    tip = random.choice(tips_ecologicos)

    await ctx.send(
        f"🌱 **[Mottainai Tip]** {tip['texto']}"
    )


@bot.command(name="clima")
async def clima(ctx):

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LATITUD}"
        f"&longitude={LONGITUD}"
        "&current=temperature_2m"
    )

    respuesta = requests.get(url)

    datos = respuesta.json()

    temperatura = datos["current"]["temperature_2m"]

    if temperatura >= 28:

        consejo = (
            "☀️ Hace bastante calor. "
            "Aprovecha la ventilación natural antes de "
            "encender ventiladores o aire acondicionado."
        )

    elif temperatura <= 10:

        consejo = (
            "❄️ Hace bastante frío. "
            "Aprovecha la energía solar para calentar tu hogar "
            "o cualquier sistema eléctrico para calentar el hogar."
        )

    elif temperatura <= 18:

        consejo = (
            "🧥 La temperatura está fresca. "
            "Aprovecha la luz natural antes de encender luces."
        )

    else:

        consejo = (
            "🌱 Temperatura agradable. "
            "Es un buen momento para realizar actividades "
            "al aire libre."
        )

    await ctx.send(
        f"🌤️ **Clima en {CIUDAD}**\n\n"
        f"🌡️ Temperatura actual: {temperatura}°C\n\n"
        f"{consejo}"
    )


@bot.command(name="ecohelp")
async def ecohelp(ctx):

    mensaje = (
        "🌍 **EcoEcho Bot - Comandos disponibles**\n\n"

        "🌱 `!tip`\n"
        "Muestra un consejo ecológico aleatorio.\n\n"

        "🌤️ `!clima`\n"
        "Consulta el clima configurado de la ciudad.\n\n"

        "📖 `!ecohelp`\n"
        "Muestra la lista de comandos disponibles.\n\n"

        "🤖 `!estado`\n"
        "Muestra el estado actual del bot.\n\n"

        "🇯🇵 `!mottainai`\n"
        "Explica la filosofía en que se basa el proyecto.\n\n"

    )

    await ctx.send(mensaje)


@bot.command(name="estado")
async def estado(ctx):

    cantidad_tips = len(tips_ecologicos)

    mensaje = (
        "🤖 **Estado de EcoEcho Bot**\n\n"

        f"🌱 Consejos ecológicos: {cantidad_tips}\n"

        f"📍 Ciudad configurada: {CIUDAD}\n"

        f"📢 Canal automático: #{CANAL_RECORDATORIOS}\n\n"

        "✅ Sistema funcionando correctamente."

    )

    await ctx.send(mensaje)


@bot.command(name="mottainai")
async def mottainai(ctx):
    mensaje = (
        "🌸 **Filosofía Mottainai**\n\n"

        "🇯🇵 Mottainai es una palabra japonesa que expresa el "
        "sentimiento de que es un desperdicio tirar o malgastar "
        "algo que todavía tiene valor.\n\n"

        "♻️ EcoEcho Bot utiliza esta filosofía para fomentar "
        "pequeños hábitos sostenibles, como ahorrar energía, "
        "cuidar el agua, reutilizar objetos y reducir residuos.\n\n"

        "💚 Cada pequeña acción cuenta cuando millones de personas "
        "la convierten en un hábito."
    )
    await ctx.send(mensaje)


bot.run(TOKEN)


```

## Aqui estan las iamgenes de el bot por si se las quieres colocar:


## Bot:
<img width="500" height="500" alt="LogoEcoEchoBot  MottainaiBot Definitivo" src="https://github.com/user-attachments/assets/3ebe7800-d92e-43e0-8c31-cdccc9b69190" />


# Imagen de el servidor:

<img width="500" height="500" alt="LogoEcoEchoBot  MottainaiBot sin background" src="https://github.com/user-attachments/assets/6e6cbd92-3d60-4bfb-8b7b-1c6de06f4ce7" />
