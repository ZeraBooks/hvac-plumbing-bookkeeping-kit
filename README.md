# HVAC and plumbing bookkeeping kit

Bookkeeping for an HVAC or plumbing company separates service calls from
installs, holds maintenance agreements and install deposits as money owed
until the work is done, books financed jobs at full price with the dealer fee
as a cost, and tracks parts on the trucks. This kit has the accounts, a
checklist, a plan schedule and a worked month.

## Files

| File | What it is |
|---|---|
| `chart-of-accounts.csv` | A starting chart of accounts for a residential service company: service, install and plan revenue apart, truck stock as an asset, customer deposits and deferred plan revenue as liabilities. Columns: Number, Name, Type, Detail, Notes. |
| `month-end-checklist.md` | Nine steps for closing the month on accrual books. |
| `maintenance-plan-schedule.csv` | Thirty fictional 240.00 yearly plans sold in October 2026, earned 600.00 a month over twelve months, with the deferred balance at each month end. |
| `financed-jobs.csv` | A fictional financed install: job price, dealer fee rate, dealer fee and the payout from the lender. |
| `october-2026-month.csv` | The fictional company's October 2026 on accrual books: every line, its account, and whether it counts in profit. |
| `check_trade_month.py` | Checks the financed jobs and the plan schedule, ties them to the month, and prints profit plus the money that reached the bank but is not earned yet. Python 3, standard library only. |

## How to use it

1. Import `chart-of-accounts.csv` into your accounting software, or compare it
   with the accounts you have. Commercial contractors add job accounts and
   retainage.
2. Keep a plan schedule like `maintenance-plan-schedule.csv` for each month's
   plan sales, and a row in `financed-jobs.csv` for each financed job.
3. Run the check:

   ```
   python3 check_trade_month.py financed-jobs.csv maintenance-plan-schedule.csv october-2026-month.csv
   ```

4. Work through `month-end-checklist.md` before you lock the month.

## The worked month

Northfield Heating & Plumbing is a fictional company with five technicians.
October 2026, accrual books:

| | Amount |
|---|---|
| Service and repair invoices paid | 41,300.00 |
| Water heater install, financed, full price | 12,000.00 |
| 30 maintenance plans at 240.00, earned this month | 600.00 |
| **Revenue** | **53,900.00** |
| Dealer fee taken by the lending partner, 8% | 960.00 |
| Parts and equipment used on jobs | 18,450.00 |
| Technician payroll, gross | 16,900.00 |
| Employer payroll taxes | 1,292.85 |
| Van fuel and leases | 3,140.00 |
| **Expenses** | **40,742.85** |
| **Profit** | **13,157.15** |

Two amounts reached the bank but are not in profit: a 6,000.00 deposit for a
November furnace install (customer deposits) and 6,600.00 of the 7,200.00 in
plan sales, which will be earned over the next eleven months (deferred
maintenance revenue). Counted as sales, they would have shown October
12,600.00 better than it was.

All figures are fictional.

## FAQ

### Cash or accrual books for a service company?

Many small shops start on cash basis. Once you sell maintenance agreements or
take install deposits, accrual books show the real month, because they hold
that money until it is earned. Your accountant decides what the tax return
uses.

### How do I record a financed job?

Book the full job price as revenue and the dealer fee as a financing fee. The
lender pays you the job less the fee, so booking only the payout makes every
financed job look cheaper than the price you quoted.

### Are parts on the trucks an expense?

Not until they go into a job. Parts bought and still on a van are truck stock,
an asset. Booking every supply house invoice straight to job cost makes some
months look terrible and others too good.

## Learn more

Full guide: [Bookkeeping for HVAC and plumbing companies](https://www.zerabooks.com/bookkeeping-for-hvac-and-plumbing). Related: [ZeraBooks bookkeeping services](https://www.zerabooks.com/bookkeeping-services).

## License

The content and data in this repository are licensed under
[CC BY 4.0](LICENSE). Free to use and adapt with credit to ZeraBooks.
The code (`*.py`) is licensed under [MIT](LICENSE-CODE).

Maintained by [ZeraBooks](https://www.zerabooks.com).
