import os, string, secrets, base64
from urllib.parse import urlparse
from httpx import Client
from .logger import logger

BASE_URL = 'https://poe.com'
HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,fr-FR;q=0.8,fr;q=0.7",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://poe.com/",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"136.0.3240.50\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"136.0.7103.49\", \"Microsoft Edge\";v=\"136.0.3240.50\", \"Not.A/Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"19.0.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}

SubscriptionsMutation = {
    "subscriptions":[
        {"subscriptionName":"messageAdded","query":None,"queryHash":"8ebe5e387283f58cd755b5c472d558b9c54849162072aedfd0691d208825341b"},
        {"subscriptionName":"messageCancelled","query":None,"queryHash":"14647e90e5960ec81fa83ae53d270462c3743199fbb6c4f26f40f4c83116d2ff"},
        {"subscriptionName":"messageDeleted","query":None,"queryHash":"4af67ecc4f59845dcc5435ecae35407671ec73c19a71ad5385b5c32a4a9c1f25"},
        {"subscriptionName":"messageRead","query":None,"queryHash":"4263caec604c36d564301de20237616c3745f0b57b88cb505b88234d47da73bc"},
        {"subscriptionName":"messageEdited","query":None,"queryHash":"a26a011ac1d2ac99a95edb2e50430fbcd88e4c1b512cef514bbf24c19bb29f57"},
        {"subscriptionName":"messageCreated","query":None,"queryHash":"9252652f3dafdb3da1fdb50b1ce3bc0112ca1917b6e9b1f13b9ed244a9f0aa1e"},
        {"subscriptionName":"messageStateUpdated","query":None,"queryHash":"117a49c685b4343e7e50b097b10a13b9555fedd61d3bf4030c450dccbeef5676"},
        {"subscriptionName":"messageAttachmentAdded","query":None,"queryHash":"65798bb2f409d9457fc84698479f3f04186d47558c3d7e75b3223b6799b6788d"},
        {"subscriptionName":"messageFollowupActionAdded","query":None,"queryHash":"d2e770beae7c217c77db4918ed93e848ae77df668603bc84146c161db149a2c7"},
        {"subscriptionName":"messageMetadataUpdated","query":None,"queryHash":"71c247d997d73fb0911089c1a77d5d8b8503289bc3701f9fb93c9b13df95aaa6"},
        {"subscriptionName":"messageReactionsUpdated","query":None,"queryHash":"3b991ab9b5f281584c9b0f8a6099cbe614bc18bd55efeadd09818a55df2ea057"},
        {"subscriptionName":"messageTextUpdated","query":None,"queryHash":"800eea48edc9c3a81aece34f5f1ff40dc8daa71dead9aec28f2b55523fe61231"},
        {"subscriptionName":"jobStarted","query":None,"queryHash":"c8b0a1fa651db0384cb8bc56bbe4f1d6c0cef28bd1e8176c0d0be2a20bb75fc7"},
        {"subscriptionName":"jobUpdated","query":None,"queryHash":"961c92a9b49fa30e67ee1a9c6a276a92829aecf9135000d6ba69efaf15df91a3"},
        {"subscriptionName":"jobCostUpdated","query":None,"queryHash":"51cae0ccaa83852b5a0c7e0c4badeb6f545c068127148dca05959300cbee1f4f"},
        {"subscriptionName":"viewerStateUpdated","query":None,"queryHash":"755b913e3dc1719f0dbab2dfb7f0dac8730810046af7a9a0c200d03212249f01"},
        {"subscriptionName":"canvasTabClosed","query":None,"queryHash":"d132f03ae1f69988057ca73dd5db4cc9f593fa6c1f63de7538953aaf7eb79313"},
        {"subscriptionName":"canvasTabOpened","query":None,"queryHash":"5675962a7dd461a44b395f5ffaf854a4ef2fbde99219ce0daa941f1eae168a2c"},
        {"subscriptionName":"canvasTabBackgrounded","query":None,"queryHash":"e83a2652673044eb4d537d455b35132be8bed12a81b1bd37f5452651224cd217"},
        {"subscriptionName":"onDataToForwardToCanvasTab","query":None,"queryHash":"3306309cb5a1d7e19867ced094f779a22d28c5c6fc617dfa136d11f51c7cee0c"},
        {"subscriptionName":"chatTitleUpdated","query":None,"queryHash":"ee062b1f269ecd02ea4c2a3f1e4b2f222f7574c43634a2da4ebeb616d8647e06"},
        {"subscriptionName":"chatDeletedV2","query":None,"queryHash":"05ca4e5f143a6429f11de0d852a9402ad770dd76f44bc1712f587338f0fa211e"},
        {"subscriptionName":"knowledgeSourceUpdated","query":None,"queryHash":"7de63f89277bcf54f2323008850573809595dcef687f26a78561910cfd4f6c37"},
        {"subscriptionName":"messagePointLimitUpdated","query":None,"queryHash":"89a2a08bd89c2225d7c9a2d0ba45787c9604bb65aadf8ed92963cc7e49586560"},
        {"subscriptionName":"chatMemberAddedWithContext","query":None,"queryHash":"7a07f48756aab5cba821b0bccff4134737f3b0eeb34f9332a12abd3dc7ff5c48"},
        {"subscriptionName":"chatMemberRemoved","query":None,"queryHash":"f85bd556b04ff0f8d47aeae14c081d194435323838e30cf7a2631c3b251eb578"},
        {"subscriptionName":"viewerRemovedFromChat","query":None,"queryHash":"29be861843ccd18c210295f8cbe1c65b4b40be06319ef1b19ec1351a8f8347ab"},
        {"subscriptionName":"chatSettingsUpdated","query":None,"queryHash":"76806efbd2d584ba9e2e515f79045a8fb2015ecb5b8e9a25bade2843fcf5fee7"},
        {"subscriptionName":"chatModalStateChanged","query":None,"queryHash":"c70c8b13b4d6d7c1a76b9d133b18a64fed6c77d88bcbe327019109b70c9a96cf"},
        {"subscriptionName":"defaultBotOfChatChanged","query":None,"queryHash":"158618e29f404ffdf715c2ea6d3377700ad1c5de6991651708380d5bd2640c71"},
        {"subscriptionName":"messageFollowupActionUpdated","query":None,"queryHash":"f87a8f00ade546fab3b79541ac3e0404be20b46604f6e209258b8933886aa80b"},
        {"subscriptionName":"unseenCountsUpdated","query":None,"queryHash":"da2a3d6565ca8a358364692657cd9b9e0aaa8b98c0686f998ef03e1e42e2bd08"},
        {"subscriptionName":"chatMuteStatusUpdated","query":None,"queryHash":"97563dd19a520bacc607de851c84df0c75bc882ecff92aa37ac2c0b3b49e8ed3"},
        {"subscriptionName":"allChatsDeleted","query":None,"queryHash":"14d26446fb7a00fae2854efc45df6abef0ca2e3d25af1cca7457bef6726963db"}]
}


BOTS_LIST = {
    'App-Creator': 'app_creator',
    'Assistant': 'capybara',
    'Claude-3.5-Sonnet': 'claude_3_igloo',
    'Claude-3-Opus': 'claude_2_1_cedar',
    'Claude-3-Sonnet': 'claude_2_1_bamboo',
    'Claude-3-Haiku': 'claude_3_haiku',
    'Claude-3-Opus-200k': 'claude_3_opus_200k',
    'Claude-3.5-Sonnet-200k': 'claude_3_igloo_200k',
    'Claude-3-Sonnet-200k': 'claude_3_sonnet_200k',
    'Claude-3-Haiku-200k': 'claude_3_haiku_200k',
    'Claude-2': 'claude_2_short',
    'Claude-2-100k': 'a2_2',
    'Claude-instant': 'a2',
    'Claude-instant-100k': 'a2_100k',
    'GPT-3.5-Turbo': 'chinchilla',
    'GPT-3.5-Turbo-Raw': 'gpt3_5',
    'GPT-3.5-Turbo-Instruct': 'chinchilla_instruct',
    'ChatGPT-16k': 'agouti',
    'GPT-4-Classic': 'gpt4_classic',
    'GPT-4-Turbo': 'beaver',
    'GPT-4-Turbo-128k': 'vizcacha',
    'GPT-4o': 'gpt4_o',
    'GPT-4o-128k': 'gpt4_o_128k',
    'GPT-4o-Mini': 'gpt4_o_mini',
    'GPT-4o-Mini-128k': 'gpt4_o_mini_128k',
    'Google-PaLM': 'acouchy',
    'Code-Llama-13b': 'code_llama_13b_instruct',
    'Code-Llama-34b': 'code_llama_34b_instruct',
    'Solar-Mini':'upstage_solar_0_70b_16bit',
    'Gemini-1.5-Flash-Search': 'gemini_pro_search',
    'Gemini-1.5-Pro-2M': 'gemini_1_5_pro_1m',
}

REVERSE_BOTS_LIST = {v: k for k, v in BOTS_LIST.items()}

EXTENSIONS = {
    '.md': 'application/octet-stream',
    '.lua': 'application/octet-stream',
    '.rs': 'application/octet-stream',
    '.rb': 'application/octet-stream',
    '.go': 'application/octet-stream',
    '.java': 'application/octet-stream',
    '.pdf': 'application/pdf',
    '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    '.txt': 'text/plain',
    '.py': 'text/x-python',
    '.js': 'text/javascript',
    '.ts': 'text/plain',
    '.html': 'text/html',
    '.css': 'text/css',
    '.csv': 'text/csv',
    '.c' : 'text/plain',
    '.cs': 'text/plain',
    '.cpp': 'text/plain',
}

MEDIA_EXTENSIONS = {
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.mp4': 'video/mp4',
    '.mov': 'video/quicktime',
    '.mp3': 'audio/mpeg',
    '.wav': 'audio/wav',
}

def bot_map(bot):
    if bot in BOTS_LIST:
        return BOTS_LIST[bot]
    return bot.lower().replace(' ', '')

def generate_nonce(length:int=16):
      return "".join(secrets.choice(string.ascii_letters + string.digits) for i in range(length))

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
    
def generate_file(file_path: list, proxy: dict=None):
    files = []   
    file_size = 0
    for file in file_path:
        if isinstance(file, str) and file.startswith("data:image"):
            file_extension = file.split(";")[0].split("/")[-1]
            content_type = MEDIA_EXTENSIONS.get(f".{file_extension}", "image/png")
            file_data = base64.b64decode(file.split(",")[1])
            file_name = f"{generate_nonce(8)}.{file_extension}"
            files.append((file_name, file_data, content_type))
            file_size += len(file_data)
            
        elif is_valid_url(file):
            # Handle URL files
            file_name = file.split('/')[-1]
            file_extension = os.path.splitext(file_name)[1].lower()
            content_type = MEDIA_EXTENSIONS.get(file_extension, EXTENSIONS.get(file_extension, None))
            if not content_type:
                raise RuntimeError("This file type is not supported. Please try again with a different file.")
            logger.info(f"Downloading file from {file}")
            with Client(proxies=proxy, http2=True) as fetcher:
                response = fetcher.get(file)
                file_data = response.content
            files.append((file_name, file_data, content_type))
            file_size += len(file_data)
        else:
            # Handle local files
            file_extension = os.path.splitext(file)[1].lower()
            content_type = MEDIA_EXTENSIONS.get(file_extension, EXTENSIONS.get(file_extension, None))
            if not content_type:
                raise RuntimeError("This file type is not supported. Please try again with a different file.")
            file_name = os.path.basename(file)
            with open(file, 'rb') as f:
                file_data = f.read()
                files.append((file_name, file_data, content_type))
                file_size += len(file_data)
    return files, file_size