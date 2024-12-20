from random import SystemRandom
from django.utils.text import slugify
import string


def random_letters(k=5):
    return "".join(SystemRandom().choices(string.ascii_letters + string.digits, k=k))


def slugfy_new(text, k=5):
    return slugify(text) + "-" + random_letters(k)
