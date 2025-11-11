import time

test_list = ["wa", "wed", "wrfs", "wqa", "w"]
start = time.time()
repeating_inputs = []
counter = 0
for current_input in test_list:
    counter += 1
    #print("Processing input number " + str(counter))
    if current_input != repeating_inputs:
        input_list = []
        if len(current_input) > 1:
            for x in current_input:
                input_list.append(x)
            current_input = input_list
        else: 
            current_input = [current_input]
        #print(current_input)
        for x in current_input:
            if x not in repeating_inputs:
                repeating_inputs.append(x)
                print(str(x) + " pressed")
        for x in repeating_inputs.copy():
            if x not in current_input:
                repeating_inputs.remove(x)
                print(str(x) + " released")
    #print(repeating_inputs)

end = time.time()
print(f"Time taken to run the code was {(end-start)*1000000} microseconds")