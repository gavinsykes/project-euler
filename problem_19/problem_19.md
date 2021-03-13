You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday. (*I've checked, it is. The [web page](https://www.dayoftheweek.org/?m=January&d=1&y=1900&go=Go) that told me that also says "If you are trying to learn Spanish then this day of the week in Spanish is lunes." for some reason.*)
- Thirty days has September, April, June and November. All the rest have thirty-one, saving February alone, which has twenty-eight, rain or shine. And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Luckily, straight away, we needn't worry about the third rule too much, as we know that a leap year didn't happen in 1900 but did in 2000, and that all other years within this range divisible by 4 are a leap year.

Now it is a little-known fact that a day that is Monday in one year will be a Tuesday the next, **except** is there is a February 29th between them, i which case it jumps from Monday to Wednesday.

Let's draw up a little table:
| Month     | Starting day when previous month starts with a Monday |
| January   | Thursday (+3) |
| February  | Thursday (+3) |
| March     | Monday (0) *or* Tuesday (+1) if it's a leap year |
| April     | Thursday (+3) |
| May       | Wednesday (+2) |
| June      | Thursday (+3) |
| July      | Wednesday (+2) |
| August    | Thursday (+3) |
| September | Thursday (+3) |
| October   | Wednesday (+2) |
| November  | Thursday (+3) |
| December  | Wednesday (+2) |

So let's take Monday as 1, Tuesday as 2, and so on up to Sunday as 7.
So let's find the first month in 1900 that began with Sunday...
February was Thursday
So was March
April was Sunday
That was easy!
So we can literally start from April 1900, count through the months, adding x, modulo 7 it and if we get 0, job done! If year % 4 == 0, add x+1 to March.