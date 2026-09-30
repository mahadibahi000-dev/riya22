import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters

# লগিং সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start কমান্ড দিলে বট যা বলবে
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_text = (
        f"হ্যালো {user_name}! 🌸 আমি আপনার মজার ফ্রেন্ড বট।\n\n"
        "✨ বিশেষ শব্দগুলো লিখে ট্রাই করুন:\n"
        "• 'হাই' লিখলে ভয়েস শুনবেন\n"
        "• 'riya' লিখলে ভয়েস শুনবেন\n"
        "• 'হ্যালো' লিখলে ভয়েস শুনবেন\n"
        "• 'মাহাদী আমার জামাই' লিখলে মজার ভয়েস শুনবেন!\n"
        "• এছাড়া /joke লিখে জোকস শুনতে পারেন।"
    )
    await update.message.reply_text(welcome_text)

# মজার জোকস কমান্ড
async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jokes_list = [
        "শিক্ষক: বলতো পল্টু, মশা আমাদের কামড়ায় কেন?\nপল্টু: স্যার, রাগ থেকে! কারণ আমরা তো ওদের গান শুনলেই তালি দিই তো তাই! 🦟😂",
        "বল্টু: দোস্ত, আমার গার্লফ্রেন্ড আমাকে ব্লক করে দিছে!\nমন্টু: তো কি হয়েছে? নতুন একটা পটিয়ে নে!\nবল্টু: না মানে, ওর ঘরের ওয়াইফাইয়ের পাসওয়ার্ডটাও তো ব্লক হয়ে গেছে! 📶😭"
    ]
    selected_joke = random.choice(jokes_list)
    await update.message.reply_text(selected_joke)

# সাধারণ মেসেজ, বিশেষ শব্দ এবং ভয়েস হ্যান্ডলার
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()
    
    # ১. "হাই" লিখলে ভয়েস দিবে
    if "হাই" in text or "hi" in text:
        await update.message.reply_text("হ্যালো! আপনার জন্য একটা ভয়েস মেসেজ রইল 👇")
        try:
            await update.message.reply_voice(voice=open('hi_voice.ogg', 'rb'))
        except FileNotFoundError:
            await update.message.reply_text("(ফোল্ডারে hi_voice.ogg ফাইলটি পাওয়া যায়নি!)")

    # ২. "riya" লিখলে ভয়েস দিবে
    elif "riya" in text:
        await update.message.reply_text("রিয়াকে নিয়ে স্পেশাল ভয়েস মেসেজ! 🎵")
        try:
            await update.message.reply_voice(voice=open('riya_voice.ogg', 'rb'))
        except FileNotFoundError:
            await update.message.reply_text("(ফোল্ডারে riya_voice.ogg ফাইলটি পাওয়া যায়নি!)")

    # ৩. "হ্যালো" লিখলে ভয়েস দিবে
    elif "হ্যালো" in text or "hello" in text:
        await update.message.reply_text("নমস্কার/হ্যালো! শুনুন আমার গলায় ভয়েস... 🎙️")
        try:
            await update.message.reply_voice(voice=open('hello_voice.ogg', 'rb'))
        except FileNotFoundError:
            await update.message.reply_text("(ফোল্ডারে hello_voice.ogg ফাইলটি পাওয়া যায়নি!)")

    # ৪. "মাহাদী আমার জামাই" লিখলে ভয়েস দিবে
    elif "মাহাদী আমার জামাই" in text:
        await update.message.reply_text("হা হা! দারুন কথা বলেছেন! শুনুন তবে ভয়েসটা 😂👇")
        try:
            await update.message.reply_voice(voice=open('mahadi_voice.ogg', 'rb'))
        except FileNotFoundError:
            await update.message.reply_text("(ফোল্ডারে mahadi_voice.ogg ফাইলটি পাওয়া যায়নি!)")

    # ৫. সাধারণ 'I love you' বা অন্যান্য কথা
    elif "i love you" in text or "ভালোবাসি" in text:
        await update.message.reply_text("I love you too, friend! 🥰✨ সবসময় এভাবেই পাশে থেকো।")
    elif "কেমন আছো" in text or "kemon acho" in text:
        await update.message.reply_text("আমি তো দারুণ আছি! 😊")
    else:
        await update.message.reply_text("কথাটি বুঝলাম না! তবে আপনি 'হাই', 'হ্যালো', 'riya' অথবা 'মাহাদী আমার জামাই' লিখে ট্রাই করতে পারেন! 🤭")

if __name__ == '__main__':
    TOKEN = "8827926597:AAFUpNr4tqcatCbSi6GydXPF8AC6CzXkGtU"
    
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("joke", joke))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("বট সফলভাবে রান হয়েছে! 🚀")
    app.run_polling()