
grep -P "^#" $1 > ${1}.temp.header
for i in {1..22}
do
    grep -P "^$i\t" $1 > ${1}.temp.chr$i
done
grep -P "^M\t" $1 > ${1}.temp.chrM
grep -P "^X\t" $1 > ${1}.temp.chrX
grep -P "^Y\t" $1 > ${1}.temp.chrY
toCat=${1}.temp.header
toCat="$toCat ${1}.temp.chrM"
for i in {1..22}
do
    toCat="$toCat ${1}.temp.chr$i"
done
toCat="$toCat ${1}.temp.chrX"
toCat="$toCat ${1}.temp.chrY"
cat $toCat > ${1}.karo.vcf

for i in {1..22}
do
        rm ${1}.temp.chr$i
done
rm ${1}.temp.header
rm ${1}.temp.chrM
rm ${1}.temp.chrX
rm ${1}.temp.chrY
