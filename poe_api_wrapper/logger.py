import logging

# 创建日志记录器
logger = logging.getLogger('poe_api_wrapper')
logger.setLevel(logging.INFO)

# 避免重复日志
if not logger.handlers:
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 设置日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # 将处理器添加到日志记录器
    logger.addHandler(console_handler)

# 导出日志记录器
__all__ = ['logger']
