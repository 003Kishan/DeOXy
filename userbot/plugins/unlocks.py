# For The-TG-Bot v3
# By Priyam Kalra

import os
from PIL import Image


@borg.on(admin_cmd(func=lambda e: e.is_group))
async def watch(event):
    if str(event.chat_id) not in str(Config.UNLOCKED_CHATS):
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.sticker:
        reply = await event.get_reply_message()
        file = event.sticker
        file_name = "sticker.png"
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await client.download_media(
            file,
            downloaded_file_name
        )
        if os.path.exists(downloaded_file_name):
            image = Image.open(downloaded_file_name)
            sticker = image.resize((461, 499))
            sticker.save(file_name)
            await client.send_file(
                event.chat_id,
                file_name,
                force_document=False,
                supports_streaming=False,
                allow_cache=False,
                reply_to=reply,
            )
            os.remove(file_name)
            os.remove(downloaded_file_name)
