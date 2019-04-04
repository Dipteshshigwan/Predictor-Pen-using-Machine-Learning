# Initializing the Serial port to recieve data in version 1

# For this importing pyserial module needs to be installed
import serial

#Function to compare the matrix
def compare(curr_matrix,user_matrix):
    '''
    :param curr_matrix:  Current matrix from arduino readings
    :param user_matrix:  Matrix values stored in database
    :return:  boolean value of True of False for Comparing the two matrices
    '''
    return curr_matrix == user_matrix


ser = serial.Serial()
ser.port = 'COM1'
ser.open()

#Create a matrix to store the incoming data
while True:
    matrix = []
    var  = ser.readline()
    printed_lis = list(var[:-2])
    temp = []

    for i in printed_lis:
        character = str(chr(i))
        temp.append(character)
        
# OUTPUT temp -> ['1', '4', '5', ',', '2', '5', '4'] convert this to [145,254]

    var = ""
    i = 0
    end = False

    while i < len(temp) - 1:
        counter = 0
        temp_array = []
        while counter < 3 and not end:
            # Check if value is , if its , then break here and append var values to temp array
            if temp[i] != ",":
                var += temp[i]
            else:
                counter += 1
                temp_array.append(int(var))
                var = ""
            i += 1
            # Check i value equals to array length if yes then array is finished so thus append last values to temp
            if i == len(temp):
                temp_array.append(int(var))
                end = True
        matrix.append(temp_array)

    # Printing the matrix
    for i in matrix:
        print(i)
    print()

    ### COMPARISON PART###

    # Create matrix for each letter alphabet i.e A, B etc.

    matrix_A = [[144,172,58],[255,178,158],[131,184,146]]
    matrix_B = [[74,144,0],[130,92,220],[174,190,144]]
    matrix_C = [[12,39,14],[57,131,211],[94,72,20]]
    matrix_D = [[211,98,177],[116,232,214],[15,46,55]]

    # form a list of matrices with above matrix as a index
    matrices = [matrix_A, matrix_B, matrix_C, matrix_C]
    # Letter array to keep track of letters
    Letter = ["A","B","C","D"]

    # Loop through each matrix to check if matix matches with anything

    for index, i in enumerate(matrices):
        match = False
        match = compare(i,matrix)
        if match:
            print("Letter is {}.".format(Letter[index]))
            break