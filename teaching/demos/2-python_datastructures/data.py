# someData = (
#     {
#         'name': 'Bob',
#         'schools': ["GW", "UMD", "DuVal"],
#     },
#     ['hello', 'bob', {'name': 'Truman', }]
# )

# print someData[1][2]['name']

people = (
    {
        'id': 0,
        'name': 'Bob',
        'friends': [
            '1', '3', '5'
        ],
        'school': 'Coding Dojo',
    },
    {
        'id': 1,
        'name': 'Gary',
        'friends': [
            '1', '3', '5'
        ],
        'school': 'Coding Dojo',
    },
    {
        'id': 2,
        'name': 'Eve',
        'friends': [
            '1', '3', '5'
        ],
        'school': 'Coding Dojo',
    },
    {
        'id': 3,
        'name': 'Alice',
        'friends': [
            '1', '3', '5'
        ],
        'school': 'Coding Dojo',
    },
    {
        'id': 4,
        'name': 'Smith',
        'friends': [
            '1', '3', '5'
        ],
        'school': 'Coding Dojo',
    },
    {
        'id': 5,
        'name': 'Speros',
        'friends': [
            '1', '5'
        ],
        'school': 'Coding Dojo',
    },
)

# Print all of bob's friends' names
for friendIdx in people[0]['friends']:
    for i in range(len(people)):
        if int(friendIdx) == people[i]['id']:
            print people[i]['name']