from pydantic import BaseModel, SecretStr


class UserWithPassword(BaseModel):
    username: str
    password: SecretStr


user = UserWithPassword(
    username="alice",
    password="pwd"
)

print(user)
# username='alice' password=SecretStr('**********')

# Чтобы получить реальное значение пароля:
real_password = user.password.get_secret_value()
print(real_password)  # super_secret_password
