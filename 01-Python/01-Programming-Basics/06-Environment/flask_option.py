# pylint: disable=missing-docstring

#import os

#def start():
#    """returns the right message"""
#    pass  # YOUR CODE HERE

#if __name__ == "__main__":
#    print(start())

import os


def start():
    """returns the right message"""
    # $CHALLENGIFY_BEGIN
    env = os.getenv('FLASK_ENV')
    if env:
        return f"Starting in {env} mode..."
    return "Starting in production mode..."
    # $CHALLENGIFY_END


if __name__ == "__main__":
    print(start())
