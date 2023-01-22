# Created by Alon Cohen

# Installation:
# This project officially supports Python 3.7.*, if you encounter issues not mentioned in this installation, please check your python version.
# Uses libraries: sounddevice, scipy and parselmouth. If you do not have these installed please run:
# pip install sounddevice
# pip install praat-parselmouth
# pip install scipy

import time
import parselmouth
import sounddevice as sd
from scipy.io.wavfile import write

def choose_vowel():
    ''' Asks user which vowel they want to practice and returns the corresponding target formants values. '''

    database = {'a': [657, 1028], 'e': [304, 2137], 'i': [275, 2400], 'o': [375, 850], 'u': [275, 750]}
    chosen_vowel = input("Which vowel would you like to practice, a, e, i, o, u? ")
    return database.get(chosen_vowel)

def recorder(freq, seconds, filename):
    ''' Takes in frequency, recording length and filename, records audio and writes a .wav file. '''

    # Little countdown to give the student time to get ready
    s = 4
    while s > 1: s -= 1; print(s), time.sleep(1)
    print('### RECORDING ###')

    recording = sd.rec(int(seconds * freq), samplerate=freq, channels=2)
    sd.wait()
    write(filename, freq, recording)

    print('### STOPPED RECORDING ###')

def read_formants(filename):
    ''' Takes in filename, ready formants out of it and returns them. '''

    sound = parselmouth.Sound(filename)
    formant_object = sound.to_formant_burg()

    stu_f1 = formant_object.get_value_at_time(1, 1)
    stu_f2 = formant_object.get_value_at_time(2, 1)

    print("Student formants:", stu_f1, stu_f2)

    return stu_f1, stu_f2

def evaluation(stu_f1, stu_f2, target_f1, target_f2):
    ''' Takes in target and student formants, evaluates the pronunciation and gives a feedback. '''

    ### F1 ###
    f1_score = stu_f1 / target_f1 * 100
    if f1_score > 100:
        f1_score = 200 - f1_score
    print('f1-score:', f1_score)

    ### F2 ###
    f2_score = stu_f2 / target_f2 * 100
    if f2_score > 100:
        f2_score = 200 - f2_score
    print('f2-score:', f2_score)

    ### Total score ###
    total_score = (f1_score + f2_score) / 2
    if total_score < 0:
        total_score = 0

    ### Feedback ###
    if total_score >= 80:
        print('Your score is:', total_score, 'Congratulations, you sound like a native!')
    elif total_score >= 70:
        print('Your score is:', total_score, 'Not perfect, but not completely off either.')
    else:
        print('Your score is:', total_score, 'This does not sound quite right. Give it another shot.')


target_f1, target_f2 = choose_vowel()
recorder(44100, 2, 'output.wav')
stu_f1, stu_f2 = read_formants('output.wav')
evaluation(stu_f1, stu_f2, target_f1, target_f2)