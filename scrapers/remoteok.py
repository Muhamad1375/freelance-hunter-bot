import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0"
}


def get_job_description(url):

    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        # RemoteOK description selector (احتمالاً اینه)
        desc = soup.find("div", {"class": "html"})

        if desc:
            return desc.get_text(strip=True)[:300]

        # fallback
        return ""

    except:
        return ""


def get_jobs():

    url = "https://remoteok.com/api"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return []

    data = response.json()

    jobs = []

    for item in data[1:]:

        link = item.get("url", "")

        if not link.startswith("http"):
            link = "https://remoteok.com" + link

        # 🧠 گرفتن توضیح کوتاه از صفحه
        description = get_job_description(link)

        jobs.append({
            "title": item.get("position", ""),
            "company": item.get("company", ""),
            "description": description,
            "link": link,
            "source": "RemoteOK"
        })

    return jobs