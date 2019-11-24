const years = {
    start : 1900,
    end   : 2000 
};

const genArray = y => {
    let arr = [];
    for (let i = y.start; i <= y.end; i++) {
        arr.push(i);
    }
    return arr;
};

const leapyears = y => {
    return genArray(years).filter(i => {
        if (i%4==0) {
            if (i%100==0) {
                if (i%400==0) {
                    return true;
                }
                return false;
            }
            return true;
        }
        return false;
    });
};

const cal = [];

cal[0][0] = new Date(years.start,1,1).getDay();
