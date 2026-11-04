"""Check an HVAC or plumbing company's month in this repo's layout.

1. Each financed job reads across: job price x dealer fee rate = dealer fee,
   and job price - dealer fee = payout from the lender.
2. The maintenance plan schedule earns the plans evenly, ends at 0.00, and
   its first month agrees with the month file (earned in profit, the rest
   held in deferred maintenance revenue).
3. Profit is every "In profit" line in the month file. Money that reached the
   bank but is not earned yet (deposits, plan money) is listed separately.

Usage:
  python3 check_trade_month.py financed-jobs.csv maintenance-plan-schedule.csv october-2026-month.csv
Python 3, standard library only.
"""
import csv
import sys
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def d(cell):
    return Decimal(cell.strip()) if cell and cell.strip() else Decimal("0")


def rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main(jobs_path, plans_path, month_path):
    ok = True
    for r in rows(jobs_path):
        price, fee, payout = d(r["Job price"]), d(r["Dealer fee"]), d(r["Payout from lender"])
        expected_fee = (price * d(r["Dealer fee rate"])).quantize(CENT, ROUND_HALF_UP)
        if expected_fee != fee or price - fee != payout:
            ok = False
            print(f"{r['Job']}: expected fee {expected_fee:,.2f} and payout {price - expected_fee:,.2f}")
        else:
            print(f"{r['Job']}: revenue {price:,.2f}, dealer fee {fee:,.2f}, lender paid {payout:,.2f}")

    sched = rows(plans_path)
    sold = sum(d(r["Sold this month"]) for r in sched)
    earned = sum(d(r["Earned this month"]) for r in sched)
    balance = Decimal("0")
    for r in sched:
        balance += d(r["Sold this month"]) - d(r["Earned this month"])
        if balance != d(r["Deferred at month end"]):
            ok = False
            print(f"{r['Month']}: running balance is {balance:,.2f}, schedule says {r['Deferred at month end']}")
    if sold != earned or balance != 0:
        ok = False
        print(f"Plans sold {sold:,.2f} but schedule earns {earned:,.2f}, leaving {balance:,.2f}")
    else:
        print(f"Plans sold {sold:,.2f}, earned over {len(sched)} months, schedule ends at 0.00")

    income = expenses = Decimal("0")
    held = defaultdict(Decimal)
    by_account = defaultdict(Decimal)
    for r in rows(month_path):
        amt = d(r["Amount"])
        by_account[r["Account"]] += amt
        if r["In profit"].strip().lower() == "yes":
            if amt >= 0:
                income += amt
            else:
                expenses -= amt
        else:
            held[r["Account"]] += amt
    first = sched[0]
    if by_account["Maintenance agreement revenue"] != d(first["Earned this month"]):
        ok = False
        print("Plan revenue in the month does not agree with the schedule's first month")
    if held["Deferred maintenance revenue"] != d(first["Deferred at month end"]):
        ok = False
        print("Deferred plan money in the month does not agree with the schedule")
    print(f"Revenue {income:,.2f}, expenses {expenses:,.2f}, profit {income - expenses:,.2f}")
    for acct, amt in held.items():
        print(f"In the bank but not earned yet: {acct} {amt:,.2f}")
    print(f"Counted as sales, these would overstate the month by {sum(held.values()):,.2f}")
    print("All checks pass." if ok else "Some checks failed; see above.")
    return ok


if __name__ == "__main__":
    a = sys.argv[1:] + [None] * 3
    sys.exit(0 if main(a[0] or "financed-jobs.csv", a[1] or "maintenance-plan-schedule.csv",
                       a[2] or "october-2026-month.csv") else 1)
