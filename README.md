# Vigenere_solver

## Ogólny zarys działania:

Funkcja `vigenere`: Jest używana do manipulowania tekstem (zarówno podczas szyfrowania, jak i deszyfrowania), chociaż w tym przypadku ma na celu obliczenie przesunięcia liter na podstawie klucza.

Funkcja `vigenere_decrypt`: Służy do odwrócenia operacji Vigenère'a, w szczególności w celu testowania różnych kluczy na zaszyfrowanym tekście, aby znaleźć ten najbardziej pasujący do rozkładu częstotliwości liter w języku polskim.

Funkcja `compare_freq`: Porównuje częstość występowania liter w odszyfrowanym tekście z oczekiwanymi częstościami liter w języku polskim. Jest kluczowa do oceny, który z próbnych kluczy najprawdopodobniej odszyfrował tekst poprawnie.

Funkcja `solve_vigenere`: Jest kluczową funkcją łamania szyfru Vigenère'a. Działa, próbując różne długości klucza i porównując różne przesunięcia dla każdego fragmentu zaszyfrowanego tekstu, aby znaleźć klucz, który daje wynik najbliższy polskiej częstotliwości liter.
