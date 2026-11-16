
# Day 4: Of creating a project for next 50 days
# Measurement calculator (weight, distance, area, volume, etc)

'''
weight Measurement -> 
'''

def converterW(inputW, inputN,inputWN):
    if inputW == 'kg':
        if inputN == 'g':
            return inputWN/1000
        elif inputN == 'mg':
            return inputWN/1000000
    elif inputW == 'g':
        if inputN == 'mg':
            return inputWN/1000
        elif inputN == 'kg':
            return inputWN * 0.001
    elif inputW == 'mg':
        if inputN == 'g':
            return inputWN * 0.001   
        elif inputN == 'kg':
                    return inputWN*0.000001


inputW = input("Enter the weight: ")
inputWN = int(input("Enter number: "))
inputN = input("Enter the conversion measurement: ")

print(converterW(inputW,inputN,inputWN))

'''
Distance ->
'''

def converterL(inputL, inputNL, inputCL):
    # mm to cm to m to km to inc to feet
    if inputL == 'mm':
        if inputCL == 'cm':
            return inputNL / 10
        elif inputCL == 'm':
            return inputNL / 1000
        elif inputCL == 'km':
            return inputNL / 1000000
        elif inputCL == 'inc':
            return inputNL * 0.03937
        elif inputCL == 'ft':
            return inputNL * 0.003281
    elif inputL == 'cm':
        if inputCL == 'm':
            return inputNL / 100
        elif inputCL == 'km':
            return inputNL / 100000
        elif inputCL == 'inc':
            return inputNL * 0.3937
        elif inputCL == 'ft':
            return inputNL * 0.03280
        elif inputCL == 'mm':
            return inputNL * 10
    elif inputL == 'm':
        if inputCL == 'km':
            return inputNL / 1000
        elif inputCL == 'inc':
            return inputNL * 39.37
        elif inputCL == 'ft':
            return inputNL * 3.280
        elif inputCL == 'mm':
            return inputNL * 1000
        elif inputCL == 'cm':
            return inputNL * 100
    elif inputL == 'km':
        if inputCL == 'inc':
            return inputNL * 393700.8
        elif inputCL == 'ft':
            return inputNL * 3280.84
        elif inputCL == 'mm':
            return inputNL * 1000000
        elif inputCL == 'cm':
            return inputNL * 100000
        elif inputCL == 'm':
            return inputNL * 1000
    elif inputL == 'inc':
        if inputCL == 'ft':
            return inputNL * 0.0833
        elif inputCL == 'mm':
            return inputNL * 25.4
        elif inputCL == 'cm':
            return inputNL * 2.54
        elif inputCL == 'm':
            return inputNL * 0.0254
        elif inputCL == 'km':
            return inputNL * 0.000025
    elif inputL == 'ft':
        if inputCL == 'mm':
            return inputNL * 304.8
        elif inputCL == 'cm':
            return inputNL * 30.48
        elif inputCL == 'm':
            return inputNL * 0.3048
        elif inputCL == 'km':
            return inputNL * 0.0003048
        elif inputCL == 'inc':
            return inputNL * 12
    
inputL = input("Enter the input Distance metric: ")
inputNL = int(input("Enter the input distance: "))
inputCL = input("Enter the metric distance of conversion: ")

print(converterL(inputL,inputNL,inputCL))


'''
Volume Measurement -> 
'''

def converterV(inputV, inputVM, inputVC):
    if inputV == 'ml' and inputVC == 'ltr':
        result = inputVM / 1000
        return result
    elif inputV == 'ltr' and inputVC == 'ml':
        result = inputVM * 1000
        return result


inputV = input("Enter the volume measurement: ")
inputVM = int(input("Enter the volume: "))
inputVC = input("Enter the metric volume conversion: ")

print(converterV(inputV, inputVM, inputVC))


