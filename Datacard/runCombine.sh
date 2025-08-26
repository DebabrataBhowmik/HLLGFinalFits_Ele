
# https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/commonstatsmethods/
# for mass in $(seq 120 1 130); do
#     nohup combine ./cards/datacard_heeg_runII_combm2_${mass}.txt -M AsymptoticLimits -n _combm2_${mass} -m ${mass} --run=blind --noFitAsimov -v 1 &> ./logger/limit_combm2_${mass}.txt &
# done

# for mass in $(seq 120 1 130); do
#     nohup combine ./cards/datacard_heeg_runII_tagm2_${mass}.txt -M AsymptoticLimits -n _tagm2_${mass} -m ${mass} --run=blind --noFitAsimov -v 1 &> ./logger/limit_tagm2_${mass}.txt &
# done

# for mass in $(seq 120 1 130); do
#     nohup combine ./cards/datacard_heeg_runII_untagm2_${mass}.txt -M AsymptoticLimits -n _untagm2_${mass} -m ${mass} --run=blind --noFitAsimov -v 1 &> ./logger/limit_untagm2_${mass}.txt &
# done

# for cat in Merged2Gsf_VBF Merged2Gsf_BST Merged2Gsf_EBHR9 Merged2Gsf_EBLR9 Merged2Gsf_EE; do
#     nohup combine ./cards/datacard_heeg_runII_${cat}_125.txt -M AsymptoticLimits -n _${cat}_125 -m 125 --run=blind --noFitAsimov -v 1 &> ./logger/limit_${cat}_125.txt &
# done



# for mass in $(seq 120 1 130); do
#     nohup combine ./cards/datacard_heeg_runII_combm2_${mass}.txt -M Significance -n _combm2_${mass}_expSignal1 -m ${mass} --expectSignal 1 --pvalue -t -1 -v 1 &> ./logger/significance_combm2_${mass}_expSignal1.txt &

#     nohup combine ./cards/datacard_heeg_runII_combm2_${mass}.txt -M Significance -n _combm2_${mass}_expectSignalMass125 -m ${mass} --expectSignalMass=125 --pvalue -t -1 -v 1  &> ./logger/significance_combm2_${mass}_expectSignalMass125.txt &
# done 

# combine -M GenerateOnly ./cards/datacard_heeg_runII_combm2_${mass}.txt

# for mass in $(seq 120 1 130); do
#     combine -M GenerateOnly ./cards/datacard_heeg_runII_combm2_${mass}.txt -t -1 --saveToys --expectSignal=1 --expectSignalMass=${mass} -m ${mass} -v 2
# done 

for mass in $(seq 120 1 130); do
    nohup combine ./cards/datacard_heeg_runII_combm2_${mass}.txt -M Significance --pvalue -n _combm2_${mass}_expSignal1 -m ${mass} -t -1 --toysFile higgsCombineTest.GenerateOnly.mH${mass}.123456.root -v 1 &> ./logger/significance_combm2_${mass}_expSignal1.txt &

    nohup combine ./cards/datacard_heeg_runII_combm2_${mass}.txt -M Significance --pvalue -n _combm2_${mass}_expectSignalMass125 -m ${mass} -t -1 --toysFile higgsCombineTest.GenerateOnly.mH125.123456.root -v 1 &> ./logger/significance_combm2_${mass}_expectSignalMass125.txt &
done 