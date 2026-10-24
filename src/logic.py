import random
from mock_data import CLASS_DATA

def calculate_rating():
    """Считает рейтинг класса на основе оценок и посещаемости"""
    rating = []
    for name, stats in CLASS_DATA.items():
        # Простая формула: сумма оценок * 10 + посещаемость
        score = (stats["math"] + stats["russian"] + stats["physics"]) * 10 + stats["attendance"]
        rating.append((name, score))
    
    # Сортируем по убыванию баллов
    rating.sort(key=lambda x: x[1], reverse=True)
    return rating

def generate_motivation(name):
    """Генерирует персональную мотивашку (пока без ИИ, но по шаблону)"""
    if name not in CLASS_DATA:
        return f"{name}, привет! Начни учиться на отлично, и я помогу тебе!"
    
    stats = CLASS_DATA[name]
    
    # Логика выбора фразы в зависимости от успеваемости
    if stats["math"] >= 5:
        return f"🔥 {name}, ты просто маг математики! Так держать!"
    elif stats["attendance"] < 90:
        return f"👋 {name}, мы скучаем! Твоя посещаемость упала. Давай вернемся в строй?"
    elif stats["russian"] >= 5:
        return f"📚 {name}, твой русский великолепен! Продолжай в том же духе."
    else:
        phrases = [
            f"✨ {name}, сегодня отличный день, чтобы подтянуть физику!",
            f"🚀 {name}, каждая решенная задача делает тебя сильнее. Вперед!",
            f"💡 {name}, не бойся ошибок, они — путь к знаниям!"
        ]
        return random.choice(phrases)
