from telethon import events, functions, types
from utilities import client
from tagAll import tagAll
from tagAdmins import tagAdmins

# Get bot suggestions when typing "/"
async def set_bot_commands():
    await client(functions.bots.SetBotCommandsRequest(
        scope=types.BotCommandScopeDefault(),
        lang_code='ar',
        commands=[
            types.BotCommand(command='tagall', description='مناداة جميع الأعضاء'),
            types.BotCommand(command='admins', description='مناداة جميع المشرفين'),
            types.BotCommand(command='stop', description='إيقاف تشغيل البوت'),
        ]
    ))

# Check if there is no thrown exceptions
async def safe_reply(event, text, **kwargs):
    try:
        await event.reply(text, **kwargs)
    except Exception as e:
        print(f"⚠️ Failed to send message in chat {event.chat_id}: {e}")

# Check if the sender is an admin
async def is_admin(event):
    if event.is_private:
        return False
    try:
        user = await event.client.get_permissions(event.chat_id, event.sender_id)
        return user.is_admin
    except:
        return False

# Check if the bot itself is an admin
async def is_bot_admin(event):
    if event.is_private:
        return False
    try:
        me = await event.client.get_me()
        bot_perms = await event.client.get_permissions(event.chat_id, me.id)
        return bot_perms.is_admin
    except:
        return False

# Bot start handler
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await set_bot_commands()
    await event.respond("🤖 البوت جاهز! اكتب '/' لرؤية الأوامر.")

# Tag all members
@client.on(events.NewMessage(pattern=r"/(tagall|ناديلي_الفحلات)"))
async def handler(event):
    if not await is_bot_admin(event):
        await safe_reply(event, "🚫 لا يمكنني العمل لأنني لست مشرفاً في هذه المجموعة.")
        return
    if await is_admin(event):
        await tagAll(event)
    else:
        await event.reply("🚫 المشرفون فقط من يمكنهم استخدام هذا البوت")

# Tag admins
@client.on(events.NewMessage(pattern='/admins'))
async def handler_admins(event):
    if not await is_bot_admin(event):
        await safe_reply(event, "🚫 لا يمكنني العمل لأنني لست مشرفاً في هذه المجموعة.")
        return
    if await is_admin(event):
        await tagAdmins(event)
    else:
        await event.reply("🚫 المشرفون فقط من يمكنهم استخدام هذا البوت")

# Stop the bot
@client.on(events.NewMessage(pattern='/stop'))
async def handler_stop(event):
    if not await is_bot_admin(event):
        await safe_reply(event, "🚫 لا يمكنني العمل لأنني لست مشرفاً في هذه المجموعة.")
        return
    if await is_admin(event):
        await event.reply("🛑 تم إيقاف تشغيل البوت.")
        await client.disconnect()
    else:
        await event.reply("🚫 المشرفون فقط يمكنهم إيقاف تشغيل البوت")

# Start the bot
print("Bot is running...")
client.run_until_disconnected()
