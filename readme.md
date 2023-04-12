# OpenAI on Azure - Bring Your Own Data

This repo demonstrates how to use [LlamaIndex](https://gpt-index.readthedocs.io/en/latest/index.html) to interrogate custom data sources with OpenAI LLMs running on Microsoft Azure.

Specifically, it uses [SimpleDirectoryReader](https://llamahub.ai/l/file) to extract text from PDFs, Word documents, etc. in a local directory to use as prompt context for LLM queries. A [custom class implementation](./azure_openai.py) routes query requests to a [provisioned OpenAI endpoint in Azure](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview).

The advantage of this approach is that LlamaIndex and its [ecosystem of data integrations](https://llamahub.ai/) abstracts the details of pulling data from custom sources and including it in query prompts appropriate for a given model. Data from [multiple custom sources](https://gpt-index.readthedocs.io/en/latest/use_cases/queries.html#synthesis-over-heterogenous-data) can be queried together, and [new data sources](https://gpt-index.readthedocs.io/en/latest/how_to/customization/custom_llms.html) can be easily integrated.

Note that LlamaIndex uses a technique called [in-context learning](https://medium.com/@atmabodha/pre-training-fine-tuning-and-in-context-learning-in-large-language-models-llms-dd483707b122), which injects additional context into LLM prompts to answer questions specific to your custom data source. Azure OpenAI Service also supports another approach called [model fine-tuning](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/fine-tuning?pivots=programming-language-python), which typically improves model performance and reduces cost and latency.

## Prerequisites

- [VS Code](https://code.visualstudio.com/download) and the [Remote Development Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (for devcontainer support)

- A Microsoft Azure account and subscription (signup for free [here](https://azure.microsoft.com/en-us/free/))

- Access to OpenAI on Azure (currently requires additional [signup](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview#how-do-i-get-access-to-azure-openai))

## Instructions

1. Clone this repo to a local folder. Open the folder (as a devcontainer) in VS Code.

1. Once you have access to OpenAI on Azure, [create a new OpenAI resource](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource).

1. [Deploy](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#deploy-a-model) a 'text-davinci-003' model to your OpenAI resource.

1. Copy [template.env](./template.env) into a new file called '.env'. Update the API_BASE and API_KEY values using those [found in the Azure portal](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/chatgpt-quickstart?tabs=command-line&pivots=programming-language-python#retrieve-key-and-endpoint) for your provisioned OpenAI resource. For API_VERSION use '2023-03-15-preview'. For DEPLOYMENT_NAME use the name of the model you deployed in the previous step.

1. Copy one or more PDF or DOCX files into the [data](./data/) folder. These are the custom data sources you'll be querying using your OpenAI model.

1. Open [main.ipynb](./main.ipynb) and update the text "YOUR CUSTOM PROMPT" with a query relevant to your source documents. For example, if you've included several project overview documents, try asking for a list of all technologies referenced within them, etc.

1. Run the notebooks cells in [main.ipynb](./main.ipynb) in order to invoke your deployed LLM in Azure. Output of the last cell should show the result of your custom query.

## Ideas for Next Steps

1. Try adjusting the temperature of your model, to see how results change

1. Use LlamaIndex to query information in a SQL database

1. Write a LlamaIndex integration for your own custom REST API

1. Use OpenAI on Azure to fine-tune your model and eliminate the need for LlamaIndex entirely
