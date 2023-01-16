var verified = [];
document.querySelector("select").onchange = function (e) {
  if (
    this.querySelectorAll("option:checked").length <= this.dataset.maxoption
  ) {
    verified = Array.apply(null, this.querySelectorAll("option:checked"));
  } else {
    Array.apply(null, this.querySelectorAll("option")).forEach(function (e) {
      e.selected = verified.indexOf(e) > -1;
    });
  }
};
