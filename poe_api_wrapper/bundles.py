from httpx import Client
from bs4 import BeautifulSoup
from .logger import logger
from py_mini_racer import MiniRacer
import re

class PoeBundle:
    form_key_pattern = r"window\.([a-zA-Z0-9]+)=function\(\)\{return window"
    window_secret_pattern = r'let useFormkeyDecode=[\s\S]*?(window\.[\w]+="[^"]+")'
    static_pattern = r'static[^"]*\.js'

    def __init__(self, document: str):
        self._window = "const window={document:{hack:1},navigator:{userAgent:'safari <3'}};"
        self._src_scripts = []
        self._webpack_script: str = None

        self.init_window(document)

    def init_window(self, document: str):
        # initialize the window object with document scripts
        logger.info("Initializing web data")

        if not document:
            logger.error("Empty document received")
            return

        try:
            scripts = BeautifulSoup(document, "html.parser").find_all('script')
            logger.info(f"Found {len(scripts)} script tags")

            for script in scripts:
                if (src := script.attrs.get("src")) and (src not in self._src_scripts):
                    if "_app" in src:
                        logger.info(f"Found app script: {src}")
                        self.init_app(src)
                    if "buildManifest" in src:
                        logger.info(f"Found manifest script: {src}")
                        self.extend_src_scripts(src)
                    elif "webpack" in src:
                        logger.info(f"Found webpack script: {src}")
                        self._webpack_script = src
                        self.extend_src_scripts(src)
                    else:
                        self._src_scripts.append(src)
                elif ("document." in script.text) or ("function" not in script.text):
                    continue
                elif script.attrs.get("type") == "application/json":
                    continue
                self._window += script.text

            logger.info("Web data initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize web data: {e}")

    def init_app(self, src: str):
        script = self.load_src_script(src)
        if not (window_secret_match := re.search(self.window_secret_pattern, script)):
            raise RuntimeError("Failed to find window secret in js scripts")
        
        self._window += window_secret_match.group(1) + ';'

    def extend_src_scripts(self, manifest_src: str):
        # extend src scripts list with static scripts from manifest
        static_main_url = self.get_base_url(manifest_src)
        manifest = self.load_src_script(manifest_src)

        matches = re.findall(self.static_pattern, manifest)
        scr_list = [f"{static_main_url}{match}" for match in matches]

        self._src_scripts.extend(scr_list)

    @staticmethod
    def load_src_script(src: str) -> str:
        with Client(
            proxies={'http://': 'http://127.0.0.1:7890', 'https://': 'http://127.0.0.1:7890'},
            verify=True,
            follow_redirects=True,
            http2=True,
            http1=False,
            timeout=30
        ) as client:
            try:
                resp = client.get(src)
                if resp.status_code != 200:
                    logger.warning(f"Failed to load script {src}, status code: {resp.status_code}")
                    return ""
                return resp.text
            except Exception as e:
                logger.error(f"Failed to load script {src}: {e}")
                return ""

    @staticmethod
    def get_base_url(src: str) -> str:
        return src.split("static/")[0]

    def get_form_key(self) -> str:
        script = self._window

        match = re.search(self.form_key_pattern, script)
        if not (secret := match.group(1)):
            raise RuntimeError("Failed to parse form-key function in Poe document")
        
        script += f'window.{secret}().slice(0, 32);'
        context = MiniRacer()
        formkey = str(context.eval(script))
        logger.info(f"Retrieved formkey successfully: {formkey}")
        return formkey
