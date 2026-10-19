# WebSocket Chat

Django Channels asosida yozilgan oddiy real-time chat demo. Bir xil xona ichidagi foydalanuvchilarga xabarlar WebSocket orqali uzatiladi.

## Ishga tushirish

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Brauzerda `http://127.0.0.1:8000/chat/` manzilini oching. Ikki brauzer oynasida bir xil xona nomini kiritsangiz, xabarlar real-time ko‘rinadi.

## Production

Production muhitida quyidagi environment variable’larni belgilang:

```bash
DJANGO_SECRET_KEY=change-me
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=example.com
REDIS_URL=redis://127.0.0.1:6379/0
```

Redis production’da bir nechta worker ishlaganda channel layer sifatida kerak. Redis ko‘rsatilmasa, loyiha local demo uchun in-memory channel layer’dan foydalanadi.

## Test

```bash
python manage.py test
```

## License

MIT
