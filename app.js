for (var i = 1; i < 3; i++) {
  ((counter) => {
    setTimeout(() => {
      console.log(counter);
    }, 1000);
  })(i);
}
