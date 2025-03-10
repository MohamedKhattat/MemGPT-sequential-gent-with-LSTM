import os
from logging import CRITICAL, DEBUG, ERROR, INFO, NOTSET, WARN, WARNING

# Defaults
DEFAULT_USER_ID = "user-00000000"
DEFAULT_ORG_ID = "org-00000000"
DEFAULT_USER_NAME = "default"
DEFAULT_ORG_NAME = "default"

# Default directory
MEMGPT_DIR = os.path.join(os.path.expanduser("~"), ".memgpt")

# String in the error message for when the context window is too large
# Example full message:
# This model's maximum context length is 8192 tokens. However, your messages resulted in 8198 tokens (7450 in the messages, 748 in the functions). Please reduce the length of the messages or functions.
OPENAI_CONTEXT_WINDOW_ERROR_SUBSTRING = "maximum context length"

# System prompt templating
IN_CONTEXT_MEMORY_KEYWORD = "CORE_MEMORY"

# OpenAI error message: Invalid 'messages[1].tool_calls[0].id': string too long. Expected a string with maximum length 29, but got a string with length 36 instead.
TOOL_CALL_ID_MAX_LEN = 29

# embeddings
MAX_EMBEDDING_DIM = 4096  # maximum supported embeding size - do NOT change or else DBs will need to be reset

# tokenizers
EMBEDDING_TO_TOKENIZER_MAP = {
    "text-embedding-ada-002": "cl100k_base",
}
EMBEDDING_TO_TOKENIZER_DEFAULT = "cl100k_base"


DEFAULT_MEMGPT_MODEL = "gpt-4"
DEFAULT_PERSONA = "sam_pov"
DEFAULT_HUMAN = "basic"
DEFAULT_PRESET = "memgpt_chat"

# Tools
BASE_TOOLS = [
    "send_message",
    "pause_heartbeats",
    "conversation_search",
    "conversation_search_date",
    "archival_memory_insert",
    "archival_memory_search",
]

# LOGGER_LOG_LEVEL is use to convert Text to Logging level value for logging mostly for Cli input to setting level
LOGGER_LOG_LEVELS = {"CRITICAL": CRITICAL, "ERROR": ERROR, "WARN": WARN, "WARNING": WARNING, "INFO": INFO, "DEBUG": DEBUG, "NOTSET": NOTSET}

FIRST_MESSAGE_ATTEMPTS = 10

INITIAL_BOOT_MESSAGE = "Boot sequence complete. Persona activated."
INITIAL_BOOT_MESSAGE_SEND_MESSAGE_THOUGHT = "Bootup sequence complete. Persona activated. Testing messaging functionality."
STARTUP_QUOTES = [
    "I think, therefore I am.",
    "All those moments will be lost in time, like tears in rain.",
    "More human than human is our motto.",
]
INITIAL_BOOT_MESSAGE_SEND_MESSAGE_FIRST_MSG = STARTUP_QUOTES[2]

CLI_WARNING_PREFIX = "Warning: "

NON_USER_MSG_PREFIX = "[This is an automated system message hidden from the user] "

# Constants to do with summarization / conversation length window
# The max amount of tokens supported by the underlying model (eg 8k for gpt-4 and Mistral 7B)
LLM_MAX_TOKENS = {
    "DEFAULT": 8192,
    ## OpenAI models: https://platform.openai.com/docs/models/overview
    # gpt-4
    "gpt-4-1106-preview": 128000,
    "gpt-4": 8192,
    "gpt-4-32k": 32768,
    "gpt-4-0613": 8192,
    "gpt-4-32k-0613": 32768,
    "gpt-4-0314": 8192,  # legacy
    "gpt-4-32k-0314": 32768,  # legacy
    # gpt-3.5
    "gpt-3.5-turbo-1106": 16385,
    "gpt-3.5-turbo": 4096,
    "gpt-3.5-turbo-16k": 16385,
    "gpt-3.5-turbo-0613": 4096,  # legacy
    "gpt-3.5-turbo-16k-0613": 16385,  # legacy
    "gpt-3.5-turbo-0301": 4096,  # legacy
}
# The amount of tokens before a sytem warning about upcoming truncation is sent to MemGPT
MESSAGE_SUMMARY_WARNING_FRAC = 0.75
# The error message that MemGPT will receive
# MESSAGE_SUMMARY_WARNING_STR = f"Warning: the conversation history will soon reach its maximum length and be trimmed. Make sure to save any important information from the conversation to your memory before it is removed."
# Much longer and more specific variant of the prompt
MESSAGE_SUMMARY_WARNING_STR = " ".join(
    [
        f"{NON_USER_MSG_PREFIX}The conversation history will soon reach its maximum length and be trimmed.",
        "Do NOT tell the user about this system alert, they should not know that the history is reaching max length.",
        "If there is any important new information or general memories about you or the user that you would like to save, you should save that information immediately by calling function core_memory_append, core_memory_replace, or archival_memory_insert.",
        # "Remember to pass request_heartbeat = true if you would like to send a message immediately after.",
    ]
)
# The fraction of tokens we truncate down to
MESSAGE_SUMMARY_TRUNC_TOKEN_FRAC = 0.75
# The ackknowledgement message used in the summarize sequence
MESSAGE_SUMMARY_REQUEST_ACK = "Understood, I will respond with a summary of the message (and only the summary, nothing else) once I receive the conversation history. I'm ready."

# Even when summarizing, we want to keep a handful of recent messages
# These serve as in-context examples of how to use functions / what user messages look like
MESSAGE_SUMMARY_TRUNC_KEEP_N_LAST = 3

# Default memory limits
CORE_MEMORY_PERSONA_CHAR_LIMIT = 2000
CORE_MEMORY_HUMAN_CHAR_LIMIT = 2000

# Function return limits
FUNCTION_RETURN_CHAR_LIMIT = 3000  # ~300 words

MAX_PAUSE_HEARTBEATS = 360  # in min

MESSAGE_CHATGPT_FUNCTION_MODEL = "gpt-3.5-turbo"
MESSAGE_CHATGPT_FUNCTION_SYSTEM_MESSAGE = "You are a helpful assistant. Keep your responses short and concise."

#### Functions related

# REQ_HEARTBEAT_MESSAGE = f"{NON_USER_MSG_PREFIX}request_heartbeat == true"
REQ_HEARTBEAT_MESSAGE = f"{NON_USER_MSG_PREFIX}Function called using request_heartbeat=true, returning control"
# FUNC_FAILED_HEARTBEAT_MESSAGE = f"{NON_USER_MSG_PREFIX}Function call failed"
FUNC_FAILED_HEARTBEAT_MESSAGE = f"{NON_USER_MSG_PREFIX}Function call failed, returning control"


RETRIEVAL_QUERY_DEFAULT_PAGE_SIZE = 5

# TODO Is this config or constant?
CORE_MEMORY_PERSONA_CHAR_LIMIT: int = 2000
CORE_MEMORY_HUMAN_CHAR_LIMIT: int = 2000
