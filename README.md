# Menu-Generator-
This is a stream-lit deployed website that generates Menu Items for you if the cuisine is inputted . It used Lang-chain and the LLM from AI21 labs 

Working:
It utilizes the LangChain library along with AI21's language model to create a dynamic response generating a restaurant name and menu items based on a specified cuisine type. Here's a detailed summary:

Environment Setup:

It sets the AI21 API key as an environment variable to authenticate requests to the AI21 service.
Function Definition:

The main function, get_response, accepts a cuisine type as input and orchestrates the sequence of prompts.
Model Initialization:

The AI21 language model (j2-ultra) is instantiated to handle the natural language processing tasks.
Prompt Templates:

First Prompt: A template is created to ask the language model for a restaurant name based on the provided cuisine. This is implemented using PromptTemplate and linked to the model with LLMChain.
Second Prompt: Another template is set up to request five menu item names based on the generated restaurant name. This also uses PromptTemplate and LLMChain.
Sequential Execution:

The two chains (one for the restaurant name and one for the menu items) are combined into a SequentialChain. This ensures that the output of the first prompt (restaurant name) becomes the input for the second prompt.
Generating Response:

When the function is called with a specific cuisine type, the sequential chain executes the prompts in order, generating a coherent restaurant name and corresponding menu items.
Usage Example:
To use this function, call get_response
