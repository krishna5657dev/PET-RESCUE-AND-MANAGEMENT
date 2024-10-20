function ConfirmDialog() {
    var x=confirm("Are you sure to delete record?")
    if (x) {
      return true;
    } else {
      return false;
    }
  }

