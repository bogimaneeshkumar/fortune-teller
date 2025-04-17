# fortune.py

# Personal Information
name = "Bogi Maneesh Kumar"
admission_number = "21JE0244"

# Welcome Message
print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")

# Get Mood Input
mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

# Display Fortune Based on Mood
if mood == "happy":
    print(f"✨ Your fortune: Great things await you, {name}! Keep smiling. ✨")
elif mood == "sad":
    print("🌧️ Your fortune: This too shall pass. Brighter days are ahead. 🌈")
elif mood == "neutral":
    print("🌀 Your fortune: Something exciting is just around the corner. Stay ready! 🔍")
else:
    print("❓ Sorry, I can't read your mood. Try happy, sad, or neutral.")
