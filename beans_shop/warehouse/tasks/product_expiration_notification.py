import logging
from datetime import timedelta

from celery import Task
from asgiref.sync import async_to_sync
from telegram import Bot
import telebot
from django.utils import timezone
from django.conf import settings

from beans_shop.warehouse.models import Product, WarehouseSettings
from config.celery_app import app

logger = logging.getLogger(__name__)


class ProductExpirationNotificationTask(Task):
    def run(self, *args, **kwargs) -> dict:
        notification_expiration_days = WarehouseSettings.get_solo().notification_expiration_days
        exp_date = timezone.now() + timedelta(days=notification_expiration_days)
        exp_products = Product.objects.filter(expiration_dt__lte=exp_date)

        if exp_products:
            # bot = Bot(settings.TELEGRAM_BOT_TOKEN)
            tb = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)
            #logger.info(f"[{self.__class__.__name__}] Bot.me {bot.get_me()}")
            for product in exp_products:
                text = f"{product.name} - {product.expiration_dt.strftime('%d %b, %Y')}"
                tb.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=text)
                # async_to_sync(bot.send_message(text=f"{product.name} - {product.expiration_dt.strftime('%d %b, %Y')}", chat_id=settings.TELEGRAM_CHAT_ID))


ProductExpirationNotificationTask = app.register_task(ProductExpirationNotificationTask())
