function isMirror(str1, str2) {
  return (
    removeNonAlphabetical(str1) === reverseString(removeNonAlphabetical(str2))
  );
}

const reverseString = (str) => str.split("").reverse().join("");

const removeNonAlphabetical = (str) => {
  const nonAlphabetical = /[^a-zA-Z]/g;
  return str.replaceAll(nonAlphabetical, "");
};
