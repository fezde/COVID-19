CHDIR_SHELL := $(SHELL)
define chdir
   $(eval _D=$(firstword $(1) $(@D)))
   $(info $(MAKE): cd $(_D)) $(eval SHELL = cd $(_D); $(CHDIR_SHELL))
endef

NOW = $(shell date "+%Y%m%d-%H%M%S")
export DEBUG_LEVEL = INFO

gatsby/develop:
	$(call chdir)
	gatsby clean
	yes | gatsby develop

gatsby/deploy:
	$(call chdir)
	gatsby clean
	npm run deploy

render_charts:
	python3 basic_numbers.py
	python3 rates.py
	python3 offsets.py
	python3 daily_changes.py
	python3 ill.py
	python3 opengraph_image.py

render_ip_map_animation: BASEDIR := charts/ill_people_map
render_ip_map_animation:
	python3 ip_map_animation.py

	convert -delay 30 -loop 0 $(BASEDIR)/tmp/ip_map_2020-*.png $(BASEDIR)/ip_map-tmp.gif
	convert $(BASEDIR)/ip_map-tmp.gif  \( -clone -1 -set delay 500 \) $(BASEDIR)/ip_map-$(NOW).gif
	rm $(BASEDIR)/ip_map-tmp.gif
	cp $(BASEDIR)/ip_map-$(NOW).gif charts/_current/ip_map.gif
	convert charts/_current/ip_map.gif -scale 40% charts/_current/ip_map_small.gif

all: render_ip_map_animation render_charts gatsby/deploy