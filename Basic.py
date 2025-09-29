from langchain.tools import tool

@tool
def claculator(expression: str) -> str:
    """Solve a basic math expression and return result"""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

print(claculator("2+5*3"))
print(claculator("100/4"))