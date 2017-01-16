import urllib.request
from bs4 import BeautifulSoup
url='http://www.amazon.in/gp/product/B016QBTJWQ/ref=s9_acss_bw_cts_VodooFS_T1L2?pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-12&pf_rd_r=1TGDFSN93QQ5MPRRX577&pf_rd_t=101&pf_rd_p=b6ccceac-31d7-4d24-85d1-e4652c88034a&pf_rd_i=1805560031'
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
for row in soup.find_all('div',attrs={"class" : "a-section"}):
 file=open("/home/playermukesh/Desktop/file4.txt","w")
 soup = BeautifulSoup(content, "html.parser")
 file.write(row.text)
 file.close()
