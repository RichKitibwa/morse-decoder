import time
import keyboard
import threading
from morse import to_morse_code
from buffer import Buffer

buffer = Buffer()

def process_buffer():
    while True:
        if buffer.has_data():
            char = buffer.get_next()
            morse = to_morse_code(char)
            print("\r\nMorse code: " + morse + "    ", end='', flush=True) 
        time.sleep(2)    

def main():
    threading.Thread(target=process_buffer,daemon=True).start()

    print("Enter input: ")
    input = ''
    while True:
        key = keyboard.read_event()
        if key.event_type == keyboard.KEY_DOWN:
            if key.name == 'enter':
                for char in input:
                    buffer.add(char)
                input = ''
            elif key.name == 'esc':
                break
            else:
                input += key.name
                print(key.name, end='', flush=True)        
    
if __name__ == "__main__":
    main()       
