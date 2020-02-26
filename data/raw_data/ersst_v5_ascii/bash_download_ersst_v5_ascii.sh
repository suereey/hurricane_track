int_year=1880
while [ $int_year -le 2019 ]; do
wget https://www1.ncdc.noaa.gov/pub/data/cmb/ersst/v5/ascii/ersst.v5.$int_year.asc
int_year=`expr $int_year + 1`
done


wget https://www1.ncdc.noaa.gov/pub/data/cmb/ersst/v5/ascii/read.ersst.f
wget https://www1.ncdc.noaa.gov/pub/data/cmb/ersst/v5/ascii/Readme
