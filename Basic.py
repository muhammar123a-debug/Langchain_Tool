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

