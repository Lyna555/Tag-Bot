async def safe_reply(event, text, **kwargs):
    try:
        await event.reply(text, **kwargs)
    except Exception as e:
        print(f"❌ safe_reply failed: {e}")
