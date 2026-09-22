def add(a, b):
    """İki sayıyı toplar."""
    return a + b


def subtract(a, b):
    """İlk sayıdan ikinci sayıyı çıkarır."""
    return a - b


def multiply(a, b):
    """İki sayıyı çarpar."""
    return a * b


def divide(a, b):
    """İlk sayıyı ikinci sayıya böler. 0'a bölme hatasını engeller."""
    if b == 0:
        raise ValueError("Bir sayı 0'a bölünemez.")
    return a / b


def power(a, b):
    """a sayısının b. kuvvetini alır."""
    return a ** b


def modulus(a, b):
    """a sayısının b'ye bölümünden kalanı verir."""
    if b == 0:
        raise ValueError("Bir sayı 0'a göre mod alınamaz.")
    return a % b