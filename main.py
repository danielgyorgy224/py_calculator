from pyscript import document
    
def delete(event):
    document.querySelector("#number1").value = ""
    document.querySelector("#number2").value = ""
    document.querySelector("#operator").selectedIndex = 0
    document.querySelector("#result").innerText = ""

def calculate(event):
    n1 = float(document.querySelector("#number1").value)
    op = document.querySelector("#operator").value
    n2 = float(document.querySelector("#number2").value)
    if op == "+":
        result = n1+n2
    elif op == "-":
        result = n1-n2
    elif op == "*":
        result = n1*n2
    elif op == "/":
        result = n1/n2
    document.querySelector("#result").innerText = f"{n1} {op} {n2} = {result}"