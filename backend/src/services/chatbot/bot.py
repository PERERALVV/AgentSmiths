# from PromptRetriver import *
from src.routes.llm import *
from src.database.vecDB import *
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser



# def bot_with_chat_history_v3(user_input):
#     retriever = getDB().as_retriever()
#     prompt = getprompt()
#     # llm = gemini_chat(0.1)
#     llm=Ggemini()

#     def format_docs(docs):
#         return "\n\n".join(doc.page_content for doc in docs)

#     rag_chain = (
#         {"context": retriever | format_docs, "question": RunnablePassthrough()}
#         | prompt
#         # | llm
#         # | StrOutputParser()
#     )
#     def update_hist(question):
#         if len(chat_history) == 0:
#             return question
#         contextualize_q_system_prompt = """Given a chat history and the latest user question \
#         which might reference context in the chat history, formulate a standalone question \
#         which can be understood without the chat history. Do NOT answer the question, \
#         just reformulate it if needed and otherwise return it as is.
#         chat history:{chat_history}
#         question:{question}
#         """
#         p=ChatPromptTemplate.from_template(contextualize_q_system_prompt)
#         return llm.chatGemini(p.invoke({"chat_history": chat_history, "question": question}).messages[0].content)
    
#     # while True:
#     #     user_input = input("user: ")
#     #     if user_input.lower() == "quit":
#     #         break
#     #     question = update_hist(user_input)
#     #     response = rag_chain.invoke(question)
#     #     output=llm.chatGemini(response.messages[0].content)
#     #     print("chatbot: ", output)
#     #     chat_history.extend([HumanMessage(content=user_input), output])

#     question = update_hist(user_input)
#     response = rag_chain.invoke(question)
#     output=llm.chatGemini(response.messages[0].content)
#     # print("chatbot: ", output)
#     chat_history.extend([HumanMessage(content=user_input), output])
#     return output
class chatbot:
    def __init__(self,sid):
        self.chat_history = []
        self.sid=sid
    def bot_chat(self,user_input):
        retriever = getDB().as_retriever()
        llm = groq_chat()

        def format_docs(docs):
            # print("\n\n".join(doc.page_content for doc in docs))
            return "\n\n".join(doc.page_content for doc in docs)
        


        contextualize_q_system_prompt = """Given a chat history and the latest user question \
        which might reference context in the chat history, formulate a standalone question \
        which can be understood without the chat history. Do NOT answer the question, \
        just reformulate it if needed and otherwise return it as is."""
        contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualize_q_system_prompt),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}"),
            ]
        )
        contextualize_q_chain = contextualize_q_prompt | llm | StrOutputParser()


        qa_system_prompt = """You are an assistant for question-answering tasks who answers the questions only based on the context.\
            Use the following pieces of retrieved context to answer the question.\
                If you don't know the answer, just say "please ask something that is relevant".\
                    Use three sentences maximum and keep the answer concise.\
                        ***important:do not answer anything outside of context*** .\

        {context}"""
        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", qa_system_prompt),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}"),
            ]
        )


        def contextualized_question(input: dict):
            if input.get("chat_history"):
                return contextualize_q_chain
            else:
                return input["question"]


        rag_chain = (
            RunnablePassthrough.assign(
                context=contextualized_question | retriever | format_docs
            )
            | qa_prompt
            | llm
        )
        
        response = rag_chain.invoke(
            {"question": user_input, "chat_history": self.chat_history})
        self.chat_history.extend([HumanMessage(content=user_input), response])
        return response.content

    def bot_init(self):
        self.chat_history=[]


if __name__ == "__main__":
    chat_history = []