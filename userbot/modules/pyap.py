from userbot.events import register as r
from userbot.cmdhelp import CmdHelp as c
from telethon import events
import os

dosya_name=0
@r(outgoing=True, pattern="^.polu[sş]tur (.*) (.*) (edit|alt|foto|m[uü]zik)$")
async def _(q):
	global dosya_name
	if q.is_reply:
		mesaj = await q.get_reply_message()
		name = q.pattern_match.group(1)
		sleep_t = q.pattern_match.group(2)
		sec = q.pattern_match.group(3)

		if name == "":
			await q.edit("**Hey, Dostum Pluginin İçin Bir Komut Vermelisim!!**")
			return

		else:
			if sleep_t == "":
				await q.edit("**Hey, Dostum Pluginin Hızını Belirtmelisin!!**")
				return

			else:
				if sec == "":
					await q.edit("**Hey, Dostum Pluginin Nasıl Olmasını İstediğini Belirtmelisin!!**")
					return

				else:
					if sec.lower() == "edit":
						liste=[]
						m_split = mesaj.text.split("\n")
						for i in m_split:
							liste.append(i)
						dosya_name=dosya_name+1

						slep = sleep_t if sleep_t else 1.6
						import userbot.helpers.p as edit
						edit.e_(dosya_name, name, slep, liste)
						#file = await q.client.upload_file(f'./fg{dosya_name}.py')
						await q.client.send_file(q.chat_id, f"./fguserbot{dosya_name}.py", force_document=True, caption="Bu Plugin @FireqanqUserBot Tarafından Yapılmıştır..")
						await q.delete()
						os.remove(f"./fguserbot{dosya_name}.py")
						return

					if sec.lower() == "alt":
						liste=[]
						m_split = mesaj.text.split("\n")
						for i in m_split:
							liste.append(i)
						dosya_name=dosya_name+1

						slep = sleep_t if sleep_t else 1.6
						import userbot.helpers.p as edit
						edit.a_(dosya_name, name, liste, slep)
						#file = await q.client.upload_file(f'./fg{dosya_name}.py')
						await q.client.send_file(q.chat_id, f"./fguserbot{dosya_name}.py", force_document=True, caption="Bu Plugin @FireqanqUserBot Tarafından Yapılmıştır..")
						await q.delete()
						os.remove(f"./fguserbot{dosya_name}.py")
						return

					if sec.lower() =="foto":
						liste=[]
						m_split = mesaj.text.split("\n")
						for i in m_split:
							liste.append(i)
						dosya_name=dosya_name+1
						slep = sleep_t if sleep_t else 1.6
						import userbot.helpers.p as edit
						edit.r_(dosya_name, name, liste)
						await q.client.send_file(q.chat_id, f"./fguserbot{dosya_name}.py", force_document=True, caption="Bu Plugin @FireqanqUserBot Tarafından Yapılmıştır..")
						await q.delete()
						os.remove(f"./fguserbot{dosya_name}.py")
						return

					if sec.lower() in ["muzik", "müzik"]:
						liste=[]
						m_split = mesaj.text.split("\n")
						for i in m_split:
							liste.append(i)
						dosya_name=dosya_name+1
						import userbot.helpers.p as edit
						edit.m_(dosya_name, name, liste)
						await q.client.send_file(q.chat_id, f"./fguserbot{dosya_name}.py", force_document=True, caption="Bu Plugin @FireqanqUserBot Tarafından Yapılmıştır..")
						await q.delete()
						os.remove(f"./fguserbot{dosya_name}.py")
						return


					

					else:
						await q.edit("**Hey, Dostum Gecersiz Bir Metin Belirttin!!**")
						return



	else:
		await q.edit("**Hey, Dostum Bir Mesajı Yanıtlamalısın!!**")
		return

c_ = c("pyap")
c_.add_command("poluştur", "<pluginin_komutu> <plugin_hızı> <edit/alt/foto/muzik> ", "@FireqanqUserBot Sizin İçin Bir User Bot Oluşturur...")
c_.add()
