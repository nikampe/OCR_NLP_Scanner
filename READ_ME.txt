Im Ordner Kopie des aktuellen Stands finden sich die relevanten Python Skripte.

Relevant sind folgende:

finalpreprocessing.py
	- Hier befindet sich die generelle Preprocessing Funktion, aus der im Moment die Zuschneidung des Bildes ausgeklammert wird.
	- Daher benötigt die Funktion das bereits zugeschnittene Bild als Input

test_preprocessing.py
	- Das Skript bearbeitet das Bild, liest es mit tesseract aus, fügt spacy ein und gibt folgende Werte aus:
		- True: Der Beleg enthält ein Währungssymbol

		- False: Kein Währungssymbol auf dem Beleg