from machine import Pin, Timer, PWM
import time


led = Pin(25, Pin.OUT)  # onboard LED
output_pins = {i: Pin(i, Pin.OUT, value=1) for i in range(12, 20)}
button =  Pin(28, Pin.IN, Pin.PULL_DOWN)
zero_cross = Pin(22, Pin.IN, Pin.PULL_DOWN)
triac_out = Pin(20, Pin.OUT, 0) 
buzzer = PWM(Pin(11))
buzzer.freq(2000)
buzzer.duty_u16(0)




def turn_off():
    for pin in output_pins.values():
        pin.value(1)
def state0():
    not_displayed = [12, 16]
    for i in range(12, 20):
        output_pins[i].value(1 if i in not_displayed else 0)

def state1():
    not_displayed = [12, 13, 14, 16, 18, 19]
    for i in range(12, 20):
        output_pins[i].value(1 if i in not_displayed else 0)
    pulse_count = 0
    pulses = [1,2]
    prev_state = zero_cross.value()
    
    while not button.value():
        current_state = zero_cross.value()
        if current_state != prev_state:
            pulse_count = (pulse_count + 1) % 20
            if pulse_count in pulses:
                send_pulses()
        prev_state = current_state
            

def state2():
    not_displayed = [13, 16, 17]
    for i in range(12, 20):
        output_pins[i].value(1 if i in not_displayed else 0)
    pulse_count = 0
    pulses = [1,2,10,11]
    prev_state = zero_cross.value()
    
    while not button.value():
        current_state = zero_cross.value()
        if current_state != prev_state:
            pulse_count = (pulse_count + 1) % 21
            if pulse_count in pulses:
                send_pulses()
        prev_state = current_state
    

def state3():
    not_displayed = [13, 16, 19]
    for i in range(12, 20):
        output_pins[i].value(1 if i in not_displayed else 0)
    pulse_count = 0
    pulses = [1,2,8,9,15,16]
    prev_state = zero_cross.value()
    
    while not button.value():
        current_state = zero_cross.value()
        if current_state != prev_state:
            pulse_count = (pulse_count + 1) % 20
            if pulse_count in pulses:
                send_pulses()
        prev_state = current_state
    

def state4():
    not_displayed = [14, 16, 18, 19]
    for i in range(12, 20):
        output_pins[i].value(1 if i in not_displayed else 0)
    pulse_count = 0
    pulses = [1,2,6,7,11,12,16,17]
    prev_state = zero_cross.value()
   
    while not button.value():
        current_state = zero_cross.value()
        if current_state != prev_state:
            pulse_count = (pulse_count + 1) % 20
            if pulse_count in pulses:
                send_pulses()
        prev_state = current_state
    

def state5():
    not_displayed = [15, 16, 19]
    for i in range(12, 20):
        output_pins[i].value(1 if i in not_displayed else 0)
    pulse_count = 0
    pulses = [1,2,5,6,10,11,15,16,19,20]
    prev_state = zero_cross.value()
    
    while not button.value():
        current_state = zero_cross.value()
        if current_state != prev_state:
            pulse_count = (pulse_count + 1) % 20
            if pulse_count in pulses:
                send_pulses()
        prev_state = current_state

    
def state6():
    not_displayed = [14, 15, 16]
    for i in range(12, 20):
        output_pins[i].value(1 if i in not_displayed else 0)
    pulse_count = 0
    pulses = [1,2,4,5,8,9,12,13,16,17,19,20]
    prev_state = zero_cross.value()
    
    while not button.value():
        current_state = zero_cross.value()
        if current_state != prev_state:
            pulse_count = (pulse_count + 1) % 20
            if pulse_count in pulses:
                send_pulses()
        prev_state = current_state
    

def state7():
    not_displayed = [12, 13, 16, 18, 19]
    for i in range(12, 20):
        output_pins[i].value(1 if i in not_displayed else 0)
    pulse_count = 0
    pulses = [1,2,4,5,7,8,10,11,13,14,16,17,19,20]
    prev_state = zero_cross.value()
    
    while not button.value():
        current_state = zero_cross.value()
        if current_state != prev_state:
            pulse_count = (pulse_count + 1) % 20
            if pulse_count in pulses:
                send_pulses()
        prev_state = current_state
    

def state8():
    not_displayed = [16]
    for i in range(12, 20):
        output_pins[i].value(1 if i in not_displayed else 0)
    pulse_count = 0
    pulses = [1,2,4,5,6,7,9,10,11,12,14,15,16,17,19,20]
    prev_state = zero_cross.value()
    
    while not button.value():
        current_state = zero_cross.value()
        if current_state != prev_state:
            pulse_count = (pulse_count + 1) % 20
            if pulse_count in pulses:
                send_pulses()
        prev_state = current_state
    

def state9():
    not_displayed = [16, 18, 19]
    for i in range(12, 20):
        output_pins[i].value(1 if i in not_displayed else 0)
    pulse_count = 0
    pulses = list(range(1, 21))
    prev_state = zero_cross.value()
    
    while not button.value():
        current_state = zero_cross.value()
        if current_state != prev_state:
            pulse_count = (pulse_count + 1) % 20
            if pulse_count in pulses:
                send_pulses()
        prev_state = current_state
    

def send_pulses():
    triac_out.value(1)
    time.sleep(0.001)
    triac_out.value(0)

states = [state0, state1, state2, state3, state4, state5, state6, state7, state8, state9]

state_index = 0
display_on = False
led.value(1)
time.sleep(1)
led.value(0)
timeout_time = time.time()
while True:
    if time.time() - timeout_time >= 30:
        state_index = 0
        states[state_index]()
    if button.value() == 1 or button_sim == 1:
        timeout_time = time.time()
        button_sim = 0
        start_time = time.time()
        while button.value() == 1:
            if time.time() - start_time > 1 and display_on == True:
                turn_off()
                state_index = 0
                display_on = False
                for _ in range(3):
                    buzzer.duty_u16(int(0.5 * 65535))
                    time.sleep(0.5)
                    buzzer.duty_u16(0)
                    time.sleep(0.5)
                time.sleep(1)
                break
            elif time.time() - start_time > 1 and display_on == False:
                display_on = True
                states[state_index]()
                state_index = (state_index + 1) % len(states)
                time.sleep(1)
                break

        else:
            if display_on == True:
                states[state_index]()
                time.sleep(0.3)
                state_index = (state_index + 1) % len(states)
                if state_index != 1:
                    button_sim = 1
                




