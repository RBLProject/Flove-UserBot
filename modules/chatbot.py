# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
✘ **Bantuan Untuk Chatbot**

๏ **Perintah:** `ai` <balas pesan/berikan pertanyaan>
◉ **Keterangan:** Sangat berguna untuk kebutuhan.
"""
import io
from io import *
import os
import requests
import openai
import shutil
from asyncio import gather
from telethon.errors import MessageNotModifiedError
from . import ayra_cmd


class OpenAi:
    def text(self, question):
        openai.api_key = udB.get_key("OPENAI_API")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Q: {question}\nA:",
            temperature=0,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return response.choices[0].text

    def photo(self, question):
        openai.api_key = udB.get_key("OPENAI_API")
        response = openai.Image.create(prompt=question, n=1, size="1024x1024")
        return response["data"][0]["url"]
        

@ayra_cmd(pattern="ai( (.*)|$)")
async def openai(event):
    question = event.pattern_match.group(2)
    if not question:
        await event.eor("`Mohon berikan pertanyaan untuk menggunakan AI.`")
        return
    msg = await event.eor("`Processing...`")
    try:
        response = OpenAi.text(question)
        await msg.edit(f"**Q:** {question}\n\n**A:** {response}")
    except Exception as e:
        await msg.edit(f"**Q:** {question}\n\n**A:** `Error: {e}`")
