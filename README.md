# Gra w życie (Bioweb)

Aplikacja pozwala na interaktywną symulację z interfejsem webowym Gry w życie (ang. Conway's Game of Life), logika gry jest napisana w C++ i wspiera współbieżne przetwarzanie siatki gry.

Aplikacja wykorzystuje [Środowisko Bioweb](http://bioweb.sourceforge.net/en/index.html)

## Instalacja

Kroki instalacji są takie same jak w [instrukcji bioweb 0.09](https://sourceforge.net/projects/bioweb/files/0.09/).

W razie problemów z instalacją - rekomenduję wykorzystanie obrazu [docker-bioweb](https://github.com/krystiancha/docker-bioweb), to rozwiązanie wymaga jedynie podmiany plików kodu źródłowego, wykonanie kroków 2 i 8 instrukcji, oraz rekompilacji aplikacji.

## Uruchomienie

Zakładając, że aplikacja została skonfigurowana i skompilowana należy użyć:

```
scons r=l
```

Następnie aplikacja powinna być dostępna pod adresem: [localhost:9000](http://localhost:9000)

## Wielowątkowość w aplikacji

W aplikacji wielowątkowość została wykorzystana do równoległego przetwarzania siatki Gry w życie.

Dla poniższej numeracji siatki 4x4:

```
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
```

Tak zostałaby przetworzona siatka dla 2 i 4 wątków:

```
Thread 1    |   Thread 2
1  2  3  4  |   9  10 11 12
5  6  7  8  |   13 14 15 16
```

```
Thread 1    |   Thread 2    |   Thread 3     |   Thread 4
1  2  3  4  |   5  6  7  8  |   9  10 11 12  |   13 14 15 16
```

Po kompilacji aplikacji, w katalogu `build_web/conwaypy`, można uruchomić symulację `speedtest.py`, która mierzy czas na przetworzenie siatki o zadanych wymiarach. Oto  rezultat jaki uzyskałem na swoim komputerze:

```
grid NxN, N = 16384
1 thread: 316.4368 s
2 thread: 239.5751 s
4 thread: 199.2044 s
```

Symulacja uwzględnia czas na skonwertowanie `boost::python::list` na `std::vector<std::vector<bool>>` - możliwe, że przez to czas wykonania nie zachowuje się odwrotnie proporcjonalnie do liczby wątków.
