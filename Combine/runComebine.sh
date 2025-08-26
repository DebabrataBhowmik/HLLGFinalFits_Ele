# significance
# cd ./cards
# for mass in $(seq 120 1 130); do
#     combine -M GenerateOnly datacard_heeg_runII_comb_${mass}.txt -t -1 --saveToys --expectSignal=1 --expectSignalMass=${mass} -m ${mass}
# done 

# for mass in $(seq 120 1 130); do
#     echo "============================================="
#     echo "Expected significance for mass @"${mass} "GeV"
#     combine datacard_heeg_runII_comb_${mass}.txt -M Significance -n _comb_${mass}_expSignal1 -m ${mass} -t -1 --toysFile higgsCombineTest.GenerateOnly.mH${mass}.123456.root
#     combine datacard_heeg_runII_comb_${mass}.txt -M Significance -n _comb_${mass}_expectSignalMass125 -m ${mass} -t -1 --toysFile higgsCombineTest.GenerateOnly.mH125.123456.root 
#     echo "============================================="
# done 

# # limit
# for mass in $(seq 120 1 130); do
#     echo "============================================="
#     echo "Expected limit for mass @"${mass} "GeV"
#     combine datacard_heeg_runII_comb_${mass}.txt -M AsymptoticLimits -n _comb_${mass} -m ${mass} --run=blind 
#     echo "============================================="
# done 

# combine datacard_heeg_runII_untagged_125.txt -M AsymptoticLimits -n _untagged_125 -m 125 --run=blind 
# combine datacard_heeg_runII_tagged_125.txt -M AsymptoticLimits -n _tagged_125 -m 125 --run=blind 

# combine datacard_heeg_runII_Merged2Gsf_VBF_125.txt -M AsymptoticLimits -n _VBF_125 -m 125 --run=blind
# combine datacard_heeg_runII_Merged2Gsf_BST_125.txt -M AsymptoticLimits -n _BST_125 -m 125 --run=blind 
# combine datacard_heeg_runII_Merged2Gsf_EBHR9_125.txt -M AsymptoticLimits -n _EBHR9_125 -m 125 --run=blind
# combine datacard_heeg_runII_Merged2Gsf_EBLR9_125.txt -M AsymptoticLimits -n _EBLR9_125 -m 125 --run=blind
# combine datacard_heeg_runII_Merged2Gsf_EE_125.txt -M AsymptoticLimits -n _EE_125 -m 125 --run=blind
# combine datacard_heeg_runII_Resolved_125.txt -M AsymptoticLimits -n _Resolved_125 -m 125 --run=blind

# text2workspace.py datacard_heeg_runII_Merged2Gsf_VBF_125.txt -c datacard_heeg_runII_Merged2Gsf_VBF_125.root -m 125
# text2workspace.py datacard_heeg_runII_Merged2Gsf_BST_125.txt -c datacard_heeg_runII_Merged2Gsf_BST_125.root -m 125
# text2workspace.py datacard_heeg_runII_Merged2Gsf_EBHR9_125.txt -c datacard_heeg_runII_Merged2Gsf_EBHR9_125.root -m 125
# text2workspace.py datacard_heeg_runII_Merged2Gsf_EBLR9_125.txt -c datacard_heeg_runII_Merged2Gsf_EBLR9_125.root -m 125
# text2workspace.py datacard_heeg_runII_Merged2Gsf_EE_125.txt -c datacard_heeg_runII_Merged2Gsf_EE_125.root -m 125
# text2workspace.py datacard_heeg_runII_Resolved_125.txt -c datacard_heeg_runII_Resolved_125.root -m 125

# nohup python3 ../makeToys.py -i datacard_heeg_runII_Merged2Gsf_VBF_125.root -e Merged2Gsf_VBF &> ../logger/toy_Merged2Gsf_VBF.txt &
# nohup python3 ../makeToys.py -i datacard_heeg_runII_Merged2Gsf_BST_125.root -e Merged2Gsf_BST &> ../logger/toy_Merged2Gsf_BST.txt &
# nohup python3 ../makeToys.py -i datacard_heeg_runII_Merged2Gsf_EBHR9_125.root -e Merged2Gsf_EBHR9 &> ../logger/toy_Merged2Gsf_EBHR9.txt &
# nohup python3 ../makeToys.py -i datacard_heeg_runII_Merged2Gsf_EBLR9_125.root -e Merged2Gsf_EBLR9 &> ../logger/toy_Merged2Gsf_EBLR9.txt &
# nohup python3 ../makeToys.py -i datacard_heeg_runII_Merged2Gsf_EE_125.root -e Merged2Gsf_EE &> ../logger/toy_Merged2Gsf_EE.txt &
# nohup python3 ../makeToys.py -i datacard_heeg_runII_Resolved_125.root -e Resolved &> ../logger/toy_Resolved.txt &

python makeSplusBModelPlot_old.py --inputWSFile ./cards/datacard_heeg_runII_Merged2Gsf_VBF_125.root --cats Merged2Gsf_VBF --ext Merged2Gsf_VBF --doBands --doToyVeto
python makeSplusBModelPlot_old.py --inputWSFile ./cards/datacard_heeg_runII_Merged2Gsf_BST_125.root --cats Merged2Gsf_BST --ext Merged2Gsf_BST --doBands --doToyVeto
python makeSplusBModelPlot_old.py --inputWSFile ./cards/datacard_heeg_runII_Merged2Gsf_EBHR9_125.root --cats Merged2Gsf_EBHR9 --ext Merged2Gsf_EBHR9 --doBands --doToyVeto
python makeSplusBModelPlot_old.py --inputWSFile ./cards/datacard_heeg_runII_Merged2Gsf_EBLR9_125.root --cats Merged2Gsf_EBLR9 --ext Merged2Gsf_EBLR9 --doBands --doToyVeto
python makeSplusBModelPlot_old.py --inputWSFile ./cards/datacard_heeg_runII_Merged2Gsf_EE_125.root --cats Merged2Gsf_EE --ext Merged2Gsf_EE --doBands --doToyVeto
python makeSplusBModelPlot_old.py --inputWSFile ./cards/datacard_heeg_runII_Resolved_125.root --cats Resolved --ext Resolved --doBands --doToyVeto











# echo "============================================="
# echo "===============   NoLoose    ================"
# echo "============================================="
# for mass in $(seq 120 1 130); do
#     echo "============================================="
#     echo "Expected limit for mass @"${mass} "GeV"
#     combine datacard_heeg_runII_NoLoose_comb_${mass}.txt -M AsymptoticLimits -n _NoLoose_comb_${mass} -m ${mass} --run=blind --noFitAsimov
#     echo "============================================="
# done 


# for mass in $(seq 120 1 130); do
#     echo "============================================="
#     echo "Expected limit for mass @"${mass} "GeV"
#     combine datacard_heeg_runII_Merged_comb_${mass}.txt -M AsymptoticLimits -n _Merged_comb_${mass} -m ${mass} --run=blind --noFitAsimov
#     echo "============================================="
# done 

# for mass in $(seq 120 1 130); do
#     echo "============================================="
#     echo "Expected limit for mass @"${mass} "GeV"
#     combine datacard_heeg_runII_Resolved_${mass}.txt -M AsymptoticLimits -n _Resolved_${mass} -m ${mass} --run=blind --noFitAsimov
#     echo "============================================="
# done 


# combine  datacard_heeg_runII_NoLoose_comb_125.txt -M AsymptoticLimits -n _test_noloose -m 125 --run=blind --noFitAsimov
# combine  datacard_heeg_runII_comb_125.txt -M AsymptoticLimits -n _test_noloose -m 125 --run=blind --noFitAsimov








# for mass in $(seq 120 1 130); do
#     combine ./cards/datacard_heeg_runII_comb_${mass}.txt -M Significance -n _comb_${mass}_expSignal1 -m ${mass} -t -1 --toysFile ./results/higgsCombineTest.GenerateOnly.mH${mass}.123456.root
#     combine ./cards/datacard_heeg_runII_comb_${mass}.txt -M Significance -n _comb_${mass}_expectSignalMass125 -m ${mass} -t -1 --toysFile ./results/higgsCombineTest.GenerateOnly.mH125.123456.root 
# done 
# cp *.root ./results
# rm *.root
# --pvalue
# for mass in $(seq 120 1 130); do
#     echo "Expected significance for mass @"${mass} "GeV"
#     combine ./cards/datacard_heeg_runII_comb_${mass}.txt -M Significance -n _comb_${mass}_expSignal1 -m ${mass} -t -1 --expectSignal=1
#     echo "---------------------------------------"
# done 

# cp *.root ./results
# rm *.root

# echo "--->  all done!"

# combine ./cards/datacard_heeg_runII_comb_125.txt -M AsymptoticLimits -n _comb_125 -m 125 --run=blind --noFitAsimov -v 1; mv *.root result/
# combine ./cards/datacard_hmmg_runII_comb_125.txt -M Significance -n _comb_125_expSignal1 -m 125 -t -1 --toysFile ./result/higgsCombineTest.GenerateOnly.mH125.123456.root -v 1


# python makeSplusBModelPlot_old.py --inputWSFile ./cards/datacard_heeg_runII_Merged2Gsf_VBF_125.root --cats Merged2Gsf_VBF --ext Merged2Gsf_VBF --doBands --doToyVeto
# python makeSplusBModelPlot_old.py --inputWSFile ./cards/datacard_heeg_runII_Merged2Gsf_BST_125.root --cats Merged2Gsf_BST --ext Merged2Gsf_BST --doBands --doToyVeto
# python makeSplusBModelPlot_old.py --inputWSFile ./cards/datacard_heeg_runII_Merged2Gsf_EBHR9_125.root --cats Merged2Gsf_EBHR9 --ext Merged2Gsf_EBHR9 --doBands --doToyVeto
# python makeSplusBModelPlot_old.py --inputWSFile ./cards/datacard_heeg_runII_Merged2Gsf_EBLR9_125.root --cats Merged2Gsf_EBLR9 --ext Merged2Gsf_EBLR9 --doBands --doToyVeto
# python makeSplusBModelPlot_old.py --inputWSFile ./cards/datacard_heeg_runII_Merged2Gsf_EE_125.root --cats Merged2Gsf_EE --ext Merged2Gsf_EE --doBands --doToyVeto
# python makeSplusBModelPlot_old.py --inputWSFile ./cards/datacard_heeg_runII_Resolved_125.root --cats Resolved --ext Resolved --doBands --doToyVeto

# cd ./cards
# combine datacard_heeg_runII_comb_125.txt -M AsymptoticLimits -n _comb_125 -m 125 --run=blind
# combine datacard_heeg_runII_comb_125.txt -M GenerateOnly -t -1 --saveToys --expectSignal=1 --expectSignalMass=125 -m 125
# combine datacard_heeg_runII_comb_125.txt -M Significance -n _comb_125_expSignal1 -m 125 -t -1 --toysFile higgsCombineTest.GenerateOnly.mH125.123456.root -v 1

# combineTool.py -M CollectLimits higgsCombine_NoLoose_comb_*.AsymptoticLimits.mH*.root -o limits_noloose.json
# combineTool.py -M CollectLimits higgsCombine_comb_*.AsymptoticLimits.mH*.root -o limits.json

#  python3 plotLimits_modified.py --auto-style exp 'cards/limits_resolved.json:exp0:Title="Expected resolved"'  'cards/limits_merged.json:exp0:Title="Expected merged"' 'cards/limits_noloose.json:exp0:Title="Expected all"'

