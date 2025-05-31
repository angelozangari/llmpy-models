from enum import Enum, auto

class Provider(Enum):
    ANTHROPIC = auto()
    OPENAI = auto()

class Model(Enum):
    GPT_4_1106_PREVIEW = 'gpt-4-1106-preview'
    DALL_E_3 = 'dall-e-3'
    DALL_E_2 = 'dall-e-2'
    GPT_4O_AUDIO_PREVIEW_2024_10_01 = 'gpt-4o-audio-preview-2024-10-01'
    GPT_4_TURBO_PREVIEW = 'gpt-4-turbo-preview'
    TEXT_EMBEDDING_3_SMALL = 'text-embedding-3-small'
    GPT_4_TURBO_2024_04_09 = 'gpt-4-turbo-2024-04-09'
    GPT_4_TURBO = 'gpt-4-turbo'
    BABBAGE_002 = 'babbage-002'
    GPT_4 = 'gpt-4'
    TEXT_EMBEDDING_ADA_002 = 'text-embedding-ada-002'
    CHATGPT_4O_LATEST = 'chatgpt-4o-latest'
    TEXT_EMBEDDING_3_LARGE = 'text-embedding-3-large'
    GPT_4O_MINI_AUDIO_PREVIEW = 'gpt-4o-mini-audio-preview'
    GPT_4O_AUDIO_PREVIEW = 'gpt-4o-audio-preview'
    GPT_4O_MINI_REALTIME_PREVIEW = 'gpt-4o-mini-realtime-preview'
    GPT_4O_MINI_REALTIME_PREVIEW_2024_12_17 = 'gpt-4o-mini-realtime-preview-2024-12-17'
    GPT_4_1_NANO = 'gpt-4.1-nano'
    GPT_3_5_TURBO_INSTRUCT_0914 = 'gpt-3.5-turbo-instruct-0914'
    GPT_4O_MINI_SEARCH_PREVIEW = 'gpt-4o-mini-search-preview'
    GPT_4_1_NANO_2025_04_14 = 'gpt-4.1-nano-2025-04-14'
    GPT_3_5_TURBO_16K = 'gpt-3.5-turbo-16k'
    GPT_4O_REALTIME_PREVIEW = 'gpt-4o-realtime-preview'
    DAVINCI_002 = 'davinci-002'
    GPT_3_5_TURBO_1106 = 'gpt-3.5-turbo-1106'
    GPT_4O_SEARCH_PREVIEW = 'gpt-4o-search-preview'
    GPT_3_5_TURBO_INSTRUCT = 'gpt-3.5-turbo-instruct'
    GPT_3_5_TURBO = 'gpt-3.5-turbo'
    O3_MINI_2025_01_31 = 'o3-mini-2025-01-31'
    GPT_4O_MINI_SEARCH_PREVIEW_2025_03_11 = 'gpt-4o-mini-search-preview-2025-03-11'
    GPT_4_0125_PREVIEW = 'gpt-4-0125-preview'
    GPT_4O_2024_11_20 = 'gpt-4o-2024-11-20'
    GPT_4O_2024_05_13 = 'gpt-4o-2024-05-13'
    O1_2024_12_17 = 'o1-2024-12-17'
    O1 = 'o1'
    GPT_4_0613 = 'gpt-4-0613'
    O1_MINI = 'o1-mini'
    GPT_4O_MINI_TTS = 'gpt-4o-mini-tts'
    O1_PRO = 'o1-pro'
    GPT_4O_TRANSCRIBE = 'gpt-4o-transcribe'
    GPT_4_5_PREVIEW = 'gpt-4.5-preview'
    O1_PRO_2025_03_19 = 'o1-pro-2025-03-19'
    GPT_4_5_PREVIEW_2025_02_27 = 'gpt-4.5-preview-2025-02-27'
    GPT_4O_SEARCH_PREVIEW_2025_03_11 = 'gpt-4o-search-preview-2025-03-11'
    GPT_IMAGE_1 = 'gpt-image-1'
    O1_MINI_2024_09_12 = 'o1-mini-2024-09-12'
    TTS_1_HD = 'tts-1-hd'
    GPT_4O = 'gpt-4o'
    TTS_1_HD_1106 = 'tts-1-hd-1106'
    GPT_4O_2024_08_06 = 'gpt-4o-2024-08-06'
    GPT_4O_MINI_2024_07_18 = 'gpt-4o-mini-2024-07-18'
    GPT_4_1_MINI = 'gpt-4.1-mini'
    GPT_4O_MINI = 'gpt-4o-mini'
    GPT_4O_MINI_AUDIO_PREVIEW_2024_12_17 = 'gpt-4o-mini-audio-preview-2024-12-17'
    GPT_3_5_TURBO_0125 = 'gpt-3.5-turbo-0125'
    TTS_1 = 'tts-1'
    TTS_1_1106 = 'tts-1-1106'
    GPT_4O_REALTIME_PREVIEW_2024_10_01 = 'gpt-4o-realtime-preview-2024-10-01'
    GPT_4O_MINI_TRANSCRIBE = 'gpt-4o-mini-transcribe'
    GPT_4_1_MINI_2025_04_14 = 'gpt-4.1-mini-2025-04-14'
    OMNI_MODERATION_2024_09_26 = 'omni-moderation-2024-09-26'
    O3_MINI = 'o3-mini'
    OMNI_MODERATION_LATEST = 'omni-moderation-latest'
    GPT_4_1 = 'gpt-4.1'
    WHISPER_1 = 'whisper-1'
    GPT_4_1_2025_04_14 = 'gpt-4.1-2025-04-14'
    COMPUTER_USE_PREVIEW_2025_03_11 = 'computer-use-preview-2025-03-11'
    COMPUTER_USE_PREVIEW = 'computer-use-preview'
    O3 = 'o3'
    O3_2025_04_16 = 'o3-2025-04-16'
    GPT_4O_AUDIO_PREVIEW_2024_12_17 = 'gpt-4o-audio-preview-2024-12-17'
    O4_MINI = 'o4-mini'
    O4_MINI_2025_04_16 = 'o4-mini-2025-04-16'
    GPT_4O_REALTIME_PREVIEW_2024_12_17 = 'gpt-4o-realtime-preview-2024-12-17'
    CODEX_MINI_LATEST = 'codex-mini-latest'
    O1_PREVIEW_2024_09_12 = 'o1-preview-2024-09-12'
    O1_PREVIEW = 'o1-preview'
    CLAUDE_OPUS_4_20250514 = 'claude-opus-4-20250514'
    CLAUDE_SONNET_4_20250514 = 'claude-sonnet-4-20250514'
    CLAUDE_3_7_SONNET_20250219 = 'claude-3-7-sonnet-20250219'
    CLAUDE_3_5_SONNET_20241022 = 'claude-3-5-sonnet-20241022'
    CLAUDE_3_5_HAIKU_20241022 = 'claude-3-5-haiku-20241022'
    CLAUDE_3_5_SONNET_20240620 = 'claude-3-5-sonnet-20240620'
    CLAUDE_3_HAIKU_20240307 = 'claude-3-haiku-20240307'
    CLAUDE_3_OPUS_20240229 = 'claude-3-opus-20240229'

model_to_provider = {
    Model.GPT_4_1106_PREVIEW: Provider.OPENAI,
    Model.DALL_E_3: Provider.OPENAI,
    Model.DALL_E_2: Provider.OPENAI,
    Model.GPT_4O_AUDIO_PREVIEW_2024_10_01: Provider.OPENAI,
    Model.GPT_4_TURBO_PREVIEW: Provider.OPENAI,
    Model.TEXT_EMBEDDING_3_SMALL: Provider.OPENAI,
    Model.GPT_4_TURBO_2024_04_09: Provider.OPENAI,
    Model.GPT_4_TURBO: Provider.OPENAI,
    Model.BABBAGE_002: Provider.OPENAI,
    Model.GPT_4: Provider.OPENAI,
    Model.TEXT_EMBEDDING_ADA_002: Provider.OPENAI,
    Model.CHATGPT_4O_LATEST: Provider.OPENAI,
    Model.TEXT_EMBEDDING_3_LARGE: Provider.OPENAI,
    Model.GPT_4O_MINI_AUDIO_PREVIEW: Provider.OPENAI,
    Model.GPT_4O_AUDIO_PREVIEW: Provider.OPENAI,
    Model.GPT_4O_MINI_REALTIME_PREVIEW: Provider.OPENAI,
    Model.GPT_4O_MINI_REALTIME_PREVIEW_2024_12_17: Provider.OPENAI,
    Model.GPT_4_1_NANO: Provider.OPENAI,
    Model.GPT_3_5_TURBO_INSTRUCT_0914: Provider.OPENAI,
    Model.GPT_4O_MINI_SEARCH_PREVIEW: Provider.OPENAI,
    Model.GPT_4_1_NANO_2025_04_14: Provider.OPENAI,
    Model.GPT_3_5_TURBO_16K: Provider.OPENAI,
    Model.GPT_4O_REALTIME_PREVIEW: Provider.OPENAI,
    Model.DAVINCI_002: Provider.OPENAI,
    Model.GPT_3_5_TURBO_1106: Provider.OPENAI,
    Model.GPT_4O_SEARCH_PREVIEW: Provider.OPENAI,
    Model.GPT_3_5_TURBO_INSTRUCT: Provider.OPENAI,
    Model.GPT_3_5_TURBO: Provider.OPENAI,
    Model.O3_MINI_2025_01_31: Provider.OPENAI,
    Model.GPT_4O_MINI_SEARCH_PREVIEW_2025_03_11: Provider.OPENAI,
    Model.GPT_4_0125_PREVIEW: Provider.OPENAI,
    Model.GPT_4O_2024_11_20: Provider.OPENAI,
    Model.GPT_4O_2024_05_13: Provider.OPENAI,
    Model.O1_2024_12_17: Provider.OPENAI,
    Model.O1: Provider.OPENAI,
    Model.GPT_4_0613: Provider.OPENAI,
    Model.O1_MINI: Provider.OPENAI,
    Model.GPT_4O_MINI_TTS: Provider.OPENAI,
    Model.O1_PRO: Provider.OPENAI,
    Model.GPT_4O_TRANSCRIBE: Provider.OPENAI,
    Model.GPT_4_5_PREVIEW: Provider.OPENAI,
    Model.O1_PRO_2025_03_19: Provider.OPENAI,
    Model.GPT_4_5_PREVIEW_2025_02_27: Provider.OPENAI,
    Model.GPT_4O_SEARCH_PREVIEW_2025_03_11: Provider.OPENAI,
    Model.GPT_IMAGE_1: Provider.OPENAI,
    Model.O1_MINI_2024_09_12: Provider.OPENAI,
    Model.TTS_1_HD: Provider.OPENAI,
    Model.GPT_4O: Provider.OPENAI,
    Model.TTS_1_HD_1106: Provider.OPENAI,
    Model.GPT_4O_2024_08_06: Provider.OPENAI,
    Model.GPT_4O_MINI_2024_07_18: Provider.OPENAI,
    Model.GPT_4_1_MINI: Provider.OPENAI,
    Model.GPT_4O_MINI: Provider.OPENAI,
    Model.GPT_4O_MINI_AUDIO_PREVIEW_2024_12_17: Provider.OPENAI,
    Model.GPT_3_5_TURBO_0125: Provider.OPENAI,
    Model.TTS_1: Provider.OPENAI,
    Model.TTS_1_1106: Provider.OPENAI,
    Model.GPT_4O_REALTIME_PREVIEW_2024_10_01: Provider.OPENAI,
    Model.GPT_4O_MINI_TRANSCRIBE: Provider.OPENAI,
    Model.GPT_4_1_MINI_2025_04_14: Provider.OPENAI,
    Model.OMNI_MODERATION_2024_09_26: Provider.OPENAI,
    Model.O3_MINI: Provider.OPENAI,
    Model.OMNI_MODERATION_LATEST: Provider.OPENAI,
    Model.GPT_4_1: Provider.OPENAI,
    Model.WHISPER_1: Provider.OPENAI,
    Model.GPT_4_1_2025_04_14: Provider.OPENAI,
    Model.COMPUTER_USE_PREVIEW_2025_03_11: Provider.OPENAI,
    Model.COMPUTER_USE_PREVIEW: Provider.OPENAI,
    Model.O3: Provider.OPENAI,
    Model.O3_2025_04_16: Provider.OPENAI,
    Model.GPT_4O_AUDIO_PREVIEW_2024_12_17: Provider.OPENAI,
    Model.O4_MINI: Provider.OPENAI,
    Model.O4_MINI_2025_04_16: Provider.OPENAI,
    Model.GPT_4O_REALTIME_PREVIEW_2024_12_17: Provider.OPENAI,
    Model.CODEX_MINI_LATEST: Provider.OPENAI,
    Model.O1_PREVIEW_2024_09_12: Provider.OPENAI,
    Model.O1_PREVIEW: Provider.OPENAI,
    Model.CLAUDE_OPUS_4_20250514: Provider.ANTHROPIC,
    Model.CLAUDE_SONNET_4_20250514: Provider.ANTHROPIC,
    Model.CLAUDE_3_7_SONNET_20250219: Provider.ANTHROPIC,
    Model.CLAUDE_3_5_SONNET_20241022: Provider.ANTHROPIC,
    Model.CLAUDE_3_5_HAIKU_20241022: Provider.ANTHROPIC,
    Model.CLAUDE_3_5_SONNET_20240620: Provider.ANTHROPIC,
    Model.CLAUDE_3_HAIKU_20240307: Provider.ANTHROPIC,
    Model.CLAUDE_3_OPUS_20240229: Provider.ANTHROPIC,
}
