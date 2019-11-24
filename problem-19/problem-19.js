const years = {
    start : 1900,
    end   : 2000 
};

const leapyears = y => { y.filter(i => i%4 == 0 ? i%100 == 0 ? i%400 == 0 ? true : false : true : false) };

