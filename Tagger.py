import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

emoji_calisan = []

anlik_calisan = []

tekli_calisan = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**𝗠𝗲𝗿𝗵𝗮𝗯𝗮 ❤️**\n ● 𝗚𝗿𝘂𝗯𝘂𝗻𝘂𝘇𝗱𝗮𝗸𝗶 𝗡𝗲𝗿𝗱𝗲𝘆𝘀𝗲 𝘁𝘂‌𝗺 𝘂‌𝘆𝗲𝗹𝗲𝗿𝗲 𝗲𝘁𝗶𝗸𝗲𝘁 𝗮𝘁𝗮𝗯𝗶𝗹𝗶𝗿𝗶𝗺 𝗯𝗲𝗻𝗶 𝗴𝗿𝘂𝗯𝘂𝗻𝘂𝘇𝗮 𝗲𝗸𝗹𝗲𝘆𝗶𝗽 𝘆𝗲𝘁𝗸𝗶 𝘃𝗲𝗿𝗺𝗲𝗻𝗶𝘇 𝘆𝗲𝘁𝗲𝗿𝗹𝗶 . . . \n● 𝗞𝗼𝗺𝘂𝘁𝗹𝗮𝗿 𝗶𝗰𝗶𝗻  ➪  /help  𝘆𝗮𝘇𝗺𝗮𝗻𝗶𝘇 𝘆𝗲𝘁𝗲𝗿𝗹𝗶𝗱𝗶𝗿  . . .**",
                    buttons=(
                   
		      [Button.url('Beni Gruba Ekle ➕', 'https://t.me/StarTaggerBot?startgroup=a')],
                      [Button.url('Support🛠', 'https://t.me/BotDestekGrubu')],
                      [Button.url('Resmi Kanal📣', 'https://t.me/StarBotKanal')],
		      [Button.url('Developer👨🏻‍💻', 'https://t.me/ByWolk')],
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**🇹🇷 StarTaggerBot Komutları**\n\n**/tag <sebeb> - 5-li Etiket Atar**\n\n**/etag <sebeb> - Emoji ile etiketler**\n\n**/tektag sebeb - Üyeleri Tek Tek Etiketler**\n\n**/admins sebeb - Yöneticileri Tek Tek Etiketler**\n\n**/start - botu başlatır**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('Beni Gruba Ekle➕', 'https://t.me/StarTagBot?startgroup=a')],
                      [Button.url('Support👨‍💻', 'https://t.me/BotDestekGrubu')],
                      [Button.url('Resmi Kanal🔖', 'https://t.me/StarBotKanal')],
		      [Button.url('Developer🧑‍🔧', 'https://t.me/ByWolk')],
                    ),
                    link_preview=False
                   )
	
@client.on(events.NewMessage(pattern="^/reklam$"))
async def help(event):
  helptext = "**Çok özellikleri Etiket Botu Bulmaya Çalışan Grub Sahibleri @StarTaggerBot Size Göre:\n\n📌 5-li etiket\n📌 Emoji etiket\n📌 Tekli Etiket\n📌 Yalnız Yöneticileri etiketleme\n📌\n\n Böyle Çok özellikli @StarTagBot 'u grubunuza yönetici olarak ekleyip rahatlıkla üyelir , etiket ata bilirsiz **"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('Botu Gruba Ekle❤️', 'https://t.me/lucitaggerbot?startgroup=a')],
                    ),
                    link_preview=False
                   )
	
	

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)


emoji = " ❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🤩 🥳 😏 😒 " \
        "😞 😔 😟 😕 🙁 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡  🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 " \
        "😯 😦 😧 😮 😲 🥱 😴 🤤 😪 😵 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿 👹 👺 🤡  👻 💀 👽 👾 🤖 🎃 😺 😸 😹 " \
        "😻 😼 😽 🙀 😿 😾 🔞 🌹 ".split(" ")


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global emoji_calisan
  if event.is_private:
    return await event.respond("**Bu komutu gruplar ve kanallar için geçerli❗**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadace yoneticiler kullana bilir〽️**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Geçmiş mesajlar için etiket ede bilmiom**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Etiket Yapmak için sebeb yok❗️")
  else:
    return await event.respond("**Etikete Başlamak için sebeb yazın...!**")
  
  if mode == "text_on_cmd":
    emoji_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in emoji_calisan:
        await event.respond("** Etiketleme işlemi başarıyla durduruldu🤠**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    emoji_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in emoji_calisan:
        await event.respond("Işlem Başarıyla Durduruldu🤠\n\n**Buda sizin reklamınız ola bilir @StarMusicKanal**❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu komutu gruplar ve kanallar için geçerli❗️**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadace yoneticiler kullana bilir🤠**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajlara Cevab Vermeyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Başlatmak için sebeb yok😕")
  else:
    return await event.respond("Işleme başlamak için sebeb yok")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Işlem Başarıyla Durduruldu🤠\n\n**Buda sizin reklamınız ola bilir @StarMusicKanal**❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("işlem başarıyla durduruldu🤠")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu komutu gruplar ve kanallar için geçerli❗️**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadace yoneticiler kullana bilir〽**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**önceki mesajı etiketleye bilmerim*")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Başlamaq için Sebeb Yazın❗️")
  else:
    return await event.respond("**Işleme başlamağım için sebeb yazın..**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**👤 - [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Işlem Başarıyla Durduruldu\n\n**Buda sizin reklamınız ola bilir @StarBotKanal**❌****")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👤 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("Işlem Başarıyla Durduruldu🤠\n\n**Buda sizin reklamınız ola bilir @StarMusicKanal**❌**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	


@client.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def mentionall(tagadmin):

	if tagadmin.pattern_match.group(1):
		seasons = tagadmin.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tagadmin.get_input_chat()
	a_=0
	await tagadmin.delete()
	async for i in client.iter_participants(chat, filter=cp):
		if a_ == 500:
			break
		a_+=5
		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(0.5)


print(">> Bot çalışıyor sakin ol 😃 @StarBotKanal bilgi alabilirsin <<")
client.run_until_disconnected()
