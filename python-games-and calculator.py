# ====================================== Basic calculator

num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(round(num1 + num2))
elif operator == "-":
    print(round(num1 - num2))
elif operator == "/":
    print(round(num1 / num2))
elif operator == "*":
    print(round(num1 * num2))
else:
    print("Invalid operator")
# ==========================================Guessing game================
secrete = "woooo"
guesses = ""
num_guess = 0
guess_limit = 3
out_of_guesses = False

while guesses != secrete and not (out_of_guesses):
    if num_guess < guess_limit:
        guesses = input("enter guess")
        num_guess += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Too Many Guesses. You lose HAHAHAHHAHAHHAHAHHAHAHA!!!!!!!!!!!!!!!!!")
else:
    print("You win!")
# =========================BASIC TRANSLATION USING FOR LOOPS AND IF STATEMENTS
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                # IF THE WORD IS IN UPPERCASE THEN DO THIS
                translation = translation + "G"
            else:
                # ELSE DO THIS
                translation = translation + "g"
        else:
            translation = translation + letter

    return translation


print(translate(input("Enter a Phrase: ")))
