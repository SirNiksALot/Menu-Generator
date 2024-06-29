import os

os.environ["AI21_API_KEY"] = "wcAttkCoVaeDDQi8z2pu05Hezjj96UT1"

from langchain_ai21 import AI21LLM
from langchain_core.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain


def get_response(cuisine):
    model = AI21LLM(model="j2-ultra")
    
    template1=PromptTemplate(
        input_variables=["cuisine"],
        template="Suggest only a name for a {cuisine} cuisine restaurant"
    )
    chain1=LLMChain(llm=model,prompt=template1,output_key="restaurant_name")

    template2=PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest 5 menu item names only for a restaurant named {restaurant_name}"
    )
    chain2=LLMChain(llm=model,prompt=template2,output_key="menu_items")
    
    chain = SequentialChain(
    chains = [chain1, chain2],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name', "menu_items"]
    )

    response=chain({"cuisine":cuisine})
    return response