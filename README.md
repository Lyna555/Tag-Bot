# بوت التاغ التليجرام Tag-Bot
بوت تليجرام مبني باستخدام Telethon لمساعدة المشرفين في إدارة مجموعاتهم عن طريق تاغ الأعضاء بكفاءة.

## المميزات 
أوامر للمشرفين فقط:
  *  /ناديلي_الفحلات - تاغ جميع أعضاء المجموعة
  *  /admins - تاغ جميع مشرفي المجموعة
  *  /stop - إيقاف البوت
  
## نظام تاغ ذكي:
* استثناء البوتات تلقائياً
* تحديد معدل الرسائل (تأخير 2 ثانية بين المجموعات)
* تاغ بتنسيق HTML
* يدعم المستخدمين مع/بدون أسماء مستخدمين
## المتطلبات 📋
* بايثون 3.7+
* مكتبة Telethon
* بيانات اعتماد API تليجرام
* توكن البوت من @BotFather
## التنصيب 🛠️:
### 1. تنزيل المشروع
   ```
git clone https://github.com/yourusername/telegram-tag-bot.git
```
```
cd telegram-tag-bot
```

 ### 2. إعداد بيئة افتراضية

```
python -m venv venv
```
```
source venv/bin/activate  # في ويندوز استخدم: venv\Scripts\activate
```
4. تثبيت المتطلبات packages
pip install telethon python-dotenv
5. تهيئة البوت
احصل على بيانات اعتماد API من my.telegram.org BotFather
أنشئ ملف config.py وأضف بياناتك (من اجل حماية البيانات الحساسة):
API_ID = 'your_api_id'
API_HASH = 'your_api_hash'
BOT_TOKEN = 'your_bot_token'
6. تشغيل البوت
python main.py
المكونات الأساسية
1. main.py
from telethon import events
from utilities import client
from tagAll import tagAll
from tagAdmins import tagAdmins


async def is_admin(event):
    """التحقق من أن المرسل مشرف"""
    if event.is_private:
        return False
    user = await event.client.get_permissions(event.chat_id, event.sender_id)
    return user.is_admin


@client.on(events.NewMessage(pattern='/ناديلي_الفحلات'))
async def handle_tag_all(event):
    """معالجة أمر التاغ الجماعي"""
    if await is_admin(event):
        await tagAll(event)
    else:
        await event.reply("🚫 للمشرفين فقط!")
# ... other handlers ....

2. tagAdmins.py (المميزات الرئيسية)
جلب جميع مشرفي المجموعة باستخدام عامل التصفية ChannelParticipantsAdmins
تنسيق التاغ مع استخدام معرف المستخدم كبديل
تقسيم الرسائل لاحترام حد 4080 حرف في تليجرام
تطبيق تأخير 2 ثانية بين المجموعات
3. tagAll.py (المميزات الرئيسية)
المرور على جميع المشاركين في المجموعة
تخطي حسابات البوتات
التعامل مع مستخدمين مع/بدون أسماء مستخدمين
تجميع الرسائل لتجنب تجاوز الحد المسموح




كيفية الاستخدام 🚀
الأمر
الوصف
الصلاحيات
/ناديلي_الفحلات
تاغ جميع أعضاء المجموعة
المشرفون فقط
/admins
تاغ جميع مشرفي المجموعة
المشرفون فقط
/stop
ايقاف البوت
المشرفون فقط

الأمان 🔒
جميع الأوامر الحساسة مقصورة على المشرفين فقط
البوت يتحقق من صلاحية المشرف قبل تنفيذ أي أمر
 
