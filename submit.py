


# vector = [4.898712714478583, -1.2439799891883509e-12, -2.374161028538222e-13, 8.145994377709371e-11, -1.7117817833960421e-10, -1.8366976965696096e-15, 6.35513405133212e-16, 2.3462516835537143e-05, -2.0472100298772093e-06, -1.4876080539133759e-08, 9.572911174164225e-10]# : [113206875020.648, 169702969009.363]
# vector = [3.335589197613109, -7.89537105303546e-13, -1.6845829852670346e-13, 2.316361297984149e-11, -1.7558614944454155e-10, -1.4792800881711402e-15, 6.931746370457392e-16, 2.211778254595069e-05, -1.8618297937180475e-06, -1.7317438552159648e-08, 9.345585304057048e-10] : [111388900371.54839, 138659314680.84534]
# vector = [4.898712714478583, -1.2439799891883509e-12, -2.374161028538222e-13, 8.145994377709371e-11, -1.7117817833960421e-10, -1.8366976965696096e-15, 7.512327696275132e-16, 2.4555934980039217e-05, -1.990295686587803e-06, -1.8894707914486446e-08, 1.0081108294001304e-09] : [106817628185.466, 169919430320.51312]

# vector = [3.335589197613109, -7.89537105303546e-13, -1.6845829852670346e-13, 2.1318491169281167e-11, -1.7860563911642863e-10, -1.3835822952785652e-15, 7.234789325116876e-16, 2.211778254595069e-05, -1.8618297937180475e-06, -1.7317438552159648e-08, 9.345585304057048e-10] : [92212859074.61559, 151238356026.3178]
# vector = [2.2843186297203717, -8.739907583765651e-13, -1.6437340136948344e-13, 2.3616024753434204e-11, -1.9290454038564216e-10, -1.4896463542933527e-15, 6.383029704820937e-16, 2.308950006569273e-05, -1.8496330384350285e-06, -1.7428751240818852e-08, 9.215622172859837e-10]

vector = [2.198208805806239, -8.373813322512766e-13, -1.6496337197197626e-13, 2.4229126970082312e-11, -1.628257504095639e-10, -1.4632196009071528e-15, 6.202416990590212e-16, 2.3120152847186146e-05, -1.7272019740868676e-06, -1.7440471520650087e-08, 8.993218533696864e-10]

assert len(vector) == 11

ID = 'SOql4uavXyMdC9BTYktZDz152sPIhQLm6ucxoy2ujxmqb8o7E1'

from client2 import submit
print(submit(ID, vector))

# ([-10.0, -1.457990220064754e-12, -10.0, 4.620107525277624e-11, -1.7521481289918844e-10, -1.8366976965696096e-15, 8.529440604118815e-16, 2.2942330256117977e-05, -2.0472100298772093e-06, -1.597928341587757e-08, 9.982140340891233e-10], [13072745615.275206, 363475493334.69293])
# ([3.1949023879097087, -1.1566445813966808e-12, -1.706303783105885e-13, 7.164510593350617e-11, -2.9798027152778016e-10, -1.4938953170083339e-15, 1.5155307589985295e-15, 3.493791911133584e-05, -2.049689889668182e-06, -9.819094534206726e-09, 7.375886083349607e-10], [1585818192301.4272, 115225209097.53365])
# ([5.257715462208707, -1.5813775331788235e-12, -2.9480495309192186e-13, 8.593009830088329e-11, -1.332409515451414e-10, -1.6843765991129728e-15, 6.265155703236774e-16, 2.4411673897134494e-05, -2.0244212134558293e-06, -1.6416110433492366e-08, 9.756881052282443e-10], [25280444667.08707, 223402721178.2745])

# [3.5087298397576405, -1.1826938839898644e-12, -3.6492793406562876e-13, 6.424792201564891e-11, -1.7580741026875796e-10, -1.5038227131691847e-15, 7.321390443144845e-16, 2.1156061371918495e-05, -2.1593377914505938e-06, -1.9208052673185773e-08, 1.051047646013754e-09] : [2147115875295.7356, 3295475593481.603]
# vector = [5.257715462208707, -1.5813775331788235e-12, -2.9480495309192186e-13, 8.593009830088329e-11, -1.332409515451414e-10, -1.6843765991129728e-15, 6.265155703236774e-16, 2.4411673897134494e-05, -2.0244212134558293e-06, -1.6416110433492366e-08, 9.756881052282443e-10]
# vector = [-10, -1.5813775331788235e-12, -2.9480495309192186e-13, 8.593009830088329e-11, -1.332409515451414e-10, -1.6843765991129728e-15, 6.265155703236774e-16, 2.4411673897134494e-05, -2.0244212134558293e-06, -1.6416110433492366e-08, 9.756881052282443e-10]
# vector = [4.705047092684407, -1.4772040011613657e-12, -1.8825763307931724e-13, 9.781133221291978e-11, -2.0913757231551474e-10, -1.2268411517146056e-15, 7.22798542127232e-16, 2.2750291005191946e-05, -1.4004548558200827e-06, -1.8419700719922213e-08, 6.991112756193292e-10]
# vector  = [4.507674867929613, -1.5335125686089102e-12, -1.8413131517730056e-13, 9.311510481796091e-11, -1.9785349872009217e-10, -1.2102881864517688e-15, 7.977328881107871e-16, 2.1934669493572696e-05, -1.4594388217074661e-06, -1.7600494029406784e-08, 7.665700643861209e-10]
# vector = [4.572754504629397, -9.610070824266873e-13, -1.8015496102065248e-13, 8.254852692264057e-11, -1.7547127291621515e-10, -2.054196020876703e-15, 6.322725306084644e-16, 2.4958838782053804e-05, -2.0108744112797645e-06, -1.818482794810048e-08, 1.007744569152792e-09]

