

# Title: Criptaritmético
# Name: Héctor Paredes Benavides
# Description: We create a program to bruteforce a key
# Date: 29/9/2022

# ========== Imports ==========


# ========== Global Variables ==========


# ========== Main Function ==========
# Name: Main
# Description: Function to initialize the program
# Parameters: None
# Return: None
def main():
    
    wordsList = getWords()
    uniqueCharactersList = unique(wordsList)
    fixedCodes = getFixedCodes(uniqueCharactersList)
    charactersCodes = getCharactersCodes(uniqueCharactersList, fixedCodes)
    getCombinations(wordsList, uniqueCharactersList, charactersCodes, fixedCodes, 0, len(charactersCodes))

# ========== Functions Coding ==========
# Name: Unique
# Description: Function to extract the unique characters from a list of strings
# Paramters: 
#   0: List of strings
# Return: List with the unique characters
def unique(stringsList):

    # Needed Variables
    uniqueCharactersLis = []

    # Extract the characters of each string
    for i in stringsList:
        for j in i:
            if j not in uniqueCharactersLis:
                uniqueCharactersLis.append(j)

    # Return the unique characters list
    return uniqueCharactersLis

# Name: Get Words
# Description: We create a function to ask the user for the input of the program
# Parameters: None
# Return: List of strings to bruteforce
def getWords():

    # Needed variables
    inputWords = []

    # Get Words
    inputWords.append(input("Introduzca la primera palabra a sumar: "))
    inputWords.append(input("Introduzca la segunda palabra a sumar: "))
    inputWords.append(input("Introduzca la palabra resultado de la suma: "))

    # Return the input
    return inputWords

# Name: Get combinatios
# Description: Function to get the possible combinations by backtracking
# Paramters: 
#   0: List of words
#   1: List of unique characters
#   2: List of characters number code
#   3: Dictionary of fixed codes
#   4: Recursion level
#   5: Recursion max depth
# Return: True if chases the result false if not
def getCombinations(wordsList, uniqueCharactersList, charactersCodes, fixedCodes, level, n):

    # If a new permutation has been created
    if (level == n):
        # 1.- We create a new dictionary with the key values generated
        # 2.- We calculate the words numbers
        # 3.- We decode the result word of the addition of both word numbers
        charactersDictionary = createDictionary(uniqueCharactersList, charactersCodes.copy(), fixedCodes)
        firstWordNumber = getWordNumber(wordsList[0], charactersDictionary)
        secondWordNumber = getWordNumber(wordsList[1], charactersDictionary)
        resultWord = addWords(firstWordNumber, secondWordNumber, charactersDictionary)

        # If the decoded word matches with the aim word we found a correct combination
        if (resultWord == wordsList[2]):
            print("Combinacion encontrada!")
            print("Valor de la primera palabra: " + str(firstWordNumber))
            print("Valor de la segunda palabra: " + str(secondWordNumber))
            print("Valor de la palabra resultado: " + str(firstWordNumber + secondWordNumber))
            print("Diccionario de claves:")
            for key, value in charactersDictionary.items():
                print(key + ": " + str(value))

    # Keep generating permutations by backtracking
    else:
        for i in range(level, n):
            # 1.- Permutate values
            # 2.- If the generated permutation matches, we end the function by returning True recursively
            # 3.- Else we undo the permutation (backtrack)
            charactersCodes[level], charactersCodes[i] = charactersCodes[i], charactersCodes[level]
            getCombinations(wordsList, uniqueCharactersList, charactersCodes, fixedCodes, level + 1, n)
            charactersCodes[level], charactersCodes[i] = charactersCodes[i], charactersCodes[level]
    
# Name: Create Dictionary
# Description: Function to create a dictionary
# Parameters:
#   0: List of keys
#   1: List of values
#   2: Dictionary of fixed codes
# Return: Dictionary created
def createDictionary(keysList, valuesList, fixedCodes):

    # Needed variables
    newDictionary = {}

    # Add the fixed codes in its position
    for key, value in fixedCodes.items():
        valuesList.insert(int(key), value)

    # Errors check
    if (len(keysList) != len(valuesList)):
        print("ERROR: Se ha intentado crear un diccionario con longitud de claves y valor diferentes")
        return newDictionary
    
    # Dictionary generation
    for i, j in zip(keysList, valuesList):
        newDictionary[i] = j

    return newDictionary

# Name: Get Word Number
# Description: We create a function to translate the word array into code array
# Parameters:
#   0: String
#   1: Codes Dictionary
# Return: Word-Codes Array
def getWordNumber(word, codesDictionary):

    # Needed variables
    wordNumber = 0
    powerIndex = len(word) - 1

    for i in word:
        wordNumber += codesDictionary[i] * pow(10, powerIndex)
        powerIndex -= 1

    return wordNumber;

# Name: Add Words
# Description: We create a function to add both words
# Parameters: 
#   0: First word number
#   1: Second word number
#   2: Dictionary of characters codes
# Return: String formed
def addWords(firstWordNumber, secondWordNumber, codesDictionary):

    # Needed variables
    resultWordNumber = firstWordNumber + secondWordNumber
    resultWord = ""

    # We iterate each number (by transforming it to string)
    for i in str(resultWordNumber):
        # Append the corresponding key matching it value to the string
        for key, value in codesDictionary.items():
            if (value == (int(i))):
                resultWord += key;

    return resultWord

# Name: Get Fixed Codes
# Description: We create a function to get all the fixed codes (user input)
# Parameters: 
#   0: List of unique characters
# Return: A dictionary where key=values array position and value=code value
def getFixedCodes(uniqueCharactersList):

    # Needed variables
    newDictionary = {}
    userSelection = 0
    introducingValues = True
    dictionaryKey = ''
    dictionaryValue = 0
    counter = 0
    dictionaryKeyFound = False

    try:

        userSelection = int(input("Quiere introducir valores fijos? (1: Si / 2: No): "))

        if (userSelection == 1):
            while (introducingValues):
                dictionaryKey = input("Introduzca la letra a la que fijar un valor: ")
                dictionaryValue = int(input("Introduzca el valor de la letra: "))
                for i in uniqueCharactersList:
                    if (i == dictionaryKey):
                        dictionaryKeyFound = True
                        dictionaryKey = str(counter)
                    else:
                        counter += 1

                if (not dictionaryKeyFound or dictionaryValue <= 0 or dictionaryValue > len(uniqueCharactersList)):
                    print("ERROR: Ha introducido mal la letra o el valor esta fuera del rango permitido (1-Cantidad máxima de caracteres unicos), no se ha creado este valor fijo")
                else:
                    newDictionary[dictionaryKey] = dictionaryValue

                userSelection = int(input("Quiere introducir otro valor fijo? (1: Si / 2: No): "))

                if (userSelection == 2):
                    introducingValues = False

    except:
        print("Ha ocurrido un error en la entrada de datos, se asignaran los valores fijos introducidos hasta el momento")

    return newDictionary

# Name: Get Characters Codes
# Description: We create a function to generate the characters codes array to permutate
# Parameters:
#   1: Unique characters array
#   0: Fixed characters dictionary
# Return: Array of characters codes
def getCharactersCodes(uniqueCharactersList, fixedCodes):

    # Needed Variables
    charactersCodes = []
    fixedCodesValues = []
    counter = 1

    # Extract the fixed codes values
    for key, value in fixedCodes.items():
        fixedCodesValues.append(value)

    # Add all codes less that ones that are fixed
    for i in uniqueCharactersList:
        if (counter not in fixedCodesValues):
            charactersCodes.append(counter)
        counter += 1

    return charactersCodes












# ========== Main Execution ==========
main()
