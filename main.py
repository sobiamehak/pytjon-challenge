# 📢 Day 3 – Daily Python Challenge 🐍
# 🚀 Challenge: Aisa Python program likho jo user se ek number le aur check kare ke wo prime number hai ya nahi! 🔢💡

# 🔥 Example:
# 📌 Input: 7
# 📌 Output: Yes, it's a prime number!
# 📌 Input: 10
# 📌 Output: No, it's not a prime number!

# 🔥 Think you can do it? Let’s go! 💪🚀
# 💡Hint:
# ⿡ Prime Number wo hota hai jo sirf 1 aur apne aap se divisible ho.
# ⿢ Tum loops (for/while) aur modulus operator (%) ka use kar sakte ho.
# ⿣ Edge Cases: 1 aur negative numbers prime nahi hote!

# Function to check if the number is prime
def is_prime(number):
    # Edge case: 1 and negative numbers are not prime
    if number <= 1:
        return False
    
    # Check divisibility from 2 to square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    # If no divisors are found, the number is prime
    return True

# Taking input from the user
num = int(input("Enter a number: "))

# Checking if the number is prime or not
if is_prime(num):
    print(f"Yes, {num} is a prime number!")
else:
    print(f"No, {num} is not a prime number!")



