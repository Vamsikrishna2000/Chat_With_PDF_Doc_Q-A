Project Name: Conversational PDF Chatbot with LangChain and Gemini Pro

Description:

This project builds a user-friendly Streamlit application that allows you to interact with your PDFs through a conversational interface. By leveraging the capabilities of LangChain, Gemini Pro's powerful LLM model, and vector search techniques, you can ask questions, filter information, and gain insights from your PDFs in a natural and interactive way.

Key Technologies:

Streamlit: Streamlines front-end development for creating interactive web apps.
PyPDF2: Extracts text content from PDF documents.
LangChain:
  RecursiveCharacterTextSplitter: Splits large text into manageable chunks for processing.
  GoogleGenerativeAIEmbeddings: Generates vector representations of text using a pre-trained Google Generative AI model.
  FAISS: Enables efficient vector search to retrieve relevant information from PDFs.
  ChatGoogleGenerativeAI: Interacts with the Gemini Pro LLM model for question answering.
  load_qa_chain: Constructs a question-answering chain using the specified model and prompt.
  PromptTemplate: Defines a structured format for prompts sent to the LLM.
dotenv: Loads environment variables from a .env file to securely store API keys
