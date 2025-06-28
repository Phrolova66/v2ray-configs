from bs4 import BeautifulSoup
import requests
import urllib.parse

def get_v2ray_links(ts_url):
    try:
        response = requests.get(ts_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # 搜索所有可能包含配置的标签
            divs = soup.find_all('div', class_='tgme_widget_message_text')
            divs2 = soup.find_all('div', class_='tgme_widget_message_text js-message_text before_footer')
            spans = soup.find_all('span', class_='tgme_widget_message_text')
            codes = soup.find_all('code')
            span = soup.find_all('span')
            main = soup.find_all('div')

            all_tags = divs + spans + codes + divs2 + span + main

            v2ray_configs = []
            for tag in all_tags:
                text = tag.get_text().strip()
                # 支持更多协议类型
                if any(text.startswith(p) for p in ['vmess://', 'vless://', 'ss://', 'trojan://', 'tuic://']):
                    v2ray_configs.append(text)

            return v2ray_configs
    except Exception as  e:
        print(f'Failed to fetch URL: { e }')
        return None

def save_all_configs(v2ray_configs):
    with open('Subs.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(v2ray_configs))

if __name__ == '__main__':
    telegram_urls = [
        'v2line', 'forwardv2ray', 'inikotesla', 'PrivateVPNs', 'VlessConfig', 'v2rayngvpn', 'vmess_vless_v2rayng',
        'proxystore11', 'DirectVPN', 'VmessProtocol', 'OutlineVpnOfficial', 'shadowsocksshop', 'beiten', 'MsV2ray',
        'foxrayiran', 'DailyV2RY', 'yaney_01', 'FreakConfig', 'EliV2ray', 'ServerNett', 'v2rayng_fa2', 'v2rayng_org',
        'freeland8', 'vmessiran', 'Outline_Vpn', 'vmessq', 'WeePeeN', 'V2rayNG3', 'ShadowsocksM', 'networknim',
        'V2rayNGvpni', 'custom_14', 'v2rayNG_VPNN', 'v2ray_outlineir', 'v2_vmess', 'FreeVlessVpn', 'FreeNet1500',
        'v2rayan', 'ShadowSocks_s', 'napsternetv_config', 'vpnmasi', 'V2Ray_FreedomIran', 'V2RAY_VMESS_free',
        'v2ray_for_free', 'V2rayN_Free', 'free4allVPN', 'vpn_ocean', 'configV2rayForFree', 'FreeV2rays', 'DigiV2ray',
        'freev2rayssr', 'v2rayn_server', 'Shadowlinkserverr', 'iranvpnet', 'vmess_iran', 'mahsaamoon1', 'V2RAY_NEW',
        'configV2rayNG', 'config_v2ray', 'vpn_proxy_custom', 'v2ray_custom', 'VPNCUSTOMIZE', 'HTTPCustomLand',
        'ViPVpn_v2ray', 'frev2ray', 'v2ray_ar', 'beta_v2ray', 'vip_vpn_2022', 'FOX_VPN66', 'VorTexIRN', 'YtTe3la',
        'Network_442', 'VPN_443', 'v2rayng_v', 'ultrasurf_12', 'iSeqaro', 'frev2rayng', 'Awlix_ir', 'v2rayNG_Matsuri',
        'God_CONFIG', 'V2pedia', 'Configforvpn01', 'V2RayOxygen', 'v2rayNG_VPN', 'v2RayChannel', 'Easy_Free_VPN'
    ]

    all_v2ray_configs = []
    prefix = 'https://t.me/s/'
    for url in telegram_urls:
        url = prefix + url
        if configs := get_v2ray_links(url):
            all_v2ray_configs.extend(configs)

    if all_v2ray_configs:
        # 去重处理
        unique_configs = list(set(all_v2ray_configs))
        # 保存到Subs.txt
        save_all_configs(unique_configs)
        print(f'Saved { len(unique_configs) } unique configs to Subs.txt')
    else:
        print('No V2Ray configs found.')
