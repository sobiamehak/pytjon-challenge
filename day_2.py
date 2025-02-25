# 📢 Day 2 – Daily Python Challenge 🐍 

# 🚀 Challenge: Aisa Python program likhna hai jo user se ek sentence le aur usme jitne words hain, count kare! 🔢💡  

# 🔥 Example:  
# 📌 Input: "Python is amazing!"  
# 📌 Output: Total words: 3  

# 💡 Hint: 
# - split() function ka use karke sentence ko words me tod sakte ho.  
# - len() function se words ki total count nikal sakte ho.  

#day 2
text = input("[Enter a sentence I will tell you the length of words and reserved your sentence] \n ") #user input
convert = text.split()  #convert sentence in words
reserved = convert[::-1]  # reserved sentence words
print(reserved) # to show in terminal reserved sentence
count = len(convert) #describe length of words
print(count)   # show length of words in terminal