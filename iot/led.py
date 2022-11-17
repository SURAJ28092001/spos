import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN)



while True :
    prox_val = GPIO.input(36)
    if prox_val :
        print("obstacle detected\n")
        
    else :
        print("No obstacle detected\n")