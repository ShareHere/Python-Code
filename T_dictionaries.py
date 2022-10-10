mounthconversions ={
    "Jan" :"January",
    "Feb" :"february",
    "Mar" :"March",
    "Apr" :"April",
    "May" :"May",
    "jun":"june",
    "jul":"july",
    "aug":"auguest",
    "sep":"septembar",
    "oct":"octbar",
    "nov":"novbar",
    "dec":"decbar",

}

print(mounthconversions.get("Mar"))
print(mounthconversions["jul"])

print(mounthconversions.get("lov","not a valid key"))