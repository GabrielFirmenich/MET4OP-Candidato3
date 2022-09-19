from distutils.command.build_scripts import first_line_re


firstline = "Hello World"
keys = ["CandidatoA", "CandidatoB", "CandidatoC", "CandidatoD"]
values = [300, 250, 200, 60]
votos = dict(zip(keys, values))
print(votos)
# %%