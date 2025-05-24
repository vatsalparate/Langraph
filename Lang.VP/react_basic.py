from langcahain_google_genai import ChatgoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv
llm = ChatgoogleGenerativeAI(model="gemini-1.5-pro")
result = llm.invoke("give me a fact about cats")
print(results)
