from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
# from telebot import TeleBot, types
# from rest_framework.response import Response
#
# from config.settings import BOT_TOKEN
from dentic.models import BotUser

TELEGRAM_URL = "https://api.telegram.org/bot"
# bot = TeleBot(BOT_TOKEN)

#
# class BotView(APIView):
#     def post(self, request):
#         json_str = request.body.decode('UTF-8')
#         update = types.Update.de_json(json_str)
#         bot.process_new_updates([update])
#         return Response({'code': 200})
#
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     telegramuser = BotUser.objects.all().filter(user_telegram_id=message.from_user.id, register_status=True).first()
#     if not telegramuser:
#         text = """🇺🇿:Siz ro'yxatdan o'tmagansiz.🔒 \nIltimos ro'yxatdan o'tish uchun tasdiqlash kodini yuboring!🔑\n
# 🇷🇺: Вы не зарегистрированы.🔒 \nПожалуйста, отправьте код подтверждения для регистрации!🔑"""
#
#         bot.send_message(message.from_user.id, text=text)
