import random

# Import daftar kata untuk dipilih dan tahapan seni hangman
from hangman_words import word_list
from hangman_arts import stages

# Jumlah nyawa yang dimiliki pemain
lives = 6

# Menampilkan sambutan kepada pemain
print("HELLO WELCOME TO HANGMAN GAME!")

# Memilih kata secara acak dari daftar kata
choosen_word = random.choice(word_list)

# Placeholder untuk menampilkan progres tebakan pemain (mulai dengan semua '_')
placeholder = ""
word_lengh = len(choosen_word)
for position in range(word_lengh):
    placeholder += "_"
print(placeholder)

# Inisialisasi status permainan
game_over = False
# Daftar huruf yang sudah ditebak dengan benar oleh pemain
correct_letters = []

# Loop utama permainan hingga selesai (game_over = True)
while not game_over:
    print(f"*********************** {lives}/6 LIVES LEFT ***********************")
    # Meminta pemain untuk menebak huruf
    guess = input("Guess a letter: ").lower()

    # Cek jika huruf sudah ditebak sebelumnya
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    # String baru untuk menampilkan progres kata yang ditebak
    display = ""

    # Iterasi melalui setiap huruf dalam kata yang dipilih
    for letter in choosen_word:
        if letter == guess:  # Jika huruf cocok dengan tebakan pemain
            display += letter
            correct_letters.append(guess)  # Tambahkan huruf ke daftar huruf yang benar
        elif letter in correct_letters:  # Jika huruf sudah ditebak sebelumnya
            display += letter
        else:  # Jika huruf belum ditebak
            display += "_"

    # Tampilkan progres kata ke pemain
    print("Words to guess: " + display)

    # Jika huruf yang ditebak tidak ada di kata, kurangi nyawa pemain
    if guess not in choosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life!")

        # Jika nyawa habis, pemain kalah
        if lives == 0:
            game_over = True
            print(f"*********************** IT WAS {choosen_word} YOU LOSE! ***********************")

    # Jika semua huruf sudah ditebak (tidak ada '_' dalam display), pemain menang
    if "_" not in display:
        game_over = True
        print("*********************** CONGRATS YOU WIN! ***********************")

    # Menampilkan tahap seni hangman sesuai dengan jumlah nyawa yang tersisa
    print(stages[lives])
