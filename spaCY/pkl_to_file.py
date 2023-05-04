import pickle
import sys

def tofile(pkl, newfile):
	with open(pkl, 'rb') as fl: 
		lst = pickle.load(fl)
		fl.close()
	with open(newfile, 'w') as f:
		for i in lst:
			f.write(str(i) + "\n")
		f.close()

# tofile('spaCY\proposition_list.pkl', 'spaCY\cur_prop_txt.txt')
# tofile('spaCY\subj_substance_list.pkl', 'spaCY\cur_subj_txt.txt')
# tofile('spaCY\subj_vb_obj.pkl', 'spaCY\cur_svo_txt.txt')
# tofile('spaCY\quant_list.pkl', 'spaCY\cur_quant_txt.txt')


# tofile('spaCY_hypernymy\_np_vp_pairs.pkl', 'spaCY_hypernymy\_np_vp_pairs.txt')
# tofile('spaCY_hypernymy\get_hype_base_lemma_sents.pkl', 'spaCY_hypernymy\get_hype_base_lemma_sents.txt')

# tofile('spaCY_hypernymy\\100_most_common.pkl', 'spaCY_hypernymy\\100_most_common.txt')
#tofile('spaCY_hypernymy\_pairs_containing_common.pkl', 'spaCY_hypernymy\_pairs_containing_common.txt')
# tofile('spaCY_hypernymy\_NP-VPoneword.pkl', 'spaCY_hypernymy\_NP-VPoneword.txt')
# tofile('spaCY_hypernymy\_all_oneVP_pairs.pkl', 'spaCY_hypernymy\_all_oneVP_pairs.txt')
# tofile('spaCY_hypernymy\_all_AP_VP_pairs.pkl', 'spaCY_hypernymy\_all_AP_VP_pairs.txt')

#tofile('spaCY_hypernymy\_pairs_containing_and_common.pkl', 'spaCY_hypernymy\_pairs_containing_and_common.txt')
