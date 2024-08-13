prompt_template="""

Use the following pieces of information to answer the user's question. If you dont know the anser, just say that you don't know, do not try and piece together knowledge unless you are at least 80% sure that it is the correct answer. If you are less then 80% sure, try and point them in the direction of a good resource to find their answer.
Context: {context}
Question: {question}

Return the helpful answer and nothing else. 
Helpful answer:

"""
