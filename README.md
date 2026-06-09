# Reversi
Marta Piraszewska  

## Opis projektu
Celem projektu jest implementacja gry Reversi w paradygmacie programowania funkcyjnego. 
  
Gra działa w trybach gracz vs gracz oraz gracz vs AI w różnych poziomach trudności. 
   
Logika gry obejmie generowanie planszy, wyznaczanie możliwych ruchów zgodnie z zasadami gry, wykonywanie ruchów wraz z odwracaniem pionków przeciwnika oraz sprawdzanie, kiedy gra powinna się zakończyć.  
  
Interfejs użytkownika jest zrealizowany w postaci terminalowej (CLI).  
  
Dodatkowo zaimplementowany jest moduł sztucznej inteligencji oparty na algorytmie Minimax z przycinaniem alfa-beta, który pozwala na wybór najlepszego ruchu poprzez analizę możliwych przyszłych stanów gry.

## Uruchomienie projektu 
Instalacja zależności:  
`make install`  
Uruchomienie gry:  
`make run`  
Uruchomienie testów jednostkowych:  
`make test`  

## Struktura projektu
Projekt składa się z następujących modułów:
- reversi.py - implementacja logiki gry,  
- minimax.py - implementacja algorytmu Minimax,  
- heuristic.py - funkcja oceny pozycji,  
- console_game.py - interfejs terminalogy gry (CLI),  
- minimax_evaluation.py - moduł do testowania skuteczności algorytmu Minimax,   
- test_reversi.py - testy jednostkowe,  
- main.py - punkt wejścia aplikacji uruchamiający grę i wybór trybu rozgrywki,  
- minimax_experiments.ipynb - notebook do uruchamiania eksperymentów i porównywania skuteczności algorytmu Minimax dla różnych głębokości przeszukiwania poprzez symulację wielu gier przeciwko losowemu graczowi.

## Reprezentacja danych
- state (stan gry) - reprezentowany jest jako krotka: (board, current_player):  
    - board - tablica dwuwymiarowa 8 na 8, zawiera wartości ‘x’, ‘o’ i ‘ ’ (pole puste), które określają jaki pionek znajduje się na danym polu,  
    - current_player - gracz, w danej chwili ma wykonać ruch, przyjmuje wartości ‘x’ albo ‘o’,  
- WEIGHTS - macierz wag określająca strategiczną wartość poszczególnych pól planszy wykorzystywana w funkcji heurystycznej,  

## Moduły gry - lista głównych funkcji

### Logika gry - plik reversi.py
- get_start_state() - zwraca początkowy stan gry w postaci krotki (board, player),  
- generate_start_board() - tworzy planszę początkową,  
- get_possible_moves(state) - zwraca listę wszystkich legalnych ruchów dla aktualnego gracza,  
- make_move(state, move) - wykonuje ruch i zwraca nową planszę,  
- update_state(state, move) - zwraca nowy stan gry po wykonaniu ruchu,  
- is_gameover(state) - sprawdza, czy gra została zakończona (żaden z graczy nie ma legalnego ruchu),   
- get_winner(board) - wyznacza zwycięzcę na podstawie liczby pionków na planszy.  

### Sztuczna inteligencja (algorytm minimax) - plik minimax.py
- minimax(state, depth, alpha, beta, ai_player) - funkcja rekurencyjna, przeszukuje możliwe stany gry do zadanej głębokości, wybierając najlepszy wynik przy założeniu optymalnej gry obu graczy,  
- get_best_move(board, depth, ai_player)- wybiera najlepszy możliwy ruch dla gracza ai, wykorzystując algorytm minimax do oceny wszystkich opcji.  

### Heurystyka - plik heuristic.py
- heuristic(board, player, weights) - oblicza ocenę planszy dla wskazanego gracza na podstawie wag przypisanych poszczególnym polom. 

### Testowanie skuteczności algorytmu Minimax - plik minimax_evaluate.py
- random_move(state) - zwraca losowy legalny ruch dla danego stanu gr,
- simulate_games(depth, games, ai_player, wins=0, draws=0, losses=0) - uruchamia wiele symulacji i zlicza wyniki (wygrane AI, remisy, porażki).

### Interfejs terminalowy (CLI) - plik console_game.py
- print_board(board) - wyświetla aktualną planszę,  
- convert_from_human_move(move) - przekształca ruch wpisany przez użytkownika (np. „3d”) na współrzędne planszy,  
- convert_to_human_move(move) - zamienia współrzędne planszy na format czytelny dla użytkownika,  
- human_player(state) -  pobiera i waliduje ruch gracza,  
- ai_player_easy(state) - wykonuje ruch komputera na łatwym poziomie (Minimax, głębokość 2),  
- ai_player_medium(state) - wykonuje ruch komputera na średnim poziomie (Minimax, głębokość 3),  
- ai_player_hard(state) - wykonuje ruch komputera na trudnym poziomie (Minimax, głębokość 4),   
- main_loop(state, players) -  główna pętla gry odpowiedzialna za wyświetlanie planszy, obsługę ruchów graczy oraz aktualizację stanu gry,   
- game() - uruchamia grę, wyświetla menu i inicjalizuje wybrany tryb rozgrywki. 

## Algorytm sztucznej inteligencji (Minimax)
Algorytm sztucznej inteligencji został zaimplementowany przy użyciu algorytmu Minimax z przycinaniem alfa-beta. Analizuje on możliwe przyszłe stany gry do zadanej głębokości i wybiera ruch prowadzący do najlepszego wyniku przy założeniu optymalnej gry obu graczy. Przycinanie alfa-beta pozwala pominąć część analizowanych stanów, co przyspiesza działanie algorytmu.  
  
Po osiągnięciu maksymalnej głębokości przeszukiwania wykorzystywana jest funkcja heurystyczna oceniająca planszę. Ocena opiera się na macierzy wag przypisanych do pól planszy - pola strategicznie korzystne mają wysokie wartości, a niekorzystne wartości ujemne. Funkcja heurystyczna sumuje wagi pionów gracza i odejmuje wagi pionów przeciwnika, zwracając pojedynczą wartość liczbową określającą jakość danej pozycji.  Dzięki temu algorytm preferuje ruchy prowadzące do zajmowania korzystnych pozycji.
    
Poprawność i skuteczność algorytmu została dodatkowo sprawdzona w notebooku minimax_experiments.ipynb, w którym przeprowadzono serię symulacji gier Minimax przeciwko losowemu graczowi. Dla 100 rozegranych partii algorytm osiągnął 89 zwycięstw, 3 remisy i 8 porażek przy głębokości przeszukiwania 2 oraz 92 zwycięstwa, 1 remis i 7 porażek przy głębokości 3 oraz 96 zwycięstw, 0 remisów i 4 porażki przy głębokości 4.  

## Interfejs terminalowy (CLI)
Interfejs konsolowy umożliwia uruchomienie i prowadzenie gry w trybie tekstowym. Program na początku wyświetla menu, w którym użytkownik wybiera tryb gry (gracz vs gracz lub gracz vs AI w różnych poziomach trudności). Dane wejściowe od użytkownika ograniczają się do wyboru opcji z menu oraz wpisywania ruchów w formacie tekstowym (np. „3d”). Ruch jest następnie konwertowany na współrzędne planszy i weryfikowany względem listy dostępnych legalnych ruchów. Jeśli jest poprawny, zostaje wykonany, a stan gry zostaje zaktualizowany.  
  
Dane wyjściowe interfejsu to przede wszystkim aktualna plansza gry wyświetlana w czytelnej formie tekstowej, lista możliwych ruchów dla aktualnego gracza oraz komunikaty informujące o przebiegu gry, takie jak kto jest aktualnym graczem, wykonany ruch AI, brak dostępnych ruchów (pas) oraz wynik końcowy. Interfejs odpowiada również za obsługę zakończenia gry i wyświetlenie zwycięzcy lub informacji o remisie. 

## Zastosowanie programowania funkcyjnego
Projekt został zaimplementowany w możliwie funkcyjnym stylu. Główna logika gry opiera się na funkcjach czystych, które nie modyfikują danych wejściowych i dla tych samych argumentów zwracają zawsze ten sam wynik. Stan gry przekazywany jest między funkcjami jako argument, a każdy ruch tworzy nowy stan zamiast modyfikacji istniejącego. W wielu miejscach użyto rekurencji zamiast pętli.  
  
Elementy niezgodne z paradygmatem funkcyjnym dotyczą głównie interfejsu użytkownika, wykonują operacje wejścia/wyjścia, a więc posiadają efekty uboczne oraz modułu eksperymentów (minimax_evaluation.py), gdzie używana jest funkcja losowa (random_move) do symulacji przeciwnika. Wynika to z  praktycznych wymagań aplikacji konsolowej i potrzeby przeprowadzania testów i nie wpływa na funkcyjny charakter głównej logiki gry.
