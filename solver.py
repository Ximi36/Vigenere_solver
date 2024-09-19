import itertools
import string
import textwrap


# Funkcja wykonuje operację Vigenère'a na tekście. Przesuwa litery tekstu na podstawie cyklicznie powtarzanego klucza.
# Zwraca wynik, który może być użyty do szyfrowania lub deszyfrowania, w zależności od klucza.
def vigenere(plaintext, key, a_is_zero=True):
    key = key.lower()  # Zamiana klucza na małe litery
    key_iter = itertools.cycle(map(ord, key))  # Klucz przekształcony na wartości ASCII i cyklicznie powtarzany
    return "".join(
        # Dla każdej litery tekstu jawnego obliczamy nową literę po przesunięciu jej o wartość wynikającą z klucza
        chr(ord('a') + ((next(key_iter) - ord('a') + ord(letter) - ord('a')) + (0 if a_is_zero else 2)) % 27)
        if letter in string.ascii_lowercase or letter == "{"  # Obsługujemy litery oraz znak spacji, reprezentowany przez '{'
        else letter  # Pozostawiamy inne znaki bez zmian
        for letter in plaintext.lower()  # Operujemy na tekście zamienionym na małe litery
    )


# Funkcja deszyfrująca tekst zaszyfrowany szyfrem Vigenère'a. Tworzy odwrotny klucz, który pozwala odwrócić operację szyfrującą.
def vigenere_decrypt(ciphertext, key, a_is_zero=True):
    # Generowanie odwrotnego klucza poprzez odwrócenie przesunięcia liter
    inverse = "".join(chr(ord('a') +
                          ((27 if a_is_zero else 22) -  # Odwracamy przesunięcie o wartość klucza
                           (ord(k) - ord('a'))
                           ) % 27) for k in key)
    # Użycie funkcji vigenere z odwrotnym kluczem do odszyfrowania tekstu
    return vigenere(ciphertext, inverse, a_is_zero)


# Tabela częstotliwości liter w języku polskim, gdzie ostatnia pozycja to spacja
POLISH_FREQ = [
    0.08379652,  # A
    0.012436055,  # B
    0.03722425,  # C
    0.02763288,  # D
    0.075958953,  # E
    0.002618117,  # F
    0.011554958,  # G
    0.008995581,  # H
    0.06953114,  # I
    0.01966105,  # J
    0.028623065,  # K
    0.032575415,  # L
    0.024427365,  # M
    0.048544249,  # N
    0.07060524,  # O
    0.026021731,  # P
    0.0000251742,  # Q (nie używana w polskim, ale potrzebna dla pełności alfabetu)
    0.038357089,  # R
    0.041503864,  # S
    0.033280292,  # T
    0.019694616,  # U
    0.000285308,  # V (rzadko występuje w polskim)
    0.038172479,  # W
    0.000159437,  # X (rzadko występuje)
    0.03236563,  # Y
    0.055097932,  # Z
    0.16086  # Spacja (reprezentowana przez '{')
]


# Funkcja porównująca częstość występowania liter w tekście z oczekiwaną częstością dla języka polskiego.
# Zwraca sumę różnic między rzeczywistymi i oczekiwanymi częstościami.
def compare_freq(text):
    if not text:
        return None  # Zwracamy None, jeśli tekst jest pusty
    # Przefiltrowanie tekstu, aby pozostały tylko litery i spacja ('{')
    text = [t for t in text.lower() if t in string.ascii_lowercase or t == "{"]
    freq = [0] * 27  # Inicjalizujemy listę na zliczanie częstości liter (27 pozycji: 26 liter + spacja)
    total = float(len(text))  # Łączna liczba liter w tekście

    # Zliczamy wystąpienia każdej litery w tekście
    for l in text:
        freq_index = ord(l) - ord('a')  # Obliczamy indeks dla litery (odpowiednik pozycji w alfabecie)
        freq[freq_index] += 1  # Zwiększamy licznik dla danej litery

    # Zwracamy sumę różnic między obserwowaną a oczekiwaną częstością dla każdej litery
    return sum(abs(f / total - E) for f, E in zip(freq, POLISH_FREQ))


# Funkcja próbująca złamać szyfr Vigenère'a na podstawie analizy częstości liter.
# Testuje różne długości klucza i różne przesunięcia dla każdej litery, aby znaleźć klucz najlepiej pasujący do częstotliwości liter w języku polskim.
def solve_vigenere(text, a_is_zero=True):
    best_keys = []  # Lista przechowująca najlepsze klucze
    key_min_size = 3  # Minimalna długość klucza, którą sprawdzamy
    key_max_size = 10  # Maksymalna długość klucza, którą sprawdzamy

    # Przefiltrowanie tekstu, aby pozostały tylko litery i spacje ('{')
    text_letters = [c for c in text.lower() if c in string.ascii_lowercase or c == '{']

    # Próbujemy różnych długości klucza
    for key_length in range(key_min_size, key_max_size):
        key = [None] * key_length  # Inicjalizujemy tablicę na znaki klucza
        # Dla każdej pozycji w kluczu próbujemy znaleźć najlepsze dopasowanie
        for key_index in range(key_length):
            # Pobieramy litery z tekstu w interwałach odpowiadających pozycji w kluczu
            letters = "".join(itertools.islice(text_letters, key_index, None, key_length))
            shifts = []
            # Testujemy każdą literę alfabetu jako możliwy znak klucza
            for key_char in string.ascii_lowercase + '{':
                # Odszyfrowujemy fragment tekstu przy użyciu pojedynczego znaku klucza i oceniamy wynik
                shifts.append(
                    (compare_freq(vigenere_decrypt(letters, key_char, a_is_zero)), key_char)
                )
            # Wybieramy znak klucza, który daje najlepsze dopasowanie do częstości liter
            key[key_index] = min(shifts, key=lambda x: x[0])[1]
        # Zapisujemy znaleziony klucz
        best_keys.append("".join(key))

    # Sortujemy klucze według ich dopasowania do częstości liter i zwracamy najlepszy klucz
    best_keys.sort(key=lambda key: compare_freq(vigenere_decrypt(text, key, a_is_zero)))
    return best_keys[:1]  # Zwracamy tylko najlepszy klucz


# Funkcja zamieniająca spacje na znak '{', aby poprawnie obsługiwać szyfr Vigenère'a (szyfr obejmuje spacje)
def replace_spaces(ciphertext):
    return ciphertext.replace(' ', '{')


# Funkcja przywracająca spacje z powrotem z zamiennika '{'
def antyspace(ciphertext):
    return ciphertext.replace('{', ' ')


# Główny program:
CIPHERTEXT = input("Podaj tekst do odszyfrowania: ")  # Wczytanie zaszyfrowanego tekstu od użytkownika

CIPHERTEXT = replace_spaces(CIPHERTEXT)  # Zamiana spacji na '{' w tekście

# Wyświetlamy zaszyfrowany tekst
print("Rozwiązywanie szyfru Vigenere'a:")
print("*" * 80)
print(textwrap.fill(CIPHERTEXT, 80))  # Wyświetlamy tekst w bardziej czytelnej formie
print("*" * 80)

# Próbujemy złamać szyfr
for key in reversed(solve_vigenere(CIPHERTEXT)):
    print("")
    print("Znaleziony klucz:", antyspace(key))  # Wyświetlamy znaleziony klucz, zamieniając '{' na spacje.
    print("Rozwiązanie:")
    print("=" * 80)

    # Odszyfrowujemy tekst i wyświetlamy go w czytelnej formie.
    print(antyspace(textwrap.fill(vigenere_decrypt(CIPHERTEXT, key))))
    print("=" * 80)
