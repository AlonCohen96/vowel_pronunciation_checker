# Created by Alon Cohen
# BA-Thesis
# https://www.cl.uzh.ch/en/studies/theses/lic-master-theses.html#:~:text=Alon%20Cohen%3A%20Aussprachebewertung%20von%20Vokalen%20mittels%20Formantenanalyse%20(PDF%2C%201%20MB)

# Installation:
# This project officially supports Python 3.7.*, if you encounter issues not mentioned in this installation, please check your python version.
# Uses libraries: sounddevice, scipy and parselmouth. If you do not have these installed please run:
# pip install sounddevice
# pip install praat-parselmouth
# pip install scipy

import os
import winsound
import parselmouth #pip install praat-parselmouth
import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import *


mint_background_color = "mint cream"
samplerate = 44100
recording_length = 0.75
recording_length_median = recording_length / 2


class App(Frame):

    def click_vowel_button(self, filepath, target_f1, target_f2):
        winsound.PlaySound(filepath, winsound.SND_FILENAME)
        self.target_f1 = target_f1
        self.target_f2 = target_f2
        self.button_record.config(state='normal')

    def click_record(self):
        recording = sd.rec(int(recording_length * samplerate), samplerate=samplerate, channels=2)
        sd.wait()
        write("recordings/output.wav", samplerate, recording)
        winsound.PlaySound('dependencies/sound_effects/windows_background.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        root.destroy()

    def createWidgets(self):
        self.label_vowels = Label(root, text="Which vowel would you like to practice today?", padx=15, pady=10, background=mint_background_color)
        self.label_vowels.grid(row=0, column=1, columnspan=3, sticky='NSEW')

        self.button_tat = Button(root, text='Tat', padx=20, pady=5, width=1, command=lambda : self.click_vowel_button('dependencies/words/Tat.wav', 750, 1150))
        self.button_tat.grid(row=2, column=0)

        self.button_mann = Button(root, text='Mann', padx=20, pady=5, width=1, command=lambda : self.click_vowel_button('dependencies/words/Mann.wav', 800, 1400))
        self.button_mann.grid(row=2, column=1)

        self.button_steg = Button(root, text='Steg', padx=20, pady=5, width=1, command=lambda : self.click_vowel_button('dependencies/words/Steg.wav', 375, 2100))
        self.button_steg.grid(row=2, column=2)

        self.button_bett = Button(root, text='Bett', padx=20, pady=5, width=1, command=lambda : self.click_vowel_button('dependencies/words/Bett.wav', 500, 1900))
        self.button_bett.grid(row=2, column=3)

        self.button_stiel = Button(root, text='Stiel', padx=20, pady=5, width=1, command=lambda : self.click_vowel_button('dependencies/words/Stiel.wav', 275, 2400))
        self.button_stiel.grid(row=2, column=4)

        self.button_kick = Button(root, text='Kick', padx=20, pady=5, width=1, command=lambda : self.click_vowel_button('dependencies/words/Kick.wav', 325, 2200))
        self.button_kick.grid(row=3, column=0)

        self.button_tot = Button(root, text='Tot', padx=20, pady=5, width=1, command=lambda : self.click_vowel_button('dependencies/words/Tot.wav', 375, 850))
        self.button_tot.grid(row=3, column=1)

        self.button_kopf = Button(root, text='Kopf', padx=20, pady=5, width=1, command=lambda : self.click_vowel_button('dependencies/words/Kopf.wav', 500, 900))
        self.button_kopf.grid(row=3, column=2)

        self.button_mut = Button(root, text='Mut', padx=20, pady=5, width=1, command=lambda : self.click_vowel_button('dependencies/words/Mut.wav', 275, 750))
        self.button_mut.grid(row=3, column=3)

        self.button_kuss = Button(root, text='Kuss', padx=20, pady=5, width=1, command=lambda : self.click_vowel_button('dependencies/words/Kuss.wav', 325, 850))
        self.button_kuss.grid(row=3, column=4)

        self.button_bös = Button(root, text='Bös', padx=20, pady=5, width=1, command=lambda : self.click_vowel_button('dependencies/words/Bös.wav', 375, 1700))
        self.button_bös.grid(row=4, column=0)

        self.button_töff = Button(root, text='Töff', padx=20, pady=5, width=1, command=lambda : self.click_vowel_button('dependencies/words/Töff.wav', 500, 1550))
        self.button_töff.grid(row=4, column=1)

        self.button_kühl = Button(root, text='Kühl', padx=20, pady=5, width=1, command=lambda : self.click_vowel_button('dependencies/words/Kühl.wav', 275, 2000))
        self.button_kühl.grid(row=4, column=2)

        self.button_record = Button(root, text='Record', background="orange red", state=DISABLED, command=self.click_record)
        self.button_record.grid(row=5, column=2, pady=25)

        self.label_note = Label(root, text='To get optimal results, speak loud and clear.'
                                           '\n The recording window is only one second, so speak as soon as you hit "Record".'
                                           '\n If you keep getting extremely low results, you are probably speaking too early or too late.')
        self.label_note.grid(row=6, columnspan=5)

    def on_closing(self):
        if os.path.exists("recordings/output.wav"):
            os.remove("recordings/output.wav")
        exit()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()


class Evaluation(Frame):

    def evaluation_fomula(self):
        #Read formants
        sound = parselmouth.Sound('recordings/output.wav')
        formant_object = sound.to_formant_burg()
        stu_f1 = formant_object.get_value_at_time(1, recording_length_median)
        stu_f2 = formant_object.get_value_at_time(2, recording_length_median)

        #For debugging
        #print("student f1: ", stu_f1)
        #print("student f2: ", stu_f2)

        #Evaluate
        ### F1 ###
        f1_score = stu_f1 / app.target_f1 * 100
        if f1_score > 100:
            f1_score = 200 - f1_score

        ### F2 ###
        f2_score = stu_f2 / app.target_f2 * 100
        if f2_score > 100:
            f2_score = 200 - f2_score

        ### Total score ###
        self.total_score = round((f1_score + f2_score) / 2)
        if self.total_score < 0:
            self.total_score = 0

        ### Feedback ###
        if self.total_score >= 80:
            self.feedback = 'Congratulations, you sound like a native!'
        elif self.total_score >= 70:
            self.feedback = 'Not perfect, but not completely off either.'
        else:
            self.feedback = 'This does not sound quite right. Give it another shot.'

    def click_tryAgain(self):
        root2.destroy()

    def click_quit(self):
        os.remove("recordings/output.wav")
        exit()

    def createWidgets(self):
        self.label_title = Label(root2, text="Your score is", background=mint_background_color)
        self.label_title.pack()

        self.label_score = Label(root2, text=str(self.total_score)+'%', font=(None, 50), padx=50, pady=25, background=mint_background_color)
        self.label_score.pack()

        self.label_feedback = Label(root2, text=self.feedback, background=mint_background_color)
        self.label_feedback.pack()

        self.button_tryAgain = Button(root2, text="Try again", command=self.click_tryAgain)
        self.button_tryAgain.pack()

        self.button_quit = Button(root2, text="Quit", command=self.click_quit)
        self.button_quit.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.evaluation_fomula()
        self.pack()
        self.createWidgets()


while True:
    root = Tk()
    root.title("Vowel Pronuciation Checker")
    root.configure(background=mint_background_color)
    app = App(master=root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()

    root2 = Tk()
    root2.title("Evaluation")
    root2.configure(background=mint_background_color)
    evaluation = Evaluation(master=root2)
    evaluation.mainloop()