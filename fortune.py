# fortune.py - Version 1.1

import random

name = "Bogi Maneesh Kumar"
admission_number = "21JE0244"

print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")

mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

fortunes = {
    "happy": [
        f"✨ Great things await you, {name}! Keep smiling. ✨",
        "🌟 Your joy will lead others today. Shine on!"
    ],
    "sad": [
        "🌧️ Tough times will pass. You're stronger than you know.",
        "💖 Something beautiful is on its way to heal your sadness."
    ],
    "neutral": [
        "🌀 Stay open—today holds a surprise!",
        "🌈 Calm days often bring the best ideas."
    ],
    "stressed": [
        f"💆 Breathe deep, {name}. You've got this.",
        "🍵 Take a break. A calm mind opens doors."
    ]
}

if mood in fortunes:
    print(random.choice(fortunes[mood]))
else:
    print("❓ Sorry, I can only read happy, sad, neutral, or stressed moods.")
