import logging as logger
import random
import string


def generate_random_email_and_password(domain=None, email_prefix=None):
    logger.debug('Generating random email and password.')

    if not domain:
        domain = 'test.com'
    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10
    random_password_string_length = 20

    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    password_string = ''.join(random.choices(string.ascii_letters, k=random_password_string_length))

    email = f'{email_prefix}_{random_string}@{domain}'

    random_info = {'email': email, 'password': password_string}
    logger.debug(f'Randomly generated email and password: {random_info}')

    return random_info
    