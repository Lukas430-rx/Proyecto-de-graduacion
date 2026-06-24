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
            "Aprovecha la energía solar para calentar tu hogar o."
            "O ponte ropa abrigada antes de encender calefaccion."
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

bot.run(TOKEN)
