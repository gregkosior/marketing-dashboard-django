📊 Marketing Analytics Dashboard

Flask & Django | Data → API → Web App

Projekt edukacyjno-portfoliówy pokazujący pełny proces pracy z danymi:
od surowych plików CSV, przez analizę i czyszczenie danych, bazę SQL, aż po aplikacje webowe we Flasku i Django.

🎯 Cel projektu

Celem projektu było:

praktyczne przejście pełnego pipeline’u danych

nauka pracy z:

Pythonem

SQL

HTTP / API

Flask

Django

porównanie Flask vs Django na tym samym problemie

zbudowanie projektu portfolio pod staż / junior backend / data

Projekt był rozwijany krok po kroku, z naciskiem na zrozumienie, a nie kopiowanie gotowych rozwiązań.

🧠 Etapy projektu (krok po kroku)
1️⃣ Analiza i czyszczenie danych (Jupyter Notebook)

Projekt rozpoczął się od pracy na surowych danych CSV (dane sklepowe / e-commerce).

Utworzono dwa notebooki Jupyter:

📒 Notebook 1 – eksploracja danych

wczytanie CSV (pandas)

analiza kolumn i typów danych

sprawdzenie braków danych

wstępne statystyki

📒 Notebook 2 – czyszczenie danych

usunięcie niepotrzebnych kolumn

ujednolicenie nazw

poprawa typów danych

wyliczenie nowych kolumn (np. PnL)

zapis czystego, gotowego pliku CSV

📌 Efekt:
➡️ gotowy plik CSV przygotowany pod bazę danych

2️⃣ Baza danych SQL (SQLite)

Po przygotowaniu danych:

załadowano oczyszczony CSV do SQLite

zaprojektowano prostą strukturę tabeli

wykonano podstawowe zapytania SQL:

SUM

GROUP BY

agregacje danych

📌 Efekt:
➡️ jedno źródło danych do aplikacji webowych

3️⃣ Aplikacja webowa – Flask (backend + frontend)

Kolejnym krokiem było zbudowanie aplikacji we Flasku, aby:

zrozumieć podstawy:

HTTP

routing

API

zobaczyć „manualne” podejście do backendu

Funkcjonalności Flask:

endpointy API:

/api/summary

/api/group

połączenie z SQLite

frontend:

HTML

CSS

JavaScript (fetch)

dashboard z:

podsumowaniem danych

tabelą wyników

📌 Wnioski:

Flask daje dużą swobodę

ale przy większym UI i strukturze wymaga więcej ręcznej pracy

łatwo o błędy w ścieżkach, statycznych plikach i HTML

4️⃣ Aplikacja webowa – Django (porównanie z Flask)

Po zamknięciu etapu Flask projekt został przepisany na Django, aby:

porównać oba frameworki w praktyce

zobaczyć różnice w:

strukturze

organizacji kodu

pracy z HTML

obsłudze bazy danych

Django – kluczowe elementy:

projekt + aplikacje (startproject, startapp)

narzucona struktura

migracje

ORM

czytelny podział:

views

urls

templates

models

📌 Wnioski:

Django ma więcej konfiguracji na start

ale po opanowaniu struktury:

praca jest szybsza

kod czytelniejszy

łatwiej rozwijać aplikację

framework lepiej nadaje się do większych projektów

⚖️ Flask vs Django – podsumowanie
Obszar	Flask	Django
Start	szybki	wolniejszy
Struktura	dowolna	narzucona
HTML	ręcznie	templates + layout
Baza danych	ręczny SQL	ORM
Skalowalność	mniejsza	duża
Projekty	małe / API	większe aplikacje
🛠️ Technologie

Python 3

Pandas

Jupyter Notebook

SQLite

Flask

Django

HTML / CSS

JavaScript (Fetch API)

Git / GitHub

📁 Struktura projektu (przykład)
project/
├── notebooks/
│   ├── 01_exploration.ipynb
│   └── 02_cleaning.ipynb
│
├── data/
│   ├── raw.csv
│   └── clean.csv
│
├── flask_app/
│   └── ...
│
├── django_app/
│   └── ...
│
├── README.md
└── requirements.txt

🚀 Dalsze plany rozwoju

druga aplikacja Django z innymi danymi

menu / przełącznik między dashboardami

refaktoryzacja SQL i modeli

logowanie użytkowników

role (admin / user)

rozbudowany projekt HR (Django)
📌 Podsumowanie

Projekt pokazuje pełny proces pracy z danymi i aplikacją webową:
od surowych plików CSV, przez analizę, bazę danych, API, aż po frontend.

Jest to projekt edukacyjny, ale budowany w sposób zbliżony do realnych projektów komercyjnych.
