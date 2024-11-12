def function(x):
    return x * x * x - (x + 1)  # Funkcja x^3 - (x + 1), sprawdzenie czy znaleziono miejsce zerowe funkcji

def look():
    a = int(input("Podaj liczbę a: "))
    b = int(input("Podaj liczbę b: "))
    epsilon = 0.001

    # Sprawdzenie, czy przedział zawiera pierwiastek
    if function(a) * function(b) >= 0:
        return "Brak pierwiastka w tym przedziale"

    while abs(a - b) > epsilon:  # Sprawdzenie odległości między a i b
        c = (a + b) / 2  # Obliczenie punktu środkowego

        if function(c) == 0:  # Jeżeli znaleziono dokładny pierwiastek
            return c
        elif function(a) * function(c) < 0:  # Pierwiastek znajduje się w przedziale [a, c]
            b = c  # Skraca przedział zmieniając b na c
        else:  # Pierwiastek znajduje się w przedziale [c, b]
            a = c

    return (a + b) / 2  # Zwraca przybliżoną wartość pierwiastka

print(look())
