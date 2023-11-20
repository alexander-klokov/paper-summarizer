from langchain.prompts import PromptTemplate

map_prompt = """
    Write a concise summary of the following:
    "{text}"
    CONCISE SUMMARY:
"""
map_prompt_template = PromptTemplate(template=map_prompt, input_variables=["text"])

combine_prompt = """
    Write a concise summary of the following text delimited by triple backquotes.
    Return your response in bullet points which covers the key points of the text.
    ```{text}```
    BULLET POINT SUMMARY:

    """
combine_prompt_template = PromptTemplate(template=combine_prompt, input_variables=["text"])