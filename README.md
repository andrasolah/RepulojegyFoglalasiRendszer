# RepulojegyFoglalasiRendszer
Repülőjegy Foglalási Rendszer


# Repülőjegy Foglalási Rendszer

Ez a projekt egy egyszerű repülőjegy foglalási rendszert valósít meg, ahol járatokra lehet jegyet foglalni, lemondani a foglalást, és megtekinteni az aktuális foglalások listáját.

## Fő osztályok

- **Járat (absztrakt osztály):** Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).
- **BelföldiJarat:** Belföldi járatokra vonatkozó osztály, amelyek olcsóbbak és rövidebbek.
- **NemzetkoziJarat:** Nemzetközi járatokra vonatkozó osztály, magasabb jegyárakkal.
- **LégiTársaság:** Tartalmazza a járatokat és saját attribútumot, mint például a légitársaság neve.
- **JegyFoglalás:** A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.

## Funkciók

- **Jegy foglalása:** A járatokra jegyet lehet foglalni, és visszaadja a foglalás árát.
- **Foglalás lemondása:** A felhasználó lemondhatja a meglévő foglalást.
- **Foglalások listázása:** Az összes aktuális foglalás listázása.

## Adatvalidáció

- Ellenőrzi, hogy a járat elérhető-e foglalásra, és hogy a foglalás időpontja érvényes-e.
- Biztosítja, hogy csak létező foglalásokat lehessen lemondani.

## Felhasználói interfész

- Egyszerű felhasználói interfész, amely lehetővé teszi a következő műveleteket:
  - Jegy foglalása
  - Foglalás lemondása
  - Foglalások listázása

## Előkészítés

A rendszer indulásakor egy légitársaság, 3 járat és 6 foglalás előre be van töltve a rendszerbe, így a felhasználó azonnal használatba veheti a rendszert.