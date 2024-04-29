const obj = {
  toString() {
    return 'abc';
  },
  valueOf() {
    return true;
  },
};

console.log(1 + obj);
