dic = [
    {
        "name": "12",
        "age": "4",
        "phone": "399883"
    },
    {
        "name": "Мотаро",
        "age": "323",
        "phone": "99442334"
    },
    {
        "name": "Милена",
        "age": "1111",
        "phone": "33223"
    },
    {
        "name": "Челиос",
        "age": "9329",
        "phone": "2131311"
    },
    {
        "name": "12",
        "age": "4",
        "phone": "399883"
    },
    {
        "name": "1343",
        "age": "5",
        "phone": "399881"
    },
    {
        "name": "r4r3",
        "age": "6",
        "phone": "399882"
    },
    {
        "name": "miracle",
        "age": "7",
        "phone": "399884"
    },
    {
        "name": "Xh",
        "age": "8",
        "phone": "399885"
    },
    {
        "name": "Brain",
        "age": "111",
        "phone": "39973"
    },
    {
        "name": "Wisdom",
        "age": "10",
        "phone": "399881233231"
    },
    {
        "name": "Dick",
        "age": "99",
        "phone": "123"
    },
]

def search(name,age,phone):
    for dicts in dic:
        if dicts['name'] == name:
            return dicts
        if dicts['age'] == age:
            return dicts
        if dicts['phone'] == phone:
            return dicts