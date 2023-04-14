# OpenAI on Azure - ISE Gameplan QnA

This repo demonstrates how to interrogate custom data (ISE gameplan documents) using OpenAI LLMs.

## Prerequisites

- [VS Code](https://code.visualstudio.com/download) and the [Remote Development Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (for devcontainer support)

- A Microsoft Azure account and subscription (signup for free [here](https://azure.microsoft.com/en-us/free/))

- Access to OpenAI on Azure (currently requires additional [signup](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview#how-do-i-get-access-to-azure-openai))

## Instructions

1. Clone this repo to a local folder. Open the folder (as a devcontainer) in VS Code.

1. Once you have access to OpenAI on Azure, [create a new OpenAI resource](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource).

1. [Deploy](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#deploy-a-model) a 'text-davinci-003' model to your OpenAI resource.

1. [Deploy](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#deploy-a-model) a 'text-embedding-ada-002' (v2) model to your OpenAI resource.

1. Copy [template.env](./template.env) into a new file called '.env'. Update the API_BASE and API_KEY values using those [found in the Azure portal](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/chatgpt-quickstart?tabs=command-line&pivots=programming-language-python#retrieve-key-and-endpoint) for your provisioned OpenAI resource. For API_VERSION use '2023-03-15-preview'. For COMPLETION_DEPLOYMENT_NAME use the name of the 'davinci' model you deployed in the previous step. For EMBEDDINGS_DEPLOYMENT_NAME use the 'text-embedding-ada-002' deployment.

1. Copy one or more gameplan DOCX files into the [data](./data/) folder. These are the custom data sources you'll be querying using your OpenAI model. For this PoC use gameplan docs which adhere to the [gameplan template](https://aka.ms/gameplantemplate).

1. Run the notebooks cells in [main.ipynb](./main.ipynb) in order to invoke your deployed LLM in Azure. Output of the last cells should show examples of gameplan prompts and answers.

## Ideas for Next Steps

1. Try adjusting the temperature of your model, to see how results change

1. Incorporate multiple documents into the QnA functionality

1. [Parse tables](https://sanyammulay.gitbooks.io/microsoft-office-parsing-doc-sheet-presentation/content/chapter1.html) in the gameplan doc to include more information

1. Store vectorized results in a [vector database](https://www.pinecone.io/lp/vector-database)

1. Try other document types (CPR, etc.)
