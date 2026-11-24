# Should Zepto build out South Gujarat?

**Market-entry memo: bottom-up sizing, competitor mapping and break-even analysis.**
Self-initiated, November 2026. Public data only. Not affiliated with Zepto or any rival.

Full memo: **[madhvisingh265.github.io/case-studies/quick-commerce-south-gujarat.html](https://madhvisingh265.github.io/case-studies/quick-commerce-south-gujarat.html)**

## The question

Should Zepto open dark stores across Vapi, Valsad, Navsari and Bharuch in the next 12 months? (Dark stores are the small warehouses quick-commerce apps deliver from in 10–20 minutes.)

## Recommendation: not yet

- In the base case, the four towns generate about **2,300 quick-commerce orders a day** across all platforms.
- A small-city dark store needs about **800 orders a day** to break even (Emkay's estimate for tier-2 cities).
- The **11 dark stores** already there would need about **8,800 a day** between them. The corridor already has more stores than demand.
- At a 20% share, Zepto would get about **460 orders a day**, less than one store's break-even.
- **Hold, and revisit in 12 months** if any of these triggers fire: Blinkit adds stores in Navsari or Valsad; Zepto's Valsad store passes 800 orders a day for two months; or store costs bring break-even under about 500 orders a day.

## How the estimate is built

Households × share who order each month × orders per month × order value, with low, base and high cases.

| Layer | Definition | Orders / day | Order value / year |
|---|---|---:|---:|
| TAM | If the corridor ordered like Delhi NCR (34% of households, 6 orders a month) | 19,548 | ₹317 Cr |
| SAM | Today's market, base case (6% of households, 4 orders a month) | 2,300 | ₹37 Cr |
| SOM | Zepto at a 20% share of SAM | 460 | ₹7.5 Cr |

For four Zepto stores to break even, about 19% of households would need to order monthly. That's roughly three times the tier-2 average today.

## Files

| File | What it is |
|---|---|
| [quick_commerce_sizing.py](quick_commerce_sizing.py) | The sizing model. Every assumption is a named variable at the top; change one and re-run with `python3 quick_commerce_sizing.py` |
| [quick_commerce_sizing_output.txt](quick_commerce_sizing_output.txt) | Output of the current run |
| [data/dark_stores_oct2026.csv](data/dark_stores_oct2026.csv) | Dark stores by town and platform (QuickCommerceMap, early October 2026; JioMart excluded) |

## Assumptions and limits

- Population: 2021 estimates for each city (the 2021 census wasn't held) × 1.08 growth to 2026. 4.2 people per household.
- Ordering share (4 / 6 / 10%), orders per month (3 / 4 / 6), average order value (₹450) and Zepto's share (15 / 20 / 30%) are assumptions shown as ranges. The conclusion holds in the low and base cases and weakens only in the high case.
- Store counts come from one third-party tracker whose totals don't always match its per-platform counts.
- Biggest upside not modelled: Vapi's wider catchment (the Vapi Municipal Corporation estimates about 4.5 lakh residents, and Daman and Silvassa are next door), plus demand from industrial areas.

Sources are listed at the end of the [full memo](https://madhvisingh265.github.io/case-studies/quick-commerce-south-gujarat.html).
