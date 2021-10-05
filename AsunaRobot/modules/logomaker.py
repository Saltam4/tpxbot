from AsunaRobot.events import register
from AsunaRobot import OWNER_ID
from AsunaRobot import telethn as tbot
import os
from PIL import Image, ImageDraw, ImageFont


@register(pattern="^/logo ?(.*)")
async def lego(event):
    quew = event.pattern_match.group(1)
    if event.sender_id == OWNER_ID:
        pass
    else:

        if not quew:
            await event.reply("Provide Some Text To Draw!")
            return
        else:
            pass
    await event.reply("Creating your logo! Hold on...")
    try:
        text = event.pattern_match.group(1)
        img = Image.open("./AsunaRobot/resources/BG01.jpg")
        draw = ImageDraw.Draw(img)
        image_widthz, image_heightz = img.size
        pointsize = 500
        fillcolor = "gold"
        shadowcolor = "blue"
        font = ImageFont.truetype("./AsunaRobot/resources/Bigparty2-green.ttf", 150)
        w, h = draw.textsize(text, font=font)
        h += int(h * 0.21)
        image_width, image_height = img.size
        draw.text(
            ((image_widthz - w) / 2, (image_heightz - h) / 2),
            text,
            font=font,
            fill=rgba(0, 0, 0, 1),
        )
        x = (image_widthz - w) / 2
        y = (image_heightz - h) / 2 + 6
        draw.text(
            (x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="yellow"
        )
        fname2 = "LogoByOppaiiRobot.png"
        img.save(fname2, "png")
        await tbot.send_file(event.chat_id, fname2, caption="Made By @OppaiiRobot")
        if os.path.exists(fname2):
            os.remove(fname2)
    except Exception as e:
        await event.reply(f"Report to @SAlTAM4, {e}")


@register(pattern="^/wlogo ?(.*)")
async def lego(event):
    quew = event.pattern_match.group(1)
    if event.sender_id == OWNER_ID:
        pass
    else:

        if not quew:
            await event.reply("Provide Some Text To Draw!")
            return
        else:
            pass
    await event.reply("Creating your logo! Hold on...")
    try:
        text = event.pattern_match.group(1)
        img = Image.open("./AsunaRobot/resources/asuna-logo-gen.jpg")
        draw = ImageDraw.Draw(img)
        image_widthz, image_heightz = img.size
        pointsize = 500
        fillcolor = "white"
        shadowcolor = "blue"
        font = ImageFont.truetype("./AsunaRobot/resources/Maghrib.ttf", 1000)
        w, h = draw.textsize(text, font=font)
        h += int(h * 0.21)
        image_width, image_height = img.size
        draw.text(
            ((image_widthz - w) / 2, (image_heightz - h) / 2),
            text,
            font=font,
            fill=(255, 255, 255),
        )
        x = (image_widthz - w) / 2
        y = (image_heightz - h) / 2 + 6
        draw.text(
            (x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="white"
        )
        fname2 = "LogoByOppaiiRobot.png"
        img.save(fname2, "png")
        await tbot.send_file(event.chat_id, fname2, caption="Made By @OppaiiRobot")
        if os.path.exists(fname2):
            os.remove(fname2)
    except Exception as e:
        await event.reply(f"Report to @SAlTAM4, {e}")


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


__help__ = """
 ❍ /logo text :  Create your logo with your name

 """
__mod_name__ = "Logo"