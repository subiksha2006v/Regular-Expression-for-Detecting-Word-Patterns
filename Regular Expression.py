import re

# Input text
text = "Data science and machine learning are important in AI applications"

# 1. Detect a single word
pattern1 = r"AI"
match1 = re.findall(pattern1, text)
print("Single word detected:", match1)

# 2. Detect words starting with 'ma'
pattern2 = r"\bma\w*"
match2 = re.findall(pattern2, text)
print("Words starting with 'ma':", match2)

# 3. Detect words ending with 'ing'
pattern3 = r"\b\w+ing\b"
match3 = re.findall(pattern3, text)
print("Words ending with 'ing':", match3)

# 4. Detect words with exactly 4 letters
pattern4 = r"\b\w{4}\b"
match4 = re.findall(pattern4, text)
print("Four-letter words:", match4)

# 5. Detect capitalized words
pattern5 = r"\b[A-Z][a-z]*\b"
match5 = re.findall(pattern5, text)
print("Capitalized words:", match5)

