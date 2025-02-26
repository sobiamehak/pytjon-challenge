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

user_input = int(input("Enter a number:") ) #user input
#conditons
if  user_input < 0: # ager number mynus hu to 
   print("You can not enter negative number.") # print
elif user_input == 1: # ager number 1 hu to
   print("1 is neither even nor odd. ") # print
    
elif user_input % 2 ==0: # ager number 2 sy devide krny k bad 0 ay to
    print(f"{user_input} is even number.") #print even
else: #werna
  print(f"{user_input} is odd number.")  #print odd

