"""Render static SVG charts only from the reproduced article-table values."""
from pathlib import Path
import json,html
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'_data/highway_investment_exhibits.json').read_text())
out=ROOT/'assets/images/highway-investment'; out.mkdir(parents=True,exist_ok=True)
ink='#21372b'; muted='#526459'; green='#27704d'; blue='#446a8a'; line='#d3ded5'
def num(x): return float(x.replace(',','').replace('**',''))
def label(x): return html.escape(str(x))
def text(x,y,s,size=16,fill=ink,anchor='start',weight='normal'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{label(s)}</text>'
def rect(x,y,w,h,color):return f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{color}"/>'
def ln(x,y,x2,y2,color=line):return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{color}"/>'
def save(n,height,body,desc):
    title=data[n-1]['title']
    source=f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="{height}" viewBox="0 0 720 {height}" role="img" aria-labelledby="title desc"><title id="title">{label(title)}</title><desc id="desc">{label(desc)}</desc><rect width="720" height="{height}" fill="#fafbf8"/><g font-family="system-ui,-apple-system,sans-serif">'+''.join(body)+'</g></svg>\n'
    (out/f'exhibit-{n}.svg').write_text(source)

# Exhibit 1: equal scales for two year-end stocks; no latest-basis splice.
b=[text(28,34,'NHAI funding stocks',22,weight='bold'),text(28,60,'₹ crore · standalone statutory accounts',16,muted),rect(28,79,15,15,green),text(50,92,'Government capital'),rect(288,79,15,15,blue),text(310,92,'Borrowings including ADB')]
x0=105; length=480; maxv=800000
for tick in (0,200000,400000,600000,800000):
    x=x0+tick/maxv*length;b.extend([ln(x,116,x,403),text(x,426,f'{tick//1000:,}k' if tick else '0',15,muted,'middle')])
for i,row in enumerate(data[0]['rows']):
    y=123+i*56;b.append(text(28,y+27,row[0],16))
    for k,color in ((1,green),(2,blue)):
        v=num(row[k]);yy=y+(k-1)*23;b.extend([rect(x0,yy,v/maxv*length,17,color),text(x0+v/maxv*length+7,yy+14,f'{v/1000:,.1f}k',14)])
b.append(text(28,455,'FY2024 statement faces retain an “Unaudited” label; see source note.',14,muted))
save(1,470,b,'Government capital rises from 219,026.69 to 708,177.58 crore; borrowings rise to FY2022 then decline. All bars start at zero. Exact values follow in the table.')

# Exhibit 2: small multiples, separate units and zero-based scales.
b=[text(28,34,'NHIT portfolio and distributions',22,weight='bold'),text(28,60,'Different measures · separate zero-based scales',16,muted)]
panels=[(1,'Operating revenue','₹ crore',5000,green),(2,'Closing book assets','₹ crore',60000,blue),(3,'Carrying borrowings','₹ crore',30000,blue),(4,'Distribution per unit','₹ / unit',12,green)]
for idx,(col,title,unit,ceiling,color) in enumerate(panels):
    ox=28+(idx%2)*350; oy=92+(idx//2)*226
    b.extend([text(ox,oy,title,18,weight='bold'),text(ox,oy+22,unit,15,muted)])
    x0=ox+42;y0=oy+165;chartw=264;charth=112
    for val in (0,ceiling/2,ceiling):
        yy=y0-val/ceiling*charth;b.extend([ln(x0,yy,x0+chartw,yy),text(x0-7,yy+5,f'{val:g}',13,muted,'end')])
    for i,row in enumerate(data[1]['rows']):
        x=x0+9+i*51;v=num(row[col]);h=v/ceiling*charth
        b.extend([rect(x,y0-h,31,h,color),text(x+15.5,y0+23,row[0].replace('FY20','FY'),14,muted,'middle')])
b.extend([text(28,555,'FY2022 began operating on 16 December 2021. Later acquisitions change the comparison.',14,muted)])
save(2,580,b,'Four panels show the five table years. Revenue, book assets and carrying borrowing are in crore; DPU is rupees per unit. Each panel starts at zero and uses its own clearly labelled scale. These are changing-portfolio comparisons.')

# Exhibit 3: the exact additive cash bridge; no implication of recurring CFO.
b=[text(28,34,'NHIT FY2026 distribution cash bridge',22,weight='bold'),text(28,60,'₹ crore · trust level · financing adjustments included',16,muted)]
x0=76; y0=300; scale=200/2400
for val in (0,600,1200,1800,2400):
    yy=y0-val*scale;b.extend([ln(x0,yy,690,yy),text(x0-10,yy+5,f'{val:,}',14,muted,'end')])
running=0
names=[['Trust NDCF','before','adjustments'],['Unpaid ZCB','interest','adjustment'],['First DSRA','release'],['Second DSRA','release'],['Adjusted cash','available']]
for i,row in enumerate(data[2]['rows']):
    v=num(row[1]);x=x0+20+i*121
    if i in (0,4): start=0;end=v
    else:start=running;end=running+v
    if i<4:running=end
    y=y0-end*scale;h=(end-start)*scale
    b.append(rect(x,y,64,max(h,.7),green if i in (0,4) else blue))
    b.append(text(x+32,94,f'{v:,.2f}' if i in (0,4) else f'+{v:,.2f}',15,ink,'middle',weight='bold'))
    b.append(ln(x+32,102,x+32,y-4,muted))
    if i<4:b.append(ln(x+64,y,x+121,y,muted))
    for j,name in enumerate(names[i]):b.append(text(x+32,327+j*21,name,14,ink,'middle'))
b.extend([text(28,393,'DSRA: debt-service reserve account. Unpaid interest remains an obligation.',14,muted),text(28,416,'This bridge includes specified post-year-end SPV receipts; see the article caveats.',14,muted)])
save(3,430,b,'Start at 2055.43 crore, add 78.40 crore unpaid zero-coupon-bond interest adjustment, 93.61 crore first reserve release and 6.80 crore second reserve release. The total is 2234.24 crore. This is not consolidated operating cash flow.')
print('Rendered three static SVGs from the five reproduced exhibit tables; exhibits 4 and 5 stay as evidence tables.')
