import urllib.request
import urllib.parse
import json
import re
import os

colleges = {
    'Amity University, Jaipur': 'jaipur.amity.edu',
    'ARCH Academy of Design': 'archedu.org',
    'Arya Group Of Colleges': 'aryacollege.in',
    'Baldev Ram Mirdha Institute of Technology': 'brmit.in',
    'Biyani Group of Colleges': 'biyanicolleges.org',
    'Commerce College, Jaipur': 'uniraj.ac.in',
    'Compucom Institute of Information Technology and Management': 'compucom.co.in',
    'Dr. Bhimrao Ambedkar Law University': 'alujaipur.ac.in',
    'Haridev Joshi University of Journalism and Mass Communication': 'hju.ac.in',
    'HCM Rajasthan State Institute of Public Administration': 'hcmripa.gov.in',
    'Homoeopathy University': 'homoeopathyuniversityinfo.org',
    'ICFAI University, Jaipur': 'iujaipur.edu.in',
    'IIS University': 'iisuniv.ac.in',
    'Indian Institute of Crafts and Design': 'iicd.ac.in',
    'IHM Jaipur': 'ihmjaipur.com',
    'IPS Business School': 'ipsedu.in',
    'Jagadguru Ramanandacharya Rajasthan Sanskrit University': 'jrrsanskrituniversity.ac.in',
    'Jaipur National University': 'jnujaipur.ac.in',
    'JECRC University': 'jecrcuniversity.edu.in',
    'JK Lakshmipat University': 'jklu.edu.in',
    'Lal Bahadur Shastri College, Jaipur': 'lbscollege.com',
    'Maharaja College, Jaipur': 'universitymaharajacollege.ac.in',
    'Manipal University Jaipur': 'jaipur.manipal.edu',
    'National Institute of Agricultural Marketing': 'ccsniam.gov.in',
    'National Institute of Ayurveda': 'nia.nic.in',
    'NIMS University': 'nimsuniversity.org',
    'Pareek College': 'pareekcollege.com',
    'Picasso Animation College': 'picasso.co.in',
    'Poornima University': 'poornima.edu.in',
    'Pratap University': 'pratap.edu.in',
    'R. A. Podar Institute of Management': 'rapim.ac.in',
    'University of Rajasthan': 'uniraj.ac.in',
    'Rajasthan College': 'universityrajasthancollege.ac.in',
    'Rajasthan Pharmacy College': 'rpcjaipur.com',
    'Rawat PG Girls College': 'rawatpgcollege.com',
    'Subodh College': 'subodhpgcollege.com',
    "St. Xavier's College Jaipur": 'stxaviersjaipur.org',
    'Suresh Gyan Vihar University': 'gyanvihar.org',
    'University of Engineering & Management, Jaipur': 'uem.edu.in',
    'University of Technology, Jaipur': 'uot.edu.in',
    'Vivekananda Global University': 'vgu.ac.in',
    'MNIT Jaipur': 'mnit.ac.in',
    'LNMIIT Jaipur': 'lnmiit.ac.in',
    'Apex University': 'apex.edu.in',
    'SKIT Jaipur': 'skit.ac.in',
    'Global Institute of Technology': 'git.ac.in',
    'Poornima College of Engineering': 'poornima.org',
    'Rajasthan College of Engineering': 'rce.ac.in',
    'Tagore Engineering College': 'tagoreengineering.ac.in',
    'Jaipur Engineering College': 'jecjaipuroncampus.in'
}


def get_wiki_logo(query, domain):
    try:
        search_query = urllib.parse.quote(query)
        search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={search_query}&utf8=&format=json"
        req = urllib.request.Request(search_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read())
            if not data['query']['search']: return False
            title = data['query']['search'][0]['title']

        page_url = f"https://en.wikipedia.org/wiki/{urllib.parse.quote(title.replace(' ', '_'))}"
        req = urllib.request.Request(page_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8', errors='ignore')

        # Find infobox image
        match = re.search(r'<table class="[^"]*infobox[^"]*".*?<img[^>]+src="([^"]+)"', html, re.DOTALL)
        if match:
            img_url = match.group(1)
            if img_url.startswith('//'):
                img_url = 'https:' + img_url
            
            # Change to higher res if it's a thumbnail (it usually is)
            # Example: .../thumb/a/a2/Logo.png/220px-Logo.png -> .../a/a2/Logo.png
            img_url = re.sub(r'/thumb(/[^/]+/[^/]+/[^/]+)/[^/]+$', r'\\1', img_url)

            req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as img_resp:
                with open(f'e:/AArohan/college/{domain}.png', 'wb') as f:
                    f.write(img_resp.read())
            print(f"Downloaded Wikipedia logo for {query}")
            return True
            
    except Exception as e:
        pass
    return False

for name, domain in colleges.items():
    if not domain: continue
    
    # Check if we already have a reasonably sized image (e.g. > 10KB)
    try:
        size = os.path.getsize(f'e:/AArohan/college/{domain}.png')
        if size > 15000:
            print(f"Already have good logo for {name}")
            continue
    except:
        pass

    if not get_wiki_logo(name, domain):
        print(f"Could not find Wikipedia logo for {name}")
