# Bottom-up sizing: quick commerce in the South Gujarat corridor
cities = {  # ~2021 population estimates (Wikipedia "List of cities in Gujarat by population"; no 2021 census was held)
 "Vapi":230598, "Navsari":367322, "Bharuch":288244, "Valsad":231756}
GROWTH=1.08      # assumption: 2021->2026 growth (~1.5%/yr)
HH=4.2           # assumption: persons per urban household
AOV=450          # assumption: tier-2 AOV, below Blinkit's ~Rs518 company-wide
BE=800           # Emkay: tier-2 dark store breakeven orders/day
scen={"Low":(0.04,3,0.15),"Base":(0.06,4,0.20),"High":(0.10,6,0.30)}  # adoption, orders/HH/month, Zepto share
METRO=0.34       # NCR monthly-adoption benchmark (TAM ceiling)
rows=[]
tot_hh=0
for c,p in cities.items():
    hh=p*GROWTH/HH; tot_hh+=hh
    r=[c,round(p*GROWTH),round(hh)]
    for s,(a,f,sh) in scen.items():
        daily=hh*a*f/30
        r+= [round(daily)]
    rows.append(r)
print("city,pop2026,households,daily_orders_low,base,high")
for r in rows: print(*r,sep=",")
print("total households",round(tot_hh))
for s,(a,f,sh) in scen.items():
    daily=tot_hh*a*f/30; gmv=daily*30*12*AOV
    som=daily*sh
    print(f"{s}: market {daily:.0f}/day, annual GMV Rs{gmv/1e7:.1f} Cr; Zepto SOM {som:.0f}/day = {som/BE:.2f} breakeven stores; SOM GMV Rs{som*360*AOV/1e7:.1f} Cr")
tam=tot_hh*METRO*6/30
print(f"TAM (metro adoption 34%, 6 orders/mo): {tam:.0f}/day, Rs{tam*360*AOV/1e7:.0f} Cr/yr")
# Vapi single-store test: orders needed
vh=230598*GROWTH/HH
for a in (0.06,0.08,0.10,0.12):
  for f in (4,6):
    print(f"Vapi adoption {a:.0%} freq {f}: market {vh*a*f/30:.0f}/day; Zepto@30% {vh*a*f/30*0.3:.0f}")
# What monthly adoption would let Zepto run 4 stores (one per city) at break-even?
need=4*BE
for sh,f in ((0.20,4),(0.30,6)):
    a=need/sh*30/(tot_hh*f)
    print(f"Break-even adoption for 4 Zepto stores at {sh:.0%} share, {f} orders/mo: {a:.0%}")
# Rival stores already in the corridor (quickcommercemap, early Oct 2026; JioMart excluded)
rivals={"Vapi":5,"Valsad":2,"Navsari":1,"Bharuch":3}
print("rival stores",sum(rivals.values()),"break-even orders needed",sum(rivals.values())*BE)
