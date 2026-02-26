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

html = ''
js = '        const COLLEGE_DOMAINS = {\n'

for name in sorted(colleges.keys()):
    domain = colleges[name]
    html += f'                                    <div class="custom-option" data-value="{name}" data-domain="{domain}">\n'
    html += f'                                        <img src="college/{domain}.png" alt="" onerror="this.style.display=\'none\'">\n'
    html += f'                                        <span>{name}</span>\n'
    html += f'                                    </div>\n'
    js += f'            "{name}": "{domain}",\n'

html += """                                    <div class="custom-optgroup">Other</div>
                                    <div class="custom-option" data-value="Other Jaipur College" data-domain="">
                                        <span style="font-size:1.2rem; margin-right:4px;">🏛️</span>
                                        <span>Other College in Jaipur</span>
                                    </div>
                                    <div class="custom-option" data-value="Out of Jaipur" data-domain="">
                                        <span style="font-size:1.2rem; margin-right:4px;">🌍</span>
                                        <span>College Outside Jaipur</span>
                                    </div>"""

js = js.rstrip(',\n') + '\n        };'

with open('e:/AArohan/html_chunk.txt', 'w', encoding='utf-8') as f:
    f.write(html)
with open('e:/AArohan/js_chunk.txt', 'w', encoding='utf-8') as f:
    f.write(js)

print('Chunks written to txt')
