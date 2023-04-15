# Vowel Pronunciation Checker
A Tool to practice German Vowels for language students that I developed for my [Bachelors Thesis](https://www.cl.uzh.ch/en/studies/theses/lic-master-theses.html#:~:text=Alon%20Cohen%3A%20Aussprachebewertung%20von%20Vokalen%20mittels%20Formantenanalyse%20(PDF%2C%201%20MB)%0A%5BDec%202019%2C%20bachelor%27s%20thesis%2C%20German%5D) in Fall 2019 at the University of Zurich which was graded with a 6.

# Overview
This app enables language students to practice their pronunciation of German vowels. This was achieved with the help of formant analysis, whereby an evaluation algorithm checks the similarity of the user formants and the target formants of the respective vowel. The program provides reliable results for most vowels of the German language including umlauts.
Vowel Pronunciation Checker is written in Python. To access the Praat API I used [Parslemouth Open Source library](https://github.com/YannickJadoul/Parselmouth) for Python, [SciPy](https://github.com/scipy/scipy) for background calculations and [Tkinter](https://github.com/python/cpython/tree/master/Lib/tkinter) to create a simple GUI.

![VPC interface](https://user-images.githubusercontent.com/27009186/232230896-fd445b7d-7827-4db1-9e69-e411497caebb.PNG)
