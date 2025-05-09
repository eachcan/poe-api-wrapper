PROXY = False

def format_proxy(proxy_str: str) -> dict:
    """Format proxy string to proxy dict
    
    Args:
        proxy_str (str): proxy string in format 'ip:port' or 'http://ip:port'
        
    Returns:
        dict: proxy dict in format {'http://': 'http://ip:port'}
    """
    if not proxy_str.startswith('http://'):
        proxy_str = f'http://{proxy_str}'
    return {'http://': proxy_str}

def format_proxies(proxies: list) -> list:
    """Format list of proxy strings to list of proxy dicts
    
    Args:
        proxies (list): list of proxy strings
        
    Returns:
        list: list of proxy dicts
    """
    return [format_proxy(proxy) for proxy in proxies]