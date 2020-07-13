import pytest
import re


def email_validation(email):
    return bool(re.search(r"^[\w.+\-]+@[\w]+\.[a-z]{2,3}$", email))


def log(file_name, text):
    """
    Write log to file
    :param file_name:
    :param text:
    """
    with open(file_name, 'a') as f_obj:
        f_obj.write(text)


@pytest.mark.parametrize("email", ['test@test.ru', 'w@w.com', '123QWE@mmm.mmm'])
def test_is_emails_correct(email, log_file_name):
    is_valid = email_validation(email)
    log(log_file_name, email + ' = ' + str(is_valid) + '\n')
    assert is_valid is True, "Емейл валиден"


@pytest.mark.parametrize("email", ['test@test.', 'w@', '@tt'])
def test_is_emails_incorrect(email, log_file_name):
    is_valid = email_validation(email)
    log(log_file_name, email + ' = ' + str(is_valid) + '\n')
    assert is_valid is False, "Емейл не валиден"
