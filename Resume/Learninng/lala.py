# amount of times the STR will appear
"hello".count("e")

# x.lower() method shows how the STR look like in lower(same to upper) case. Output: "happy birthday"
x = "Happy Birthday"
x.lower()
# The STR are inmutable data type. So u cant change it unless overwrite or delete. Output:"happy birthday"
x = x.lower()
# x.capitalize(only one letter in first word in sentence) and x.title are making the first letter in the word uppercassive
x.capitalize()
x.title()

# Output:"False" Because space is not a letter.
x = "Happy Birthday"
x.isalpha()
# !  is not a letter or a number
y = "happybirthday!123"
y.isalnum()

# .lower(), .upper(), ,title(), .capitalize()
# .islower(), .isupper(),.isalalpha(), .isalnum()

# index is a place in str, count starts from 0
x.index("birthday")
x.find("birthday")


# to get rid of spaces in STR use .strip().
y.strip()
y.strip("0")

# word[5:1:2] First is where you start from in the str, second number is where you might go up to, third number is a step.
# Here is some examples with output from console.
# word = "supercalifragilisticeexpialidocious"
# word[0]
# 's'
# word[2]
# 'p'
# word[0:5:1]
# 'super'
# word[4:9:1]
# 'rcali'
# word[5:9:1]
# 'cali'
# word[5:]
# 'califragilisticeexpialidocious'
# word[5::2]
# 'clfaiitcepaioiu'
# word[:7]
# 'superca'
# word[:8]
# 'supercal'
# word[::-1]
# 'suoicodilaipxeecitsiligarfilacrepus'