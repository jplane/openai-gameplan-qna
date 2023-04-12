
from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any
import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_type = "azure"
openai.api_base = config["API_BASE"]
openai.api_version = config["API_VERSION"]
openai.api_key = config["API_KEY"]

deployment_name = config["DEPLOYMENT_NAME"]

class AzureOpenAiLLM(LLM):

    max_tokens:int

    temp: int = 0

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:

        try:
            # Create a completion for the provided prompt and parameters
            # To know more about the parameters, checkout this documentation: https://learn.microsoft.com/en-us/azure/cognitive-services/openai/reference
            completion = openai.Completion.create(
                            prompt=prompt,
                            temperature=self.temp,
                            max_tokens=self.max_tokens,
                            engine=deployment_name)
            
            # Here indicating if the response is filtered
            if completion.choices[0].finish_reason == "content_filter": # type: ignore
                raise RuntimeError("The generated content is filtered.")

            return completion.choices[0].text.strip(" \n") # type: ignore

        except openai.error.APIError as e: # type: ignore
            # Handle API error here, e.g. retry or log
            raise RuntimeError(f"OpenAI API returned an API Error: {e}")

        except openai.error.AuthenticationError as e: # type: ignore
            # Handle Authentication error here, e.g. invalid API key
            raise RuntimeError(f"OpenAI API returned an Authentication Error: {e}")

        except openai.error.APIConnectionError as e: # type: ignore
            # Handle connection error here
            raise RuntimeError(f"Failed to connect to OpenAI API: {e}")

        except openai.error.InvalidRequestError as e: # type: ignore
            # Handle connection error here
            raise RuntimeError(f"Invalid Request Error: {e}")

        except openai.error.RateLimitError as e: # type: ignore
            # Handle rate limit error
            raise RuntimeError(f"OpenAI API request exceeded rate limit: {e}")

        except openai.error.ServiceUnavailableError as e: # type: ignore
            # Handle Service Unavailable error
            raise RuntimeError(f"Service Unavailable: {e}")

        except openai.error.Timeout as e: # type: ignore
            # Handle request timeout
            raise RuntimeError(f"Request timed out: {e}")
        
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"name_of_model": config["DEPLOYMENT_NAME"]}

    @property
    def _llm_type(self) -> str:
        return "custom"
