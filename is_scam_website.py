import requests
import json

def is_scam_website(domain):
  """
  检查域名是否为诈骗网站。

  Args:
    domain: 要检查的域名。

  Returns:
    True: 域名是诈骗网站。
    False: 域名不是诈骗网站。
  """

  # 获取域名的whois信息。
  whois_url = "https://whois.domaintools.com/" + domain
  whois_response = requests.get(whois_url)
  whois_data = json.loads(whois_response.content)

  # 检查域名是否在诈骗网站列表中。
  scam_websites_url = "https://www.fraudwatchinternational.com/phishing-scam-database/"
  scam_websites_response = requests.get(scam_websites_url)
  scam_websites_data = json.loads(scam_websites_response.content)

  for scam_website in scam_websites_data:
    if scam_website["domain"] == domain:
      return True

  return False

if __name__ == "__main__":
  domain = input("请输入域名：")
  if is_scam_website(domain):
    print("域名是诈骗网站。")
  else:
    print("域名不是诈骗网站。")
