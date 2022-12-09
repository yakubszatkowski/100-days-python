# age: int
# name: str
# height: float
# is_human: bool


def police_check(age: int) -> bool:  # input has to be int and output bool
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return "can_drive"  # hint here


if police_check('twelve'):  # hint here
    print('You may pass.')
else:
    print('Pay a fine.')

