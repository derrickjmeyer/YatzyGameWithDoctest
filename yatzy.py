


def chance(dice):
    """Score the given role in the 'Chance' Yatzy category

    >>> chance([5,5,5,5,5])
    25
    >>> chance([1,2,3,4,5])
    15
    """
    return sum(dice)

def small_straight(dice):
    """Score the given roll in the 'small straight' yatzy category.

    >>> small_straight([1,2,3,4,5])
    15
    >>> small_straight([1,2,3,5,5])
    0

    It also accepts sets, or unsorted lists

    >>> small_straight({1,2,3,4,5})
    15
    >>> small_straight([1,2,3,5,4])
    15
    """
    if sorted(dice) == [1, 2, 3, 4, 5]:
        return sum(dice)
    return 0


def four_of_a_kind(dice):
    """Score the given roll in the 'Four of a kind' category

    >>> four_of_a_kind([1,6,6,6,6])
    24
    >>> four_of_a_kind([1,1,6,6,6])
    0
    """
    counts = dice_counts(dice)
    for i in [6, 5, 4, 3, 2, 1]:
        if counts[i] >= 4:
            return 4*i
    return 0

def ones(dice):
    """Score the given roll in the 'Ones' category

    >>> ones([1,1,3,4,5])
    2
    >>> ones([3,4,5,6,6])
    0
    """
    return dice_counts(dice)[1]

def twos(dice):
    """Score the given roll in the 'Twos' category

    >>> twos([2,2,3,4,5])
    4
    >>> twos([3,4,5,1,6,6])
    0
    """
    return dice_counts(dice)[2]

def threes(dice):
    """Score the given roll in the 'Threes' category

    >>> threes([3,3,4,5,6])
    6
    >>> threes([1,2,4,5,6])
    """
    return dice_counts(dice)[3]

def fours(dice):
    """Score the given roll in the 'fours' category

    >>> fours([4,4,5,6,1])

    >>> fours([1,2,3,5,6])
    """
    return dice_counts(dice)[4]

def fives(dice):
    """Score the given roll in the 'fives' category

    >>> fives([5,5,6,4,3])

    >>> fives([1,2,3,4,5])
    """
    return dice_counts(dice)[5]
