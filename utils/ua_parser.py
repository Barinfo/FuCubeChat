# utils/ua_parser.py
from ua_parser import user_agent_parser

def parse_user_agent(ua_string):
    ua_data = user_agent_parser.Parse(ua_string)
    device_info = ua_data['device']
    os_info = ua_data['os']
    ua_info = ua_data['user_agent']

    device_type = device_info['family'] if device_info['family'] else '未知设备'
    os_type = os_info['family'] if os_info['family'] else '未知操作系统'
    os_version = os_info['major'] if os_info['major'] else '未知版本'
    browser_type = ua_info['family'] if ua_info['family'] else '未知浏览器'
    browser_version = ua_info['major'] if ua_info['major'] else '未知版本'

    return {
        'device_type': device_type,
        'os_type': os_type,
        'os_version': os_version,
        'browser_type': browser_type,
        'browser_version': browser_version
    }
