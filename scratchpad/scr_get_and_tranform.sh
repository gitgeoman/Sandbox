#!/bin/bash

get_file(){
    if [ -f "./data/${i}.jp2" ]; then
        echo "${i} już pobrano."
    else
        # echo "pobieram ${i}"
        wget -P "./data/" "https://www.opengeodata.nrw.de/produkte/geobasis/lusat/dop/dop_jp2_f10/${i::-1}.jp2" && wait
        gdalwarp -s_srs EPSG:25832 -q -tr 0.9 0.9 -tap -t_srs EPSG:3857 -co BIGTIFF=YES -co TILED=YES -co COMPRESS=LZW -of GTiff -r near "./data/${i::-1}.jp2" "./output/${i::-1}.tif" && wait
        rm -rf "./nrw_2/${i::-1}.jp2"
    fi


    # echo "${i}" | tee -a log_download.txt # log ktore pliki juz pobrane

}

N=5 # stacja 80
for i in $(cat filelist.txt); do
    ((a=a%N)); ((a++==0)) && wait
    get_file ${i} &
done