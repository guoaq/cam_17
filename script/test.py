
from ana_survey import * 

d = read_csv("../survey/170209-belle-fm-fixture-E_guo.csv",sep=";")

newfile = '../result/survey_KEK'

x,y,z = Sel_points(d,newfile)

Plot_points(x,y,z,'test_survey_KEK')






