# from langchain.tools import tool
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain_google_genai import ChatGoogleGenerativeAI
# import os
# from dotenv import load_dotenv

# # @tool
# # def claculator(expression: str) -> str:
# #     """Solve a basic math expression and return result"""
# #     try:
# #         result = eval(expression)
# #         return str(result)
# #     except Exception as e:
# #         return f"Error: {e}"

# # print(claculator("2+5*3"))
# # print(claculator("100/4"))

# # basic practice
# from langchain.tools import tool
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain_google_genai import ChatGoogleGenerativeAI
# import os
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

# # --------------tool---------------
# @tool
# def calculator(expression: str) -> str:
#     """Solve a basic math expression and return result"""
#     try:
#         result = eval(expression)
#         return str(result)
#     except Exception as e:
#         return f"Error: {e}"

# #-----------------prompt + chain --------------------
# template = """
# You are a helpful assistant.
# User asked: {question}

# If it's a math problem, call the calculator tool.
# Otherwise, just answer in simple words.
# """

# prompt = PromptTemplate(input_variable=["question"], template=template)
# chain = LLMChain(llm=llm, prompt=prompt)

# # ----------------Agent Simulation---------------
# def agent(question):
#     response = chain.run(question)

#     if "calculator" in response.lower():
#         try:
#             expression = "".join([ch for ch in question if ch.isdigit() or ch in "+-*/**."])
#             return f"Tool Used: {calculator(expression)}"
#         except:
#             return "Sorry, calcultor tool failed"
#     else:
#         return response
    
# # ------------------ Test ------------------
# print(agent("What is 25*5?"))
# print(agent("Who is the president of Pakistan?"))

#five task in basic tool
# Step 1: Basic Calculator Tool (LangChain style)
from langchain.tools import tool

@tool
def calculator(expression: str) ->str:
    """Useful for doing basic arithmetic calculations. Input should be a math expression (e.g., 2+2*5)."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)} "

print(calculator.run("2+3*4"))

# Step 2: Word Counter Tool
from langchain.tools import tool

@tool
def word_counter(text: str) -> str:
    """Counter the nnumber of words in the given text."""
    try:
        words = text.split()
        count = len(words)
        return f"Eord Count {count}"
    except Exception as e:
        return f"Error: {str(e)}"

# Tool test karte hain
print(word_counter.run("LangChain makes building LLM applications easier."))

# Step 3: String Reverser Tool

from langchain.tools import tool
@tool
def string_reverse(text: str) -> str:
    """Reverse the given string."""
    try:
        return text[::-1]
    except Exception as e:
        return f"Error: {str(e)}"

print(string_reverse.run("LangChain"))

# Step 4: Translator Tool (Simple Version)

from langchain.tools import tool

#Simple dictionary
eng_to_urdu = {
    "hello": "السلام علیکم",
    "world": "دنیا",
    "good": "اچھا",
    "morning": "صبح",
    "night": "رات"
}

@tool
def Translation(text: str) -> str:
    """Translates simple English words to Urdu using a fixed dictionary"""
    try:
        words = text.lower().split()
        translate = [eng_to_urdu.get(word, word) for word in words]
        return "".join(translate)
    except Exception as e:
        return f"Error: {str(e)}"
    
print(Translation.run("good"))

from langchain.tools import tool

@tool
def file_reader(file_path: str) -> str:
    """Reads a text file and returns  its content"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            connect = f.read()
        return connect
    except Exception as e:
        return f"Error: {str(e)}"

with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("This is a test file.\nLangChain tools are very useful!")

print(file_reader.run("sample.txt"))
