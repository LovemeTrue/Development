dict = {
    'а' : 'a',
    'б' : 'b',
    'в' : 'v',
    'г' : 'g',
    'д' : 'd',
    'е' : 'e',
    'ё' : 'yo',
    'ж' : 'zh',
    'з' : 'z',
    'и' : 'i',
    'й' : 'y',
    'к' : 'k',
    'л' : 'l',
    'м' : 'm',
    'н' : 'n',
    'о' : 'o',
    'п' : 'p',
    'р' : 'r',
    'с' : 's',
    'т' : 't',
    'у' : 'u',
    'ф' : 'f',
    'х' : 'h',
    'ц' : 'c',
    'ч' : 'ch',
    'ш' : 'sh',
    'щ' : 'sch',
    'ъ' : '',
    'ы' : 'bI',
    'ь' : "'",
    'э' : 'e',
    'ю' : 'u',
    'я' : 'ya'
}
new = ''
text = input("Text: ").lower().strip()
for letters in text:
    if letters in dict:
        new = new + dict[letters]
    else:
        new = new + letters
print(new)