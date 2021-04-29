def new_pass():
    from random import choice, randint
    elements = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890'
    password = ''

    for l in range(randint(8, 11)):
        password += choice(elements)

    return password