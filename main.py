# ============================================================
# TOSHKENTOVUZ BOT - VERCEL SERVERLESS FUNCTION
# Python + Flask + Vercel
# ============================================================

import os
import json
import requests
from datetime import datetime
from flask import Flask, request, jsonify

# ============================================================
# SOZLAMALAR - VERCEL ENVIRONMENT VARIABLES
# ============================================================

BOT_TOKEN = os.environ.get('BOT_TOKEN', '8977983857:AAF-70QjNlpJchJ02O2pEGCPi11tTBTYy74')
WEBHOOK_URL = os.environ.get('WEBHOOK_URL', 'https://your-app.vercel.app/api/webhook')
CHAT_ID = os.environ.get('CHAT_ID', '8958302600')

app = Flask(__name__)

# ============================================================
# TELEGRAM API
# ============================================================

TELEGRAM_API = f'https://api.telegram.org/bot{BOT_TOKEN}'

def send_telegram_message(chat_id, text, parse_mode='HTML'):
    try:
        url = f'{TELEGRAM_API}/sendMessage'
        payload = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': parse_mode,
            'disable_web_page_preview': True
        }
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        print(f'Telegram xatosi: {e}')
        return None

# ============================================================
# WEBHOOK ENDPOINT
# ============================================================

@app.route('/api/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        print(f'Webhook ma\'lumot: {data}')
        
        if not data:
            return jsonify({'status': 'error', 'message': 'No data'}), 400
        
        event = data.get('event', 'unknown')
        time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        message = f'🚀 <b>TOSHKENTOVUZ</b>\n'
        message += f'📌 <b>Voqea:</b> {event}\n'
        message += f'🕐 <b>Vaqt:</b> {time_str}\n'
        message += f'⚡ <b>Vercel:</b> 100%\n'
        
        if event == 'item_click':
            message += f'📂 <b>Dastur:</b> {data.get("item", "Noma\'lum")}\n'
            message += f'📋 <b>Ma\'lumot:</b> {data.get("sub", "Noma\'lum")}\n'
        elif event == 'search':
            message += f'🔍 <b>Qidiruv:</b> {data.get("query", "Noma\'lum")}\n'
        elif event == 'contact':
            message += f'👤 <b>Ism:</b> {data.get("name", "Noma\'lum")}\n'
            message += f'📝 <b>Xabar:</b> {data.get("message", "Noma\'lum")}\n'
        elif event == 'webhook_test':
            message += f'🧪 <b>Webhook test</b>\n'
        
        message += f'\n🤖 <b>Bot:</b> @ToshkentovuzBot'
        
        result = send_telegram_message(CHAT_ID, message)
        
        return jsonify({
            'status': 'success',
            'event': event,
            'timestamp': time_str,
            'telegram': result
        }), 200
        
    except Exception as e:
        print(f'Webhook xatosi: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500

# ============================================================
# TELEGRAM BOT WEBHOOK
# ============================================================

@app.route('/api/telegram', methods=['POST'])
def telegram_webhook():
    try:
        update = request.get_json()
        print(f'Telegram update: {update}')
        
        if 'message' in update:
            message = update['message']
            chat_id = message['chat']['id']
            text = message.get('text', '')
            
            if text == '/start':
                response = (
                    '🚀 <b>TOSHKENTOVUZ BOT</b>\n\n'
                    '🌐 Dunyodagi eng kuchli portal!\n'
                    '🤖 AI tomonidan boshqariladi\n'
                    '⚡ Vercel 100% ulangan!\n\n'
                    '📋 <b>Mavjud komandalar:</b>\n'
                    '/start - Botni ishga tushirish\n'
                    '/help - Yordam\n'
                    '/info - Ma\'lumot\n'
                    '/status - Holat\n\n'
                    '🌐 Sayt: https://toshkentov.uz'
                )
                send_telegram_message(chat_id, response)
            elif text == '/help':
                response = '📋 <b>Yordam</b>\n\n/start - Botni ishga tushirish\n/help - Yordam\n/info - Ma\'lumot\n/status - Holat'
                send_telegram_message(chat_id, response)
            elif text == '/info':
                response = (
                    '📊 <b>TOSHKENTOVUZ</b>\n\n'
                    '🛡️ 100% XAVFSIZ\n'
                    '⚡ VERCEL 100% ULANGAN\n'
                    '🤖 AI BOSHQARUV\n\n'
                    '📊 1000+ TUGMA\n'
                    '🌐 10000+ SAYT\n'
                    '⚡ 24/7 ISHLASH\n\n'
                    '🌐 Sayt: https://toshkentov.uz'
                )
                send_telegram_message(chat_id, response)
            elif text == '/status':
                response = (
                    '📊 <b>Holat</b>\n\n'
                    '✅ Bot: Ishlaydi\n'
                    '⚡ Vercel: 100% Faol\n'
                    '🛡️ Xavfsizlik: 100%\n'
                    '🤖 AI: Aktiv\n'
                    f'🕐 {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
                )
                send_telegram_message(chat_id, response)
            else:
                response = (
                    '🤖 <b>TOSHKENTOVUZ AI</b>\n\n'
                    '📝 Xabaringiz qabul qilindi!\n'
                    '⚡ Vercel 100% orqali uzatildi.\n\n'
                    '📋 Yordam uchun /help'
                )
                send_telegram_message(chat_id, response)
        
        return jsonify({'status': 'ok'}), 200
        
    except Exception as e:
        print(f'Telegram webhook xatosi: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500

# ============================================================
# SET WEBHOOK
# ============================================================

@app.route('/api/setwebhook', methods=['GET'])
def set_webhook():
    try:
        webhook_url = f'{WEBHOOK_URL}/api/telegram'
        url = f'{TELEGRAM_API}/setWebhook'
        payload = {'url': webhook_url, 'allowed_updates': ['message']}
        response = requests.post(url, json=payload)
        return jsonify({
            'status': 'success',
            'webhook_url': webhook_url,
            'response': response.json()
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# ============================================================
# HEALTH CHECK
# ============================================================

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'bot': 'TOSHKENTOVUZ',
        'version': '3.0',
        'platform': 'Vercel',
        'timestamp': datetime.now().isoformat()
    })

# ============================================================
# ROOT
# ============================================================

@app.route('/api', methods=['GET'])
def index():
    return jsonify({
        'name': 'TOSHKENTOVUZ Bot',
        'version': '3.0',
        'status': 'running',
        'platform': 'Vercel',
        'endpoints': [
            '/api/webhook - POST',
            '/api/telegram - POST',
            '/api/setwebhook - GET',
            '/api/health - GET'
        ]
    })

# ============================================================
# FOR VERCEL SERVERLESS
# ============================================================

# Vercel uchun handler
def handler(request, context):
    return app(request, context)