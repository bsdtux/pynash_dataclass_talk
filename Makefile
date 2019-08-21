SHELL:=/bin/bash
BATTLE_HERO=$(subst battle-,,$(@))
JSON_HERO=$(subst json-,,$(@))

battle-%:
	simulator --battle ${BATTLE_HERO}

json-%:
	simulator --json ${JSON_HERO}
