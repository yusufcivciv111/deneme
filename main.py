import discord
import random

# Botun ayrıcalıklarını tanımlayalım
intents = discord.Intents.default()
intents.message_content = True

# Bot oluşturalım ve ayrıcalıkları aktaralım
client = discord.Client(intents=intents)

# Plastik el işleri fikirleri içeren bir liste oluşturalım
plastik_el_isleri = [
    "Boş plastik şişeleri dekoratif vazolara dönüştürün.",
    "Plastik kaşıklarla birlikte rengarenk bir çiçek saksısı yapın.",
    "Eski plastik bardakları keyifli mumluklar haline getirin.",
    "Plastik atıkları kullanarak renkli bir duvar sanatı oluşturun.",
    "Plastik şişelerden şeffaf bir lamba gölgesi yapın.",
    "Eski plastik tabakları rengarenk birer masa altlığına dönüştürün."
]   "Boş plastik şişelerini çöpe atmak yerine süsleyip kalemlik haline getirin"
    "Boş plastikleri süsleyip  suluk olarak kullanın"
    "Eski plastikleri sertleştirerek mobilya yapın"
    "Plastikleri fabrikadan bazı işlemlerle geçirip kağıt haline getirerek ormanların yok olmasını engelleyin"
    "Plastikleri geri dönüştürüp yeni otomobil malzemeleri yapın"
    ""


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!plastik_el_isleri'):
        # Rastgele bir plastik el işi fikri seçelim
        fikir = random.choice(plastik_el_isleri)
        await message.channel.send(f"İşte bir plastik el işi fikri: {fikir}")

# Botu çalıştıralım
client.run("")
