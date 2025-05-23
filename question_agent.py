import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(model="gpt-4o-mini", max_tokens=1000, temperature=0)

template = """
You are a helpful AI assistant. Your task is to answer the user's question to the best of your ability.

User's question: {question}

Please provide a clear and concise answer:
"""

prompt = PromptTemplate(template=template, input_variables=["question"])

qa_chain = prompt | llm

def get_answer(question):
    """
    Get an answer to the given question using the QA chain.
    """
    input_variables = {"question": question}
    response = qa_chain.invoke(input_variables).content
    return response

if __name__ == "__main__":
    try:
        user_question = input("Enter your question: ")
        user_answer = get_answer(user_question)
        print("\n--- Answer ---")
        print(user_answer)
    except Exception as e:
        print(f"An error occurred: {e}")