# Password Generator
import string, random
print(" 4. Password Generator")
characters = (
    string.digits )


password =''.join(random.choice(characters) for _ in range(4))
print("Generated Password:", password)
