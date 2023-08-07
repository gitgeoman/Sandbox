#!/bin/bash



#dowlnoad file
get_file(){
    # echo ${item_name}
    wget -P ./nrw "https://www.opengeodata.nrw.de/produkte/geobasis/lusat/dop/dop_jp2_f10/${i}.jp2"
    echo "${i}" | tee -a log_download.txt # log ktore pliki juz pobrane

}
#gdal tranform
transform(){
    gdalwarp -s_srs EPSG:25832 -q -tr 0.9 0.9 -tap -t_srs EPSG:3857 -co BIGTIFF=YES -co TILED=YES -co COMPRESS=LZW -of GTiff -r near "./nrw/${i}.jp2" "./nrw_t/${i}.tif"
}

echo 'start skryptu'

no_of_threats=15 # stacja 80
for i in $(cat filelist.txt); do
    ((a=a%no_of_threats)); ((a++==0)) && wait
    get_file ${i} &
done

for i in $(cat filelist.txt); do
    ((a=a%no_of_threats)); ((a++==0)) && wait
    transform ${i} &
done

echo 'koniec skryptu'


#unzip \*.zip
# find . -name "*.zip" -exec rm -rf {} \;