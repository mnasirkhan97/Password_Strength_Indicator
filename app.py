# # 01
# import re
# import random
# import string
# import streamlit as st
# import nltk
# import requests
# import hashlib
# import datetime

# # Download word list for passphrase generation
# nltk.download('words')
# from nltk.corpus import words

# # List of common weak passwords
# COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123", "password123", "admin", "iloveyou"]

# # Function to check password strength in real-time
# def check_password_strength(password):
#     score = 0
#     suggestions = []

#     # Check for common weak passwords
#     if password.lower() in COMMON_PASSWORDS:
#         return "❌ Very Weak - This password is too common!", ["Avoid using common passwords like 'password123' or '123456'."]

#     # Length Check
#     if len(password) >= 8:
#         score += 1
#     else:
#         suggestions.append("Password should be at least 8 characters long.")

#     # Upper & Lowercase Check
#     if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
#         score += 1
#     else:
#         suggestions.append("Include both uppercase and lowercase letters.")

#     # Digit Check
#     if re.search(r"\d", password):
#         score += 1
#     else:
#         suggestions.append("Add at least one number (0-9).")

#     # Special Character Check
#     if re.search(r"[!@#$%^&*]", password):
#         score += 1
#     else:
#         suggestions.append("Include at least one special character (!@#$%^&*).")

#     # Strength Rating
#     if score == 4:
#         return "✅ Strong Password!", []
#     elif score == 3:
#         return "⚠️ Moderate Password - Consider adding more security features.", suggestions
#     else:
#         return "❌ Weak Password - Improve it using the suggestions below:", suggestions

# # Function to generate a passphrase
# def generate_passphrase():
#     word_list = words.words()
#     chosen_words = random.sample(word_list, 3)  # Pick 3 random words
#     chosen_words = [word.capitalize() for word in chosen_words]  # Capitalize first letter
#     number = str(random.randint(10, 99))  # Add a random number
#     special_char = random.choice("!@#$%^&*")  # Add a special character
#     return "-".join(chosen_words) + number + special_char

# # Function to generate a random strong password
# def generate_strong_password(length=12):
#     characters = string.ascii_letters + string.digits + "!@#$%^&*"
#     return ''.join(random.choice(characters) for _ in range(length))

# # Function to check if password is in a data breach
# def check_password_breach(password):
#     sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
#     prefix, suffix = sha1_password[:5], sha1_password[5:]
#     url = f"https://api.pwnedpasswords.com/range/{prefix}"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         hashes = response.text.splitlines()
#         for line in hashes:
#             stored_hash, count = line.split(":")
#             if stored_hash == suffix:
#                 return f"⚠️ This password has been leaked {count} times! Choose a different one."
#     return "✅ No breaches found for this password."

# # Function to set password expiry reminder
# def check_password_expiry():
#     if "password_set_date" not in st.session_state:
#         st.session_state.password_set_date = datetime.date.today()

#     expiry_date = st.session_state.password_set_date + datetime.timedelta(days=90)
#     days_left = (expiry_date - datetime.date.today()).days

#     if days_left <= 0:
#         return "🔴 Your password has expired! Please update it immediately."
#     elif days_left <= 10:
#         return f"🟠 Your password will expire in {days_left} days. Consider updating it."
#     else:
#         return f"🟢 Password is safe. {days_left} days left before expiry."

# # Streamlit UI
# st.title("🔐 Password Strength Meter")

# password = st.text_input("Enter your password:", type="password", key="password_input")

# # Real-time password strength update
# if password:
#     strength, feedback = check_password_strength(password)
    
#     # Display password strength
#     st.markdown(f"### {strength}")
    
#     # Show progress bar based on score
#     score = sum(1 for _ in feedback)
#     progress = (4 - score) / 4  # Normalize to 0-1
#     st.progress(progress)

#     if feedback:
#         st.warning("Here are some improvements:")
#         for tip in feedback:
#             st.write(f"➡️ {tip}")

#     # Check for password breach
#     breach_status = check_password_breach(password)
#     if "⚠️" in breach_status:
#         st.error(breach_status)
#     else:
#         st.success(breach_status)

# # Password expiry reminder
# expiry_status = check_password_expiry()
# if "🔴" in expiry_status:
#     st.error(expiry_status)
# elif "🟠" in expiry_status:
#     st.warning(expiry_status)
# else:
#     st.success(expiry_status)

# # Sidebar for password generation
# st.sidebar.header("🔑 Generate a Password")
# length = st.sidebar.slider("Select Password Length", min_value=8, max_value=24, value=12)

# if st.sidebar.button("Generate Strong Password"):
#     strong_password = generate_strong_password(length)
#     st.sidebar.success(f"💡 Suggested Strong Password: `{strong_password}`")

# if st.sidebar.button("Generate Passphrase"):
#     passphrase = generate_passphrase()
#     st.sidebar.success(f"💡 Easy-to-Remember Passphrase: `{passphrase}`")


# 00
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
