from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Разрешаем сайту обращаться к локальному скрипту

TOKEN = "8669690935:AAHUxZPeBW8eQBzoCWETkQioMy9eocI1DbU"
CHAT_ID = "1137512652"

@app.route('/send_anketa', methods=['POST'])
def send_anketa():
    try:
        # Получаем данные из формы
        data = request.form
        
        text = (
            f"🚀 **НОВАЯ АНКЕТА ОХОТНИКА**\n\n"
            f"👤 Имя: {data.get('userName', '—')}\n"
            f"📅 ДР: {data.get('birthDate', '—')}\n"
            f"✈️ ТГ: {data.get('telegram', '—')}\n"
            f"🎮 Ник: {data.get('minecraftNick', '—')}\n"
            f"💻 Платформа: {data.get('platform', '—')}\n"
            f"🔍 Откуда: {data.get('source', '—')}\n"
            f"🏠 Другие проекты: {data.get('otherHouses', '—')}\n"
            f"📝 О себе: {data.get('extraInfo', '—')}"
        )

        # Отправка в Telegram
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        response = requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": text
        })

        if response.status_code == 200:
            print("✅ Сообщение отправлено в Telegram!")
            return "success"
        else:
            print(f"❌ Ошибка Telegram: {response.text}")
            return f"Error TG: {response.status_code}"

    except Exception as e:
        print(f"🔥 Критическая ошибка: {e}")
        return str(e)

if __name__ == '__main__':
    print("🤖 Сервер запущен на http://127.0.0.1:5000")
    app.run(port=5000)