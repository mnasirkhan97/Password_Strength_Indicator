import re
import random
import string
import streamlit as st
import nltk

# Download word list for passphrase generation
nltk.download('words')
from nltk.corpus import words

# List of common weak passwords
COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123", "password123", "admin", "iloveyou"]

# Function to check password strength in real-time
def check_password_strength(password):
    score = 0
    suggestions = []

    # Check for common weak passwords
    if password.lower() in COMMON_PASSWORDS:
        return "❌ Very Weak - This password is too common!", ["Avoid using common passwords like 'password123' or '123456'."]
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", []
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", suggestions
    else:
        return "❌ Weak Password - Improve it using the suggestions below:", suggestions

# Function to generate a passphrase
def generate_passphrase():
    word_list = words.words()
    chosen_words = random.sample(word_list, 3)  # Pick 3 random words
    chosen_words = [word.capitalize() for word in chosen_words]  # Capitalize first letter
    number = str(random.randint(10, 99))  # Add a random number
    special_char = random.choice("!@#$%^&*")  # Add a special character
    return "-".join(chosen_words) + number + special_char

# Function to generate a random strong password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password", key="password_input")

# Real-time password strength update
if password:
    strength, feedback = check_password_strength(password)
    
    # Display password strength
    st.markdown(f"### {strength}")
    
    # Show progress bar based on score
    score = sum(1 for _ in feedback)
    progress = (4 - score) / 4  # Normalize to 0-1
    st.progress(progress)

    if feedback:
        st.warning("Here are some improvements:")
        for tip in feedback:
            st.write(f"➡️ {tip}")

# Sidebar for password generation
st.sidebar.header("🔑 Generate a Password")
length = st.sidebar.slider("Select Password Length", min_value=8, max_value=24, value=12)

if st.sidebar.button("Generate Strong Password"):
    strong_password = generate_strong_password(length)
    st.sidebar.success(f"💡 Suggested Strong Password: `{strong_password}`")

if st.sidebar.button("Generate Passphrase"):
    passphrase = generate_passphrase()
    st.sidebar.success(f"💡 Easy-to-Remember Passphrase: `{passphrase}`")
