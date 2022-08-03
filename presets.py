# ----------------------------------- https://github.com/m4mallu/gofilesbot ------------------------------------------ #

class Presets(object):
    CAPTION_TEXT_DOC = "\n\n<b>File Name:</b> {}\n\n<b>Format:</b> {}\n<b>Size:</b> {}"
    CAPTION_TEXT_VID = "\n\n<b>File Name:</b> {}\n\n<b>Size:</b> {}"
    ASK_PM_TEXT = "<b>Click the below button</b>"
    WELCOME_TEXT = "Hello.. <b>{}</b>\n<code>I can help you get Movies/Series from</code> @request_movies_series_tbm. " \
                   "<code>Just Keep this message live Here</code>😉\n\n" \
                   "<b> Please Save All The Files/Vedios To Cloud Or Forward To Friends And Delete Them From Bot. </b>\n"\
                   "<b> Or Simply On The Auto-Delete Timer (Set to 1 Day) </b>"
    CLEAN_CHAT_MSG = "⚠️ <b>Deleting all messages..</b>"
    MSG_FOR_PIN = "<b>For getting medias from here..</b>\n\n🔛 <code>Please start</code> @{} <code>in PM\n\n" \
                  "Send the exact Movie name.\n\n🔊 I'll reply the file in PM if available in our channel !</code>"

    BOT_PM_TEXT = "<b>Sorry.. 😢</b>\n\n<code>Bot won't work in PM, Ask in my Group. I'll reply the file in PM if " \
                  "available in our DB !</code>"
    PM_ERROR = "<b>Unable to send medias</b> ⛔️\n<code>Click the below button\nAsk here for movies later!</code>"
    MEDIA_SEND_TEXT = "<code>Media dispatched as PM 🥳</code>"
    NO_MEDIA = "Requested movie: <b>{}</b>\n\n<b>Not available " \
               "Right Now</b>\n<code>Possible Causes : 🤔\n\n⭕️ Not " \
               "released yet</code>\n⭕️ <a href='https://www.google.com/search?q={}'> Spelled incorrectly</a>\n" \
               "<code>⭕️ Unwanted texts in Msgs\n⭕ Asking theatre prints\n⭕ It Will Be Uploaded By The Admins. (Don't Spam)</code>"
    BLOCK_LIST = ['http://', 'https://', '@', '#', 'bit.ly', 't.me', '/', 'Uploaded']
