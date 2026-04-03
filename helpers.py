import random

class CredentialGenerator:
    @staticmethod
    def generate_email_and_password():
        email = f'test{random.randint(1, 99999)}selenium-{random.randint(1, 99999)}@mail.ru'
        password = f'testpass-{random.randint(100, 999)}'
        credentials = {'email': email, 'password': password}
        print(f"Сгенерированы учётные данные: email={email}, password={password}")
        return credentials
    
    @staticmethod
    def generate_incorrect_email():
        email = f'test{random.randint(1, 99999)}selenium-{random.randint(1, 99999)}'
        print(f"Сгенерированы учётные данные: email={email}")
        return email
    