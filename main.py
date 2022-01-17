epochs_init = 0  # initial epoch iteration
step_dir_init = 1.0  # initial step dir
x_init = 151.0  # initial y guess
n_epochs = 100  # number of iterations for algorithm
alpha = 0.01  # learning rate
y_min_threshold = 0.00001  # early y_min threshold

# given
def f(x):
    """
    - original polynomial expression:
    10 * (x-2)**2 + 7
    """
    """
    - simplify so we can derive gradient later
    10 * (x**2 - (4*x)- 4) + 7
    (10 * x**2) - (40 * x) - 40 + 7
    (10 * x**2) - (40 * x) - 47
    """
    return 10.0 * (x - 2.0) ** 2.0 + 7.0


def dump_epoch(y_last, y_new, x_new, epoch):
    def x_step_str(y_last, y_new):
        if y_new < y_last:
            return "left"
        elif y_new > y_last:
            return "right"

    print(
        "epoch: {0}, y_last: {1}, y_new: {2}, y_new < y_last: {3}, step_dir: {4}, x_step: {5}".format(
            epoch, y_last, y_new, (y_new < y_last), x_step_str(y_last, y_new), x_new
        )
    )


def x_step(x):
    x_new = x - (alpha * gradient(x))
    return x_new


def y_min_reached(y_last, y_new, x_new, epoch):
    if abs(y_last - y_new) <= y_min_threshold:
        print(
            "*** y_min found early epoch {0} for: y_new: {1}, x_new: {2}".format(
                epoch, y_new, x_new
            )
        )
        return True
    else:
        return False


# solve, implement
def find_min(f, x, step_dir, epoch):
    """
    - find y minimum by iterating using gradient descent:
      - y function
      - hyperparamters (y_init, alpha)
      - loss
      - y gradient
    """
    epoch = epoch + 1
    y_last = f(x)
    x_new = step_dir * x_step(x)
    y_new = f(x_new)
    dump_epoch(y_last, y_new, x_new, epoch)

    if y_min_reached(y_last, y_new, x_new, epoch):
        return epoch, x_new, y_new
    elif y_new < y_last:
        find_min(f, x_new, 1.0, epoch)
    elif y_new > y_last:
        find_min(f, x, -1.0, epoch)


def gradient(x):
    """
    - original polynomial expression
    (10 * x**2) - (40 * x) - 47
    """

    """
    - find derivative or gradient 
    (20 * x) - 40 - 0
    """
    return (20.0 * x) - 40.0 - 0.0


def main():
    """
    NA. Debug NoneType issue later.
    print("After: {0} epochs".format(epoch))
    print("    x_init:  {0}".format(x_init))
    print("    y_init:  {0}".format(f(x_init)))
    print("    x_new:   {0}".format(x_new))
    print("    y_min:   {0}".format(y_min))
    epoch, x_new, y_min = find_min(f, x_init, step_dir_init, epochs_init)
    """

    find_min(f, x_init, step_dir_init, epochs_init)


if __name__ == "__main__":
    main()
