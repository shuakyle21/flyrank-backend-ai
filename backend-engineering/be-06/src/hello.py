from http.client import responses

from openai import OpenAI
from openai.types.shared_params import ResponseFormatJSONObject
from openai.types.chat import ChatCompletionUserMessageParam

from src.llm.config import get_settings
cfg = get_settings()

client = OpenAI(
    base_url=str(cfg.llm_base_url),
    api_key=cfg.llm_api_key,
)

messages: list[ChatCompletionUserMessageParam] = [
    {"role": "user", "content": "Reply with exactly the word: ready"}
]
response_format: ResponseFormatJSONObject = {"type":"json_object"}

res = client.chat.completions.create(
    model=cfg.llm_model,
    messages=messages,
    temperature=0,
    response_format = response_format,
    extra_body={"provider": {"require_parameters": True}}
)
print(res.choices[0].message.content)
