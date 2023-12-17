from server.settings.components import config

LLM_MODEL_URL_FOR_GENERATE_MARKETING_TEXT = config(
    'LLM_MODEL_URL_FOR_GENERATE_MARKETING_TEXT',
    default='http://llama:8000/v1/chat/completions'
)


LLM_MODEL_SYSTEM_CONTENT_FOR_GENERATE_MARKETING_TEXT = config(
    'LLM_MODEL_SYSTEM_CONTENT_FOR_GENERATE_MARKETING_TEXT',
    default='Все ответы должны быть на русском.'
)


LLM_MODEL_USER_CONTENT_FOR_GENERATE_MARKETING_TEXT = config(
    'LLM_MODEL_USER_CONTENT_FOR_GENERATE_MARKETING_TEXT',
    default='',
)

