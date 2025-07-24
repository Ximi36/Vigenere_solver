# Vigenere_solver

## Ogólny zarys działania:

Funkcja `vigenere`: Jest używana do manipulowania tekstem (zarówno podczas szyfrowania, jak i deszyfrowania), chociaż w tym przypadku ma na celu obliczenie przesunięcia liter na podstawie klucza.

Funkcja `vigenere_decrypt`: Służy do odwrócenia operacji Vigenère'a, w szczególności w celu testowania różnych kluczy na zaszyfrowanym tekście, aby znaleźć ten najbardziej pasujący do rozkładu częstotliwości liter w języku polskim.

Funkcja `compare_freq`: Porównuje częstość występowania liter w odszyfrowanym tekście z oczekiwanymi częstościami liter w języku polskim. Jest kluczowa do oceny, który z próbnych kluczy najprawdopodobniej odszyfrował tekst poprawnie.

Funkcja `solve_vigenere`: Jest kluczową funkcją łamania szyfru Vigenère'a. Działa, próbując różne długości klucza i porównując różne przesunięcia dla każdego fragmentu zaszyfrowanego tekstu, aby znaleźć klucz, który daje wynik najbliższy polskiej częstotliwości liter.



## General Overview of Operation:

The `vigenere` function is used to manipulate text (both for encryption and decryption), although in this context its purpose is to calculate letter shifts based on a key.

The `vigenere_decrypt` function is used to reverse the Vigenère operation, specifically to test various keys on the encrypted text in order to find the one that best matches the letter frequency distribution of the Polish language.

The `compare_freq` function compares the frequency of letters in the decrypted text with the expected letter frequencies in Polish. It is essential for evaluating which of the trial keys most likely decrypted the text correctly.

The `solve_vigenere` function is the key function for breaking the Vigenère cipher. It works by trying different key lengths and comparing different shifts for each segment of the encrypted text in order to find the key that produces a result closest to Polish letter frequency.
