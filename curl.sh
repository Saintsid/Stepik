#!/bin/bash

# Замените YOUR_BOT_TOKEN на ваш токен бота
BOT_TOKEN="6310440777:AAFJUxWtEfaepPry_i5bGjO3WRNEANwQkC4"

# Замените USER_CHAT_ID на chat_id пользователя, которому хотите отправить сообщение
USER_CHAT_ID="5064984299"

# Замените текст_сообщения на текст вашего сообщения
MESSAGE_TEXT="Любоффф моя"

# Отправка сообщения в Telegram через API бота
curl -X POST "https://api.telegram.org/bot6310440777:AAFJUxWtEfaepPry_i5bGjO3WRNEANwQkC4/sendMessage" \
     -H "Content-Type: application/json" \
     -d "{\"chat_id\": \"${USER_CHAT_ID}\", \"text\": \"${MESSAGE_TEXT}\"}"

curl -X POST "https://api.telegram.org/bot6310440777:AAFJUxWtEfaepPry_i5bGjO3WRNEANwQkC4/sendMessage" -H "Content-Type: application/json" -d '{"chat_id": "1047353629", "text": "${MESSAGE_TEXT}"}'
