from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import load_tools, initialize_agent, AgentType

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.8, model="gpt-3.5-turbo-instruct",)
    prompt_template_name = PromptTemplate(
        template="I have a {animal_type} pet, and I want a cool name for it, it is {pet_color} in color.suggest me five names for my pet",
        input_variables = ["animal_type", "pet_color"]
    )

    name_chain = LLMChain(llm=llm, prompt= prompt_template_name, output_key="pet names")
    response = name_chain({"animal_type": animal_type, "pet_color": pet_color})

    return response['pet names']


def langchain_agents():
    llm = OpenAI(temperature=0.5, model="gpt-3.5-turbo-instruct",)
    tools = load_tools(['wikipedia', 'llm-math'], llm=llm)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True )
    result = agent.run(
        "What is the average age of a dog? Multiply the age by 3"
    )
    print(result)
if __name__ == "__main__":
    # print(generate_pet_name("cow", "brown"))
    langchain_agents()