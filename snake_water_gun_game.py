import random  # Importing random module to let computer choose randomly

# Intro message
print("🎮 Welcome to Snake 🐍 Water 💧 Gun 🔫 Game!")

print("📜 Rules:")

print(" - Snake drinks water 🐍 > 💧")

print(" - Gun kills snake 🔫 > 🐍")

print(" - Water drowns gun 💧 > 🔫")

print(" - Same choice = Draw 🤝")

print("--------------------------------------------------")


# Dictionary to define winning logic
# Each key is a (user, computer) tuple, and value is the winner



rules = {

    ('snake', 'water'): 'user',

    ('water', 'gun'): 'user',

    ('gun', 'snake'): 'user',

    ('water', 'snake'): 'computer',

    ('gun', 'water'): 'computer',

    ('snake', 'gun'): 'computer',
}



# List of valid choices
choices = ['snake', 'water', 'gun']



# 🧍 User input
user = input("🔸 Enter your choice (snake/water/gun): ").lower()



# ✅ Input validation
if user not in choices:
    print("❌ Invalid choice! Please choose only from: snake, water, or gun.")
else:
    # 🖥️ Computer randomly chooses
    computer = random.choice(choices)

    # 📊 Show both choices
    print("\n🔹 You chose:", user)

    print("🔹 Computer chose:", computer)

    # ⚖️ Game logic
    if user == computer:
        print("🔁 Result: It's a draw! 🤝")

    elif (user, computer) in rules:

        # Find the winner from the dictionary

        winner = rules[(user, computer)]

        if winner == 'user':
            print("✅ Result: You win! 🎉")

        else:
            print("💻 Result: Computer wins! 💥")


print("the game is ended....")




# The demo of this game 

# 🎮 Welcome to Snake 🐍 Water 💧 Gun 🔫 Game!
# 📜 Rules:
#  - Snake drinks water 🐍 > 💧
#  - Gun kills snake 🔫 > 🐍
#  - Water drowns gun 💧 > 🔫
#  - Same choice = Draw 🤝
# --------------------------------------------------
# 🔸 Enter your choice (snake/water/gun): snake

# 🔹 You chose: snake     
# 🔹 Computer chose: water
# ✅ Result: You win! 🎉   
# the game is ended....   
# PS C:\Users\shahz\OneDrive\Desktop\python basic\project_01snake,water,gun_game> 



# 🎮 Welcome to Snake 🐍 Water 💧 Gun 🔫 Game!
# 📜 Rules:
#  - Snake drinks water 🐍 > 💧
#  - Gun kills snake 🔫 > 🐍
#  - Water drowns gun 💧 > 🔫
#  - Same choice = Draw 🤝
# --------------------------------------------------
# 🔸 Enter your choice (snake/water/gun): water

# 🔹 You chose: water
# 🔹 Computer chose: snake
# 💻 Result: Computer wins! 💥
# the game is ended....
# PS C:\Users\shahz\OneDrive\Desktop\python basic\project_01snake,water,gun_game>




# 🎮 Welcome to Snake 🐍 Water 💧 Gun 🔫 Game!
# 📜 Rules:
#  - Snake drinks water 🐍 > 💧
#  - Gun kills snake 🔫 > 🐍
#  - Water drowns gun 💧 > 🔫
#  - Same choice = Draw 🤝
# --------------------------------------------------
# 🔸 Enter your choice (snake/water/gun): gun

# 🔹 You chose: gun
# 🔹 Computer chose: water
# 💻 Result: Computer wins! 💥
# the game is ended....
# PS C:\Users\shahz\OneDrive\Desktop\python basic\project_01snake,water,gun_game>