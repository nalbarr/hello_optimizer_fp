def square(x):
    return x * x


def average(x, y):
    return (x + y) / 2.0


def improve(guess, x):
    return average(guess, (x / guess))


def good_enough(guess, x):
    if abs(square(guess) - x) < 0.001:
        return True
    else:
        return False


def new_if(predicate, then_clause, else_clause):
    if predicate:
        print("done")
        then_clause
    else:
        print("iterate")
        else_clause


def dump_guess(guess, x):
    print("*** good_enough: guess: {0}; x: {1}".format(guess, x))


def sqrt_iter(guess, x):
    print("guess: {0}; x: {1}".format(guess, x))
    """
    NA. Functional form not working?
    new_if(
        # evalute
        good_enough(guess, x),
        # guess
        guess,
        # iterate
        sqrt_iter(improve(guess, x), x),
    )
    """
    # NA. Imperative, conditional works
    if good_enough(guess, x):
        dump_guess(guess, x)
    else:
        sqrt_iter(improve(guess, x), x)


def square_root(x):
    sqrt_iter(1.0, x)


def main():
    square_root(9.0)


if __name__ == "__main__":
    main()
