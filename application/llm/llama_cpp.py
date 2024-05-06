from application.llm.base import BaseLLM
from application.core.settings import settings


class LlamaCpp(BaseLLM):

    def __init__(
        self,
        api_key=None,
        user_api_key=None,
        llm_name=settings.MODEL_PATH,
        *args,
        **kwargs,
    ):
        global llama
        try:
            from llama_cpp import Llama
        except ImportError:
            raise ImportError(
                "Please install llama_cpp using pip install llama-cpp-python"
            )

        super().__init__(*args, **kwargs)
        self.api_key = api_key
        self.user_api_key = user_api_key
        llama = Llama(model_path=llm_name, n_ctx=2048)

    def _raw_gen(self, baseself, model, messages, stream=False, **kwargs):
        context = messages[0]["content"]
        user_question = messages[-1]["content"]
        prompt = f"### Instruction \n {user_question} \n ### Context \n {context} \n ### Answer \n"

        result = llama(prompt, max_tokens=150, echo=False)

        # import sys
        # print(result['choices'][0]['text'].split('### Answer \n')[-1], file=sys.stderr)

        return result["choices"][0]["text"].split("### Answer \n")[-1]

    def _raw_gen_stream(self, baseself, model, messages, stream=True, **kwargs):
        context = messages[0]["content"]
        user_question = messages[-1]["content"]
        prompt = f"### Instruction \n {user_question} \n ### Context \n {context} \n ### Answer \n"

        result = llama(prompt, max_tokens=150, echo=False, stream=stream)

        # import sys
        # print(list(result), file=sys.stderr)

        for item in result:
            for choice in item["choices"]:
                yield choice["text"]