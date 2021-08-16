from bs4 import BeautifulSoup
import csv
import re
import requests
import sys

def extract_data(ticker):
    resp = requests.get(f'https://www.sec.gov/cgi-bin/browse-edgar?CIK={ticker}')
    soup = BeautifulSoup(resp.text, 'html.parser')
    company_tag = soup.find('span', attrs={'class': 'companyName'})
    company_name = company_tag.text.split("CIK#")[0].strip()
    ident_tag = soup.find('p', attrs={'class': 'identInfo'})
    sic = ident_tag.find('a').text.strip()
    sector_name = re.findall(r'SIC:\s+?\d+\s+?-\s+?(.+?)State location:',
                            ident_tag.text)[0].strip()
    biz_tag = soup.find('div', attrs= {'class': 'mailer'})
    addr_tags = biz_tag.find_all('span', attrs={'class': 'mailerAddress'})
    addr_lines = [tag.text.strip() for tag in addr_tags]
    if len(addr_lines) == 2:
        addr_lines.insert(1, "")
    addr1, addr2 = addr_lines[0:2]
    csz = addr_lines[-1].split()
    z = csz[-1]
    state = csz[-2]
    city = " ".join(csz[0:-2])
    return [ticker,company_name, sic, sector_name, addr1, addr2, city, state, z]

if __name__=='__main__':
    ticker_file = sys.argv[1]
    csv_file = sys.argv[2]
    with open(ticker_file) as fin, open(csv_file, 'wt') as fout:
        csvout = csv.writer(fout)
        csvout.writerow(['Ticker', 'Name', 'SIC', 'Sector',
                         'Addr1', 'Addr2', 'City', 'State', 'Zip'])
        for ticker in fin:
            data = extract_data(ticker.strip())
            csvout.writerow(data)
