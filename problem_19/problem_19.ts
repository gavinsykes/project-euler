let year = 1900;
let month = 4;
const adder = (month,year) => {
  switch(month) {
    case 5:
    case 7:
    case 10:
    case 12:
      return 2;
    case 3:
      return year % 4 == 0 ? 1 : 0;
    default:
      return 3;
  }
}

let sundays = 0;
let weekday = 7;

while (year < 2001) {
  month++;
  if (month > 12) {
    month = 1;
    year++;
  }
  weekday = weekday + adder(month,year) % 7;
  if (weekday = 7) {
    sundays++;
  }
}

console.log(sundays);