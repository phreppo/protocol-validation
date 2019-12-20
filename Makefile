all:
	@ make -s -C specification 

run:
	@make -s -C specification run

parse:
	@make -s -C specification parse

report:
	@ make -s -C report