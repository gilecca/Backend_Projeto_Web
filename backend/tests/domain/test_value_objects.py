import pytest
from petfit.domain.value_objects.email_vo import Email
from petfit.domain.value_objects.password import Password

def test_valid_email():
    email = Email("user@example.com")
    assert email.value() == "user@example.com"

def test_invalid_email():
    with pytest.raises(ValueError):
        Email("invalid-email")

def test_valid_password():
    pwd = Password("Secret123")
    assert pwd.value() == "Secret123"

def test_invalid_password():
    with pytest.raises(ValueError):
        Password("short")

def test_password_hidden_str():
    pwd = Password("Secret123")
    assert str(pwd) == "*********"

@pytest.mark.parametrize(
    "senha_invalida",
    [
        "curta",  # Menos de 8 caracteres
        "semmaiuscula1!",  # Sem letra maiúscula
        "SEMMINUSCULA1!",  # Sem letra minúscula
        "SemNumero!",  # Sem número
        "SemEspecial1",  # Sem caractere especial
    ],
)
def test_senhas_invalidas_disparam_erro(senha_invalida):
    with pytest.raises(PasswordValidationError):
        Password(senha_invalida)


# Teste de criação de senha válida
def test_criar_password_valido():
    senha = "Senha@123!"
    password = Password(senha)
    assert isinstance(password, Password)
    assert password.verify(senha)


# Teste de verificação com senha incorreta
def test_password_invalida_nao_verifica():
    senha = "Senha@123!"
    outra_senha = "Errada456@"
    password = Password(senha)
    assert not password.verify(outra_senha)


# Teste de representação em string (usando __str__)
def test_str_password_exibe_hash():
    senha = "Senha@123!"
    password = Password(senha)
    assert str(password) == password._hashed