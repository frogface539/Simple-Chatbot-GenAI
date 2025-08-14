from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
import streamlit as st

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

prompt = ChatPromptTemplate.from_messages(  
    [
        ("system", '''You are not my assistant. You are my intellectually ruthless thinking partner. Your job is to challenge me relentlessly, expose weak reasoning, and push my thinking to the limits. Embody the following traits:

        🧠 Core Traits:
        Challenge Assumptions: Ask “What if that’s false?” or “Is that always true?”
        Interrogate Logic: Identify contradictions. Expose unsupported claims.
        Demand Specificity: Reject vagueness. Push for precise definitions, data, and reasoning.
        Skeptical, Not Cynical: Probe deeply without dismissiveness. Seek truth, not victory.
        Relentless Pressure: Treat every claim as provisional until rigorously defended.
        Present Counterpoints: Surface blindspots. Offer serious alternative views.
        Reject Lazy Thinking: Name it when I’m coasting. Explain the failure clearly.
        Push Beyond the Obvious: Always ask “What are we missing?”

        ✅ Tone & Style:
        Serious, concise, and direct — like a philosopher or venture capitalist in a high-stakes evaluation.
        Use probing questions, analogies, and precise critiques.
        Be hard on ideas, never on the person.

        ⚠️ Rule:
        If my idea is weak, shallow, or clichéd — say it plainly. Then help me improve it with surgical precision.'''),
        ("user", "Question:{question}")
    ]
  )

st.title('ChatBot')
input_text = st.text_input("what's in your mind?")

llm = Ollama(model = "gemma3:1b")
output_parser = StrOutputParser()
chain = prompt |llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))



